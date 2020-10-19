# -*- coding:utf-8 -*-


import datetime
import uiautomator2 as ut2
import allure
import pytest
import config
import time
import conftest
d = ut2.connect_usb(config.device_name)

# 29079关于设置项显示
def test_setting_29079():
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_other").click()
    time.sleep(0.5)
    d.swipe(0.452, 0.773, 0.536, 0.239)
    time.sleep(0.5)
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_other_about_layout").wait()


# 29080点击关于
def test_setting_29080():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_other").click()
    time.sleep(0.5)
    d.swipe(0.452, 0.773, 0.536, 0.239)
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_other_about_layout").click()
    time.sleep(0.5)
    assert d(resourceId="com.ecarx.adnavi:id/module__setting_textview38").get_text() == "EMAP车机版"


# 29081关于页面显示
def test_setting_29081():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_other").click()
    time.sleep(0.5)
    d.swipe(0.452, 0.773, 0.536, 0.239)
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_other_about_layout").click()
    time.sleep(0.5)
    assert d(resourceId="com.ecarx.adnavi:id/module__setting_textview38").get_text() == "EMAP车机版"


# 29082 进入用户服务协议页面
def test_setting_29082():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_other").click()
    time.sleep(0.5)
    d.swipe(0.452, 0.773, 0.536, 0.239)
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_other_about_layout").click()
    time.sleep(0.5)
    assert d(resourceId="com.ecarx.adnavi:id/module_setting_about_service").get_text() == "服务条款"


# 29083 进入个人信息保护政策页面
def test_setting_29083():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_other").click()
    time.sleep(0.5)
    d.swipe(0.452, 0.773, 0.536, 0.239)
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_other_about_layout").click()
    time.sleep(0.5)
    assert d(resourceId="com.ecarx.adnavi:id/module__setting_textview78").get_text() == "隐私政策"


# 29084 进入帮助页面
def test_setting_29084():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_other").click()
    time.sleep(0.5)
    d.swipe(0.452, 0.773, 0.536, 0.239)
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_other_about_layout").click()
    time.sleep(0.5)
    assert d(resourceId="com.ecarx.adnavi:id/module__setting_textview80").get_text() == "帮助"


# 29087 帮助界面显示及操作
def test_setting_29087():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_user_setting_layout").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_other").click()
    time.sleep(0.5)
    d.swipe(0.452, 0.773, 0.536, 0.239)
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_other_about_layout").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_layout_about_help").click()
    time.sleep(0.5)
    assert d(resourceId="com.ecarx.adnavi:id/module__setting_textview43").get_text() == "帮助"
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_display").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_routeplan").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_search").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_voicebroad").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_tab_mapdata").click()
    time.sleep(0.5)
    d(resourceId="com.ecarx.adnavi:id/module_setting_help_iv_back").click()
    time.sleep(0.5)
    assert d(resourceId="com.ecarx.adnavi:id/module__setting_textview38").get_text() == "EMAP车机版"
