# -*- coding:utf-8 -*-


import datetime
import uiautomator2 as ut2
import allure
import pytest
import config
import time
import conftest
d = ut2.connect_usb(config.device_name)


# 29029地图文字大小设置显示
def test_cache_setting_29029():
    while not d(resourceId="com.ecarx.adnavi:id/map_search").wait():
        d.press("back")
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_iv_standard_font").wait()
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_iv_big_font").wait()


# 29030设置地图文字为大字号
def test_cache_setting_29030():
    while not d(resourceId="com.ecarx.adnavi:id/map_search").wait():
        d.press("back")
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    time.sleep(2)
    d(resourceId="com.ecarx.adnavi:id/module_setting_iv_big_font").click()
    time.sleep(2)
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_iv_big_font", selected=True).wait()


# 29031设置地图文字为标准字号
def test_cache_setting_29031():
    while not d(resourceId="com.ecarx.adnavi:id/map_search").wait():
        d.press("back")
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    time.sleep(2)
    d(resourceId="com.ecarx.adnavi:id/module_setting_iv_standard_font").click()
    time.sleep(2)
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_iv_standard_font", selected=True).wait()


# 29032导航中修改地图文字大小
def test_cache_setting_29032():
    while not d(resourceId="com.ecarx.adnavi:id/map_search").wait():
        d.press("back")
    d(resourceId="com.ecarx.adnavi:id/map_search").click()
    d(resourceId="com.ecarx.adnavi:id/module_search_fragment_search_entrance_tv_input_area").click()
    d(resourceId="com.ecarx.adnavi:id/module_search_one_search_et_search_content").set_text("徐家汇")
    d(resourceId="com.ecarx.adnavi:id/module_search_one_search_btn_start_search").click()
    d(resourceId="com.ecarx.adnavi:id/module_search_search_result_btn_confirm_select").click()
    d(resourceId="com.ecarx.adnavi:id/route_radar").click()
    time.sleep(2)
    d.click(0.302, 0.565)
    d(resourceId="com.ecarx.adnavi:id/iv_more").click()
    d(resourceId="com.ecarx.adnavi:id/ll_settings").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    time.sleep(2)
    d(resourceId="com.ecarx.adnavi:id/module_setting_iv_big_font").click()
    time.sleep(2)
    d(resourceId="com.ecarx.adnavi:id/module_setting_back_iv").click()
    d.click(0.302, 0.565)
    d(resourceId="com.ecarx.adnavi:id/iv_more").click()
    d(resourceId="com.ecarx.adnavi:id/ll_settings").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_iv_big_font", selected=True).wait()
    d(resourceId="com.ecarx.adnavi:id/module_setting_back_iv").click()
    d.click(0.302, 0.565)
    d(resourceId="com.ecarx.adnavi:id/iv_more").click()
    d(resourceId="com.ecarx.adnavi:id/ll_settings").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_iv_standard_font", selected=True).wait()
    d(resourceId="com.ecarx.adnavi:id/module_setting_back_iv").click()
    d.click(0.302, 0.565)
    d(resourceId="com.ecarx.adnavi:id/iv_more").click()
    d(resourceId="com.ecarx.adnavi:id/ll_settings").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_iv_standard_font", selected=True).wait()


