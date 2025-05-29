import pytest
from modules.ui.page_objects.rozetka_login_page import RozetkaLoginPage

# UI test for negative login on rozetka.com.ua
@pytest.mark.ui
def test_rozetka_login_fail():
    page = RozetkaLoginPage()
    page.go_to()

    # Open login window and use email method
    page.open_login_modal()
    page.choose_email_login()

    # Enter wrong email and password
    page.enter_credentials("ivan.nikitenko@mistakeinemail.com", "wrong password")

    # Click the 'Continue' button and wait shortly
    page.submit_login()

    # Close browser
    page.close()