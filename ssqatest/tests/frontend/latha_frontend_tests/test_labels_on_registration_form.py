import pytest
import logging as log
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut

pytestmark=[pytest.mark.feregression, pytest.mark.fesmoke]
@pytest.mark.usefixtures("init_driver")
@pytest.mark.lp004
class TestForLabelsOnRegistrationForm():
    """
    This is a test to ensure that all the labels on the registration page are showing up correctly.
    """
    @pytest.mark.lp005
    def test_for_heading_label(self):
        form= MyAccountSignedOut(self.driver)
        # This is to ensure that the label for heading is "Register"
        # Go to the page 'My Account'
        form.go_to_my_account()

        # Get the exact string in the label from the UI
        label_heading=form.get_register_form_heading()

        # Validate to ensure that the label on the UI matches the expected label= "Register"
        assert label_heading == 'Register', f"The form has an incorrect label: '{label_heading}'"
        log.info(f"Test 1: The actual label on the UI for the form is :'{label_heading}' which matches the expected label: 'Register'")

    @pytest.mark.lp006
    def test_for_email_field(self):
        # Validate to ensure that the label on the UI matches the expected label= "Email address *"
        email_form= MyAccountSignedOut(self.driver)
        email_form.go_to_my_account()
        email_label=email_form.get_register_form_email_label()
        assert  email_label == "Email address *", f"The form has an incorrect label: '{email_label}'"
        log.info(f"Test 2: The actual label on the UI is for the Email field is '{email_label}' which matches the expected label 'Email address *'")

    @pytest.mark.lp007
    def test_for_password_field(self):
        #Validate to ensure that the label on the UI matches the expected label= "Password"
        email_passw=MyAccountSignedOut(self.driver)
        email_passw.go_to_my_account()
        passw_label=email_passw.get_register_form_password_label()
        log.info(passw_label)
        assert passw_label == 'Password *', "Incorrect Password"
        log.info(f"Test 3: The actual label on the UI is for the Password field is '{passw_label}' which matches the expected label 'Password *'")