import time


def test_tc_10_034_02(page):
    """Переходим по ссылке"""
    page.goto("/")

    expected_url = "http://localhost:8080/manage/"
    expected_status = 302

    user_settings_btn_loc = "a[id='root-action-ManageJenkinsAction']"

    with page.expect_response(lambda response: response.status) as response_info:
        page.locator(user_settings_btn_loc).click()
    print(f"response info: {response_info.value}")

    response = response_info.value
    status_code = response.status
    print(status_code)

    actual_url = page.url

    assert actual_url == expected_url and status_code == expected_status