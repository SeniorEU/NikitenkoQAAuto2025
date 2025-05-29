from modules.ui.page_objects.sign_in_page import SignInPage
import pytest

@pytest.mark.ui
def test_check_incorrect_username_page_object():
    
    # creating a page object
    sign_in_page = SignInPage()
    
    # open the page https://github.com/login
    sign_in_page.go_to()
    
    # attempt to log in to the GitHub system
    sign_in_page.try_login("ivan.nikitenko@mistakeinemail.com", "wrong password")
    print("\033[94mAttempt to log in with incorrect credentials\033[0m")
    
    # Check that the page title is what we expect
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
    print("\033[94mPage title is correct\033[0m")
    
    # Close the browser
    sign_in_page.close()