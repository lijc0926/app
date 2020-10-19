import datetime
import uiautomator2 as ut2
import allure
import pytest
import config
import time
import conftest
d = ut2.connect_usb(config.device_name)

#28826 主图画面“比例尺”按钮缩放
def test_scale_28826():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    d(resourceId="com.ecarx.adnavi:id/scale_reduce").click()
    d(resourceId="com.ecarx.adnavi:id/scale_reduce").click()
    d(resourceId="com.ecarx.adnavi:id/scale_reduce").click()
    d(resourceId="com.ecarx.adnavi:id/scale_reduce").click()
    d(resourceId="com.ecarx.adnavi:id/scale_reduce").click()
    while d(resourceId="com.ecarx.adnavi:id/scale_title").get_text() not in "200米":
        d(resourceId="com.ecarx.adnavi:id/scale_add").click()
    d(resourceId="com.ecarx.adnavi:id/scale_add").click()
    assert d(resourceId="com.ecarx.adnavi:id/scale_title").get_text() in "100米"
    d(resourceId="com.ecarx.adnavi:id/scale_add").click()
    assert d(resourceId="com.ecarx.adnavi:id/scale_title").get_text() in "50米"
    d(resourceId="com.ecarx.adnavi:id/scale_reduce").click()
    assert d(resourceId="com.ecarx.adnavi:id/scale_title").get_text() in "100米"
    d(resourceId="com.ecarx.adnavi:id/scale_reduce").click()
    assert d(resourceId="com.ecarx.adnavi:id/scale_title").get_text() in "200米"

#28760 逆地理扎标显示
def test_inversePOI_28760():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    d.long_click(0.292, 0.613)
    assert d(resourceId="com.ecarx.adnavi:id/btn_poi_destination").wait()

#28793 扎标详细信息页按钮操作
def test_inversePOIDetails_28793():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    d.long_click(0.292, 0.613)
    d(resourceId="com.ecarx.adnavi:id/btn_poi_destination").click()
    time.sleep(2)
    d.swipe(0.626, 0.843, 0.684, 0.243)
    assert d(resourceId="com.ecarx.adnavi:id/route_start_guidance").wait()
    d.press("back")
    d(resourceId="com.ecarx.adnavi:id/iv_near_search").click()
    assert d(resourceId="com.ecarx.adnavi:id/module_search_fragment_search_entrance_search").wait()
    d.press("back")
    d.long_click(0.292, 0.613)
    time.sleep(1)
    d(resourceId="com.ecarx.adnavi:id/iv_collect").click()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_toast_message").get_text() in "收藏成功"
    d(resourceId="com.ecarx.adnavi:id/iv_collect").click()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_toast_message").get_text() in "取消收藏"
    d(resourceId="com.ecarx.adnavi:id/iv_poi_cancel").click()

#28765 回车位按钮的操作
def test_Return_space_28765():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    d.swipe(0.194, 0.469, 0.732, 0.478)
    d(resourceId='com.ecarx.adnavi:id/map_revert').click()

#28800 在线模式下路况信息开关状态切换
def test_Road_conditions_28800():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    d(resourceId="com.ecarx.adnavi:id/state_time").click()
    d(resourceId="com.ecarx.adnavi:id/map_traffic_group").click()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_toast_message").get_text() in "路况已关闭"
    d.press("back")
    d(resourceId="com.ecarx.adnavi:id/state_time").click()
    d(resourceId="com.ecarx.adnavi:id/map_traffic_group").click()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_toast_message").get_text() in "路况已开启"
    d.press("back")

#28807 主图画面“更多”按钮的显示及操作
def test_user_28807():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    assert d(resourceId="com.ecarx.adnavi:id/map_more").wait()
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    assert d(resourceId="com.ecarx.adnavi:id/module_user_fragment_login_layout").wait()
    d.press("back")