# 29033熟路导航中修改地图文字大小
def test_cache_setting_29033():
    while not d(resourceId="com.ecarx.adnavi:id/map_search").wait():
        d.press("back")
    d(resourceId="com.ecarx.adnavi:id/map_search").click()
    d(resourceId="com.ecarx.adnavi:id/module_search_fragment_search_entrance_tv_input_area").click()
    d(resourceId="com.ecarx.adnavi:id/module_search_one_search_et_search_content").set_text("徐家汇")
    d(resourceId="com.ecarx.adnavi:id/module_search_one_search_btn_start_search").click()
    d(resourceId="com.ecarx.adnavi:id/module_search_search_result_btn_confirm_select").click()
    d(resourceId="com.ecarx.adnavi:id/route_radar").click()
    time.sleep(2)
    d.click(0.302, 0.565)
    d(resourceId="com.ecarx.adnavi:id/iv_more").click()
    d(resourceId="com.ecarx.adnavi:id/ll_settings").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    time.sleep(2)
    d(resourceId="com.ecarx.adnavi:id/module_setting_iv_big_font").click()
    time.sleep(2)
    d(resourceId="com.ecarx.adnavi:id/module_setting_back_iv").click()
    d.click(0.302, 0.565)
    d(resourceId="com.ecarx.adnavi:id/iv_more").click()
    d(resourceId="com.ecarx.adnavi:id/ll_settings").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_iv_big_font", selected=True).wait()
    d(resourceId="com.ecarx.adnavi:id/module_setting_back_iv").click()
    d.click(0.302, 0.565)
    d(resourceId="com.ecarx.adnavi:id/iv_more").click()
    d(resourceId="com.ecarx.adnavi:id/ll_settings").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_iv_standard_font", selected=True).wait()
    d(resourceId="com.ecarx.adnavi:id/module_setting_back_iv").click()
    d.click(0.302, 0.565)
    d(resourceId="com.ecarx.adnavi:id/iv_more").click()
    d(resourceId="com.ecarx.adnavi:id/ll_settings").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_iv_standard_font", selected=True).wait()


# 29037点击已选择的文字大小
def test_cache_setting_29037():
    while not d(resourceId="com.ecarx.adnavi:id/map_search").wait():
        d.press("back")
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    time.sleep(2)
    d(resourceId="com.ecarx.adnavi:id/module_setting_iv_standard_font").click()
    time.sleep(2)
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_iv_standard_font", selected=True).wait()
    time.sleep(2)
    d(resourceId="com.ecarx.adnavi:id/module_setting_iv_standard_font").click()
    time.sleep(2)
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_iv_standard_font", selected=True).wait()


# 29036地图文字大小继承
def test_cache_setting_29036():
    while not d(resourceId="com.ecarx.adnavi:id/map_search").wait():
        d.press("back")
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    time.sleep(2)
    d(resourceId="com.ecarx.adnavi:id/module_setting_iv_big_font").click()
    time.sleep(2)
    d.press("back")
    d.press("back")
    d(resourceId="com.ecarx.adnavi:id/map_search").click()
    d(resourceId="com.ecarx.adnavi:id/module_search_fragment_search_entrance_tv_input_area").click()
    d(resourceId="com.ecarx.adnavi:id/module_search_one_search_et_search_content").set_text("徐家汇")
    d(resourceId="com.ecarx.adnavi:id/module_search_one_search_btn_start_search").click()
    d(resourceId="com.ecarx.adnavi:id/module_search_search_result_btn_confirm_select").click()
    d(resourceId="com.ecarx.adnavi:id/route_radar").click()
    time.sleep(2)
    d.click(0.302, 0.565)
    d(resourceId="com.ecarx.adnavi:id/iv_more").click()
    d(resourceId="com.ecarx.adnavi:id/ll_settings").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    time.sleep(2)
    d(resourceId="com.ecarx.adnavi:id/module_setting_iv_big_font", selected=True).wait()


# 29035地图文字大字号显示
def test_cache_setting_29035():
    while not d(resourceId="com.ecarx.adnavi:id/map_search").wait():
        d.press("back")
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    time.sleep(2)
    d(resourceId="com.ecarx.adnavi:id/module_setting_iv_big_font").click()
    time.sleep(2)
    d.press("back")
    d.press("back")
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    time.sleep(2)
    d(resourceId="com.ecarx.adnavi:id/module_setting_iv_big_font", selected=True).wait()


# 29034地图文字标准字号显示
def test_cache_setting_29034():
    while not d(resourceId="com.ecarx.adnavi:id/map_search").wait():
        d.press("back")
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    time.sleep(2)
    d(resourceId="com.ecarx.adnavi:id/module_setting_iv_standard_font").click()
    time.sleep(2)
    d.press("back")
    d.press("back")
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_map").click()
    d.swipe(0.542, 0.721, 0.566, 0.239)
    time.sleep(2)
    d(resourceId="com.ecarx.adnavi:id/module_setting_iv_standard_font", selected=True).wait()



