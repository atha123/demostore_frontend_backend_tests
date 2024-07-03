import time
import pytest
import random
import string
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn

@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:
    """
    This test is to verify the registration of new user.

    """
    @pytest.mark.lp003
    def test_register_new_user(self):
        # Go to the My Account page directly
        account=MyAccountSignedOut(self.driver)
        account.go_to_my_account()
        account_registered= MyAccountSignedIn(self.driver)

        # Randomly create an email id
        random_email_sting_length = 10
        random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_sting_length))
        email = random_string + '@' + 'edomain.com'

        # Use this randomly created email to register
        account.input_register_email(email)
        account.input_register_password("Pass123word!@#")
        account.click_register_button()
        import pdb;pdb.set_trace()

        # Verify the registration was successful
        # account_registered.verify_user_is_signed_in()
        time.sleep(3)


        # TODO: try assertion
        # if account_registered.verify_user_is_signed_in():
        #     print("Successfully signed in")
        # else:
        #     print("Registration failed")


