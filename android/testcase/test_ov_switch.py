# -*- coding:utf-8 -*-


import datetime
import uiautomator2 as ut2
import allure
import pytest
import config
import time
d = ut2.connect_usb(config.device_name)

def test_ov_switch():
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    d(resourceId="com.ecarx.adnavi:id/state_net").click()
    try:
        while d(resourceId="com.ecarx.adnavi:id/map_front_facing_content").get_text() != "2D正北向上":
            d(resourceId="com.ecarx.adnavi:id/map_front_facing_icon").click()
            break
    finally:
        d(resourceId="com.ecarx.adnavi:id/map_state_detail_close").click()
    ovc_1_c_list = []
    ovc_1_c_time = 0
    ovc_2_c_list = []
    ovc_2_c_time = 0
    rcs_1_c_list = []
    rcs_1_c_time = 0
    rcs_2_c_list = []
    rcs_2_c_time = 0
    i = 0
    j = 3
    while i < j:
        # 全览小窗模式
        time.sleep(2)
        d(resourceId="com.ecarx.adnavi:id/map_more").click()
        time.sleep(2)
        d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
        time.sleep(2)
        d.swipe(0.55, 0.834, 0.56, 0.239)
        time.sleep(2)
        d(resourceId="com.ecarx.adnavi:id/module_setting_iv_small_map").click()
        time.sleep(2)
        d.press("back")
        time.sleep(2)
        d.press("back")
        d(resourceId="com.ecarx.adnavi:id/map_search").click()
        time.sleep(0.5)
        d(resourceId="com.ecarx.adnavi:id/module_search_fragment_search_entrance_tv_input_area").click()
        time.sleep(0.5)
        d(text="输入目的地").set_text("徐家汇公园")
        time.sleep(0.5)
        d(resourceId="com.ecarx.adnavi:id/module_search_item_one_search_history_search_poi_name").click()
        time.sleep(0.5)
        d(resourceId="com.ecarx.adnavi:id/btn_poi_destination").click()
        time.sleep(0.5)
        d(resourceId="com.ecarx.adnavi:id/route_start_guidance").click()
        time.sleep(4)
        as1 = d(resourceId="com.ecarx.adnavi:id/tv_scale_title").get_text()
        time.sleep(3)
        d(resourceId="com.ecarx.adnavi:id/minimapLL").click()
        time.sleep(3)
        ovc_1_start_time = datetime.datetime.now()
        as2 = d(resourceId="com.ecarx.adnavi:id/tv_scale_title").get_text()
        assert as1 != as2
        ovc_1_end_time = datetime.datetime.now()
        ovc_1_all_time = (ovc_1_end_time - ovc_1_start_time).total_seconds()
        ovc_1_c_list.append(str(round(ovc_1_all_time, 3)))
        ovc_1_c_time += ovc_1_all_time
        time.sleep(5)
        d(resourceId="com.ecarx.adnavi:id/minimapLL").click()
        time.sleep(3)
        ovc_2_start_time = datetime.datetime.now()
        as3 = d(resourceId="com.ecarx.adnavi:id/tv_scale_title").get_text()
        assert as2 != as3
        ovc_2_end_time = datetime.datetime.now()
        ovc_2_all_time = (ovc_2_end_time - ovc_2_start_time).total_seconds()
        ovc_2_c_list.append(str(round(ovc_2_all_time, 3)))
        ovc_2_c_time += ovc_2_all_time
        d.press("back")
        time.sleep(4)
        # 路况条模式
        d(resourceId="com.ecarx.adnavi:id/map_more").click()
        time.sleep(2)
        d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
        time.sleep(2)
        d.swipe(0.55, 0.834, 0.56, 0.239)
        time.sleep(2)
        d(resourceId="com.ecarx.adnavi:id/module_setting_iv_road_twig").click()
        time.sleep(2)
        d.press("back")
        time.sleep(2)
        d.press("back")
        d(resourceId="com.ecarx.adnavi:id/map_search").click()
        time.sleep(0.5)
        d(resourceId="com.ecarx.adnavi:id/module_search_fragment_search_entrance_tv_input_area").click()
        time.sleep(0.5)
        d(text="输入目的地").set_text("徐家汇公园")
        time.sleep(0.5)
        d(resourceId="com.ecarx.adnavi:id/module_search_item_one_search_history_search_poi_name").click()
        time.sleep(0.5)
        d(resourceId="com.ecarx.adnavi:id/btn_poi_destination").click()
        time.sleep(0.5)
        d(resourceId="com.ecarx.adnavi:id/route_start_guidance").click()
        time.sleep(4)
        d(resourceId="com.ecarx.adnavi:id/iv_full_sight").wait(1)
        time.sleep(1)
        as4 = d(resourceId="com.ecarx.adnavi:id/tv_scale_title").get_text()
        time.sleep(4)
        d(resourceId="com.ecarx.adnavi:id/iv_full_sight").click()
        rcs_1_start_time = datetime.datetime.now()
        as5 = d(resourceId="com.ecarx.adnavi:id/tv_scale_title").get_text()
        assert as4 != as5
        rcs_1_end_time = datetime.datetime.now()
        rcs_1_all_time = (rcs_1_end_time - rcs_1_start_time).total_seconds()
        rcs_1_c_list.append(str(round(rcs_1_all_time, 3)))
        rcs_1_c_time += rcs_1_all_time
        time.sleep(5)
        d(resourceId="com.ecarx.adnavi:id/iv_full_sight").click()
        rcs_2_start_time = datetime.datetime.now()
        as6 = d(resourceId="com.ecarx.adnavi:id/tv_scale_title").get_text()
        assert as5 != as6
        rcs_2_end_time = datetime.datetime.now()
        rcs_2_all_time = (rcs_2_end_time - rcs_2_start_time).total_seconds()
        rcs_2_c_list.append(str(round(rcs_2_all_time, 3)))
        rcs_2_c_time += rcs_2_all_time
        d.press("back")
        time.sleep(2)
        d(resourceId="com.ecarx.adnavi:id/map_more").click()
        time.sleep(2)
        d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
        time.sleep(2)
        d.swipe(0.55, 0.834, 0.56, 0.239)
        time.sleep(2)
        d(resourceId="com.ecarx.adnavi:id/module_setting_iv_small_map").click()
        time.sleep(2)
        d.press("back")
        time.sleep(2)
        d.press("back")
        i += 1
    with open("D:\\wook\\log_demo\\全览模式切换.log", 'w', encoding='utf-8') as f:
        f.write('全览模式切换' + "\n")
        f.write("点击进入全览小窗模式")
        for k in range(len(ovc_1_c_list)):
            f.write(',' + ovc_1_c_list[k])
        f.write(',' + str(round(ovc_1_c_time / j, 3)) + '\n')
        f.write("点击退出全览小窗模式")
        for k in range(len(ovc_2_c_list)):
            f.write(',' + ovc_2_c_list[k])
        f.write(',' + str(round(ovc_2_c_time / j, 3)) + '\n')
        f.write("点击进入路况条模式")
        for k in range(len(rcs_1_c_list)):
            f.write(',' + rcs_1_c_list[k])
        f.write(',' + str(round(rcs_1_c_time / j, 3)) + '\n')
        f.write("点击退出路况条模式")
        for k in range(len(rcs_2_c_list)):
            f.write(',' + rcs_2_c_list[k])
        f.write(',' + str(round(rcs_2_c_time / j, 3)) + '\n')