#28808 主图画面“搜索”按钮的显示及操作
def test_search_28808():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    assert d(resourceId="com.ecarx.adnavi:id/map_search").wait()
    d(resourceId="com.ecarx.adnavi:id/map_search").click()
    assert d(resourceId="com.ecarx.adnavi:id/module_search_fragment_search_entrance_tv_input_area").wait()
    d.press("back")

#28809 主图画面“家”按钮的显示及操作
def test_Family_28809():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
# 增加历史目的地
    d(resourceId="com.ecarx.adnavi:id/map_search").click()
    d(resourceId="com.ecarx.adnavi:id/module_search_fragment_search_entrance_tv_input_area").click()
    d(resourceId="com.ecarx.adnavi:id/module_search_one_search_et_search_content").set_text("虹桥火车站")
    d(resourceId="com.ecarx.adnavi:id/module_search_one_search_btn_start_search").click()
    d(resourceId="com.ecarx.adnavi:id/module_search_search_result_btn_confirm_select").click()
    d(resourceId="com.ecarx.adnavi:id/route_start_guidance").click()
    d.press("back")

    assert d(resourceId="com.ecarx.adnavi:id/map_familiar_road").wait()
    d(resourceId="com.ecarx.adnavi:id/map_familiar_road").click()
    assert d(resourceId="com.ecarx.adnavi:id/module_user_frament_add_address_back_layout").wait()
    time.sleep(3)
    d(resourceId="com.ecarx.adnavi:id/module_user_item_add_address_set_iv").click()
    d(resourceId="com.ecarx.adnavi:id/map_familiar_road").click()
    time.sleep(3)
    assert d(resourceId="com.ecarx.adnavi:id/layout_guidance_card").wait()
    d.swipe(0.194, 0.469, 0.732, 0.478)
    d.press("back")
# 进入收藏删除收藏家 回到未收藏状态
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    d(resourceId="com.ecarx.adnavi:id/module_user_collection_layout").click()
    d(resourceId="com.ecarx.adnavi:id/module_user_fragment_home_delete_iv").click()
    d(resourceId="com.ecarx.adnavi:id/tv_simple_dialog_confirm").click()

#28810 主图画面“公司”按钮的显示及操作
def test_company_28810():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    assert d(resourceId="com.ecarx.adnavi:id/map_company").wait()
    d(resourceId="com.ecarx.adnavi:id/map_company").click()
    assert d(resourceId="com.ecarx.adnavi:id/module_user_frament_add_address_back_layout").wait()
    d(resourceId="com.ecarx.adnavi:id/module_user_item_add_address_set_iv").click()
    d(resourceId="com.ecarx.adnavi:id/map_company").click()
    time.sleep(3)
    assert d(resourceId="com.ecarx.adnavi:id/layout_guidance_card").wait()
    d.swipe(0.194, 0.469, 0.732, 0.478)
    d.press("back")
# 进入收藏删除收藏的公司 回到未收藏状态
    d(resourceId="com.ecarx.adnavi:id/map_more").click()
    d(resourceId="com.ecarx.adnavi:id/module_user_collection_layout").click()
    d(resourceId="com.ecarx.adnavi:id/module_user_fragment_company_delete_iv").click()
    d(resourceId="com.ecarx.adnavi:id/tv_simple_dialog_confirm").click()

#28814 主图画面“回车位”按钮的显示
def test_Returnspace_operating_28814():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    d.swipe(0.194, 0.469, 0.732, 0.478)
    assert d(resourceId='com.ecarx.adnavi:id/map_revert').wait()
    d(resourceId='com.ecarx.adnavi:id/map_revert').click()
    assert d(resourceId="com.ecarx.adnavi:id/map_revert").wait() is not True
    d.swipe(0.194, 0.469, 0.732, 0.478)
    assert d(resourceId='com.ecarx.adnavi:id/map_revert').wait()
    time.sleep(16)
    assert d(resourceId="com.ecarx.adnavi:id/map_revert").wait() is not True

