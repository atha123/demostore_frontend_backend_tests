import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
@pytest.mark.usefixtures("init_driver")
class TestIncorrectLogin:
    """
    This is a test for invalid login (non-existing users)
    @pytest.mark.tcid12
    @pytest.mark.ecomfe9
    @pytest.mark.smoke
    """
    @pytest.mark.lp002
        # Go to the 'My Account' page directly
    def test_invalid_user_login(self):
        account=MyAccountSignedOut(self.driver)
        account.go_to_my_account()
        # Enter the login (non existing) and a random password
        account.input_login_username('invalid')
        account.input_login_password('pass123')
        account.click_login_button()

        #Validate the actual message is same as the expected error message.
        expected_msg="Error: The username invalid is not registered on this site. If you are unsure of your username, try your email address instead."
        account.wait_until_error_is_displayed(expected_msg)

        # TODO: Checkout what this is
        # account.get_login_form_heading()
        # error_msg=account.get_login_form_heading()
        # # msg=error_msg.text()
        # print(error_msg)
        # TODO: Try this function also to validate the error message
        # account.login_user('invalid','pass123')







