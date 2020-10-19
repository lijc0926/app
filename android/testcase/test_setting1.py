# -*- coding:utf-8 -*-


import datetime
import uiautomator2 as ut2
import allure
import pytest
import config
import time
import conftest
d = ut2.connect_usb(config.device_name)


# 29066取消清除缓存
def test_cache_setting_29066():
    while not d(resourceId="com.ecarx.adnavi:id/map_search").wait():
        d.press("back")
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_other").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_other_clean_cache").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/tv_simple_dialog_cancel").click()
    time.sleep(0.5)
    assert not d(resourceId="com.ecarx.adnavi:id/tv_simple_dialog_cancel").wait()
    d(resourceId="com.ecarx.adnavi:id/module_setting_other_clean_cache").click()
    time.sleep(1)
    d.click(0.85, 0.504)
    assert not d(resourceId="com.ecarx.adnavi:id/tv_simple_dialog_cancel").wait()


# 29065路线规划页进入导航设置清除缓存
def test_cache_setting_29065():
    while not d(resourceId="com.ecarx.adnavi:id/map_search").wait():
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
    d(resourceId="com.ecarx.adnavi:id/route_more").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/more_setting").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_other").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_other_clean_cache").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/tv_simple_dialog_confirm").click()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_toast_message").get_text() == "已清除缓存"


# 29064熟路导航中清除缓存
def test_cache_setting_29064():
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
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_other").click()
    time.sleep(1)
    d(resourceId="com.ecarx.adnavi:id/module_setting_other_clean_cache").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/tv_simple_dialog_confirm").click()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_toast_message").get_text() == "已清除缓存"


# 29063 导航中清除缓存
def test_cache_setting_29063():
    while not d(resourceId="com.ecarx.adnavi:id/map_search").wait():
        d.press("back")
    d(resourceId="com.ecarx.adnavi:id/map_search").click()
    d(resourceId="com.ecarx.adnavi:id/module_search_fragment_search_entrance_tv_input_area").click()
    d(resourceId="com.ecarx.adnavi:id/module_search_one_search_et_search_content").set_text("徐家汇")
    d(resourceId="com.ecarx.adnavi:id/module_search_one_search_btn_start_search").click()
    d(resourceId="com.ecarx.adnavi:id/module_search_search_result_btn_confirm_select").click()
    d(resourceId="com.ecarx.adnavi:id/route_start_guidance").click()
    time.sleep(2)
    d.click(0.302, 0.565)
    d(resourceId="com.ecarx.adnavi:id/iv_more").click()
    d(resourceId="com.ecarx.adnavi:id/ll_settings").click()
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_other").click()
    time.sleep(1)
    d(resourceId="com.ecarx.adnavi:id/module_setting_other_clean_cache").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/tv_simple_dialog_confirm").click()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_toast_message").get_text() == "已清除缓存"


# 29062 清除缓存
def test_cache_setting_29062():
    while not d(resourceId="com.ecarx.adnavi:id/map_search").wait():
        d.press("back")
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_other").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_other_clean_cache").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/tv_simple_dialog_confirm").click()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_toast_message").get_text() == "已清除缓存"
    time.sleep(3)
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_cache_size").get_text() == "约0.00KB"


# 29061 点击清除缓存
def test_cache_setting_29061():
    while not d(resourceId="com.ecarx.adnavi:id/map_search").wait():
        d.press("back")
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_other").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_other_clean_cache").click()
    time.sleep(0.5)
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_dialog_confirm").wait()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_dialog_cancel").wait()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/tv_simple_dialog_cancel").click()


# 29060 清除缓存显示
def test_cache_setting_29060():
    while not d(resourceId="com.ecarx.adnavi:id/map_search").wait():
        d.press("back")
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_other").click()
    time.sleep(0.5)
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_other_clean_cache").wait()
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_cache_size").wait()