#28832 主图画面“车标”的操作
def test_position_28832():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    d.click(0.518, 0.496)
    assert d(resourceId="com.ecarx.adnavi:id/tv_poi_name").get_text() in "我的位置"
    d.press("back")
    assert d(resourceId="com.ecarx.adnavi:id/map_revert").wait() is not True

#28828 主图画面“音量”按钮的显示及操作
def test_Broadcast_28828():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    assert d(resourceId="com.ecarx.adnavi:id/map_sound").wait()
    d(resourceId="com.ecarx.adnavi:id/map_sound").click()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_toast_message").get_text() in "已静音"
    d(resourceId="com.ecarx.adnavi:id/map_sound").click()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_toast_message").get_text() in "已恢复播报"
    #进入导航
    d.long_click(0.292, 0.613)
    d(resourceId="com.ecarx.adnavi:id/btn_poi_destination").click()
    d(resourceId="com.ecarx.adnavi:id/route_start_guidance").click()
    time.sleep(1)
    assert d(resourceId="com.ecarx.adnavi:id/iv_mute").wait() is not True
    d.swipe(0.194, 0.469, 0.732, 0.478)
    d(resourceId="com.ecarx.adnavi:id/iv_mute").click()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_toast_message").get_text() in "已静音"
    d(resourceId="com.ecarx.adnavi:id/iv_mute").click()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_toast_message").get_text() in "已恢复播报"

#28833 主图画面“状态栏弹窗”的显示
def test_Status_bar_display_28833():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    d(resourceId="com.ecarx.adnavi:id/state_net").click()
    assert d(resourceId="com.ecarx.adnavi:id/map_traffic_group").wait()
    assert d(resourceId="com.ecarx.adnavi:id/map_gps_group").wait()
    assert d(resourceId="com.ecarx.adnavi:id/map_front_facing_icon").wait()
    assert d(resourceId="com.ecarx.adnavi:id/map_state_detail_close").wait()
    d(resourceId="com.ecarx.adnavi:id/map_state_detail_close").click()

#28834 主图画面“状态栏弹窗”的操作
def test_Status_bar_operating_28834():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    d(resourceId="com.ecarx.adnavi:id/state_net").click()
    d(resourceId="com.ecarx.adnavi:id/map_front_facing_icon").click()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_toast_message").get_text() in "已切换至:3D车头向上"

    d(resourceId="com.ecarx.adnavi:id/map_front_facing_icon").click()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_toast_message").get_text() in "已切换至:2D正北向上"

    d(resourceId="com.ecarx.adnavi:id/map_traffic_group").click()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_toast_message").get_text() in "路况已关闭"

    d(resourceId="com.ecarx.adnavi:id/map_traffic_group").click()
    assert d(resourceId="com.ecarx.adnavi:id/tv_simple_toast_message").get_text() in "路况已开启"

    d(resourceId="com.ecarx.adnavi:id/map_gps_group").click()
    assert d(resourceId="com.ecarx.adnavi:id/module_map_barchartview").wait()
    d(resourceId="com.ecarx.adnavi:id/module_map_button_exit_gps_detail").click()
    d(resourceId="com.ecarx.adnavi:id/map_state_detail_close").click()
     #判断15秒消失
    d(resourceId="com.ecarx.adnavi:id/state_net").click()
    time.sleep(16)
    assert d(resourceId="com.ecarx.adnavi:id/map_front_facing_icon").wait() is not True

#28761 逆地理信息页显示
def test_Details_page_information_28761():
    time.sleep(1)
    while d(resourceId="com.ecarx.adnavi:id/map_search").wait() is not True:
        d.press("back")
    d.long_click(0.292, 0.613)
    assert d(resourceId="com.ecarx.adnavi:id/btn_poi_destination").wait()
    assert d(resourceId="com.ecarx.adnavi:id/tv_poi_name").wait()
    assert d(resourceId="com.ecarx.adnavi:id/tv_poi_address").wait()
    assert d(resourceId="com.ecarx.adnavi:id/tv_poi_distance").wait()
    d(resourceId="com.ecarx.adnavi:id/iv_poi_cancel").click()

