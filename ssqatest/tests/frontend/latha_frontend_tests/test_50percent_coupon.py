import pytest
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.configs.MainConfigs import MainConfigs
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.Header import Header
import time

import math


pytestmark=[pytest.mark.feregression, pytest.mark.fesmoke]
@pytest.mark.usefixtures("init_driver")

class TestApply50PercentCoupon:

    @pytest.mark.lp001
    def test_50_percent_coupon(self):

        #create objects
        home_page=HomePage(self.driver)
        cart_page=CartPage(self.driver)
        header=Header(self.driver)

        #go to home page
        home_page.go_to_home_page()

        #add first item to the cart
        home_page.click_first_add_to_cart_button()
        header.wait_until_cart_item_count(1)
        time.sleep(5)

        # Now got to the cart page
        cart_page.go_to_cart_page()
        # breakpoint()

        #Before discount
        price=cart_page.get_cart_total()
        price_1=float(price)-3.0
        expected_total_after_discount = float(price_1)/2.0
        expected_compare=round(expected_total_after_discount,1)



        #apply the 50off coupon
        cart_page.apply_coupon("50OFF")
        actual_total=cart_page.get_cart_total()
        actual_total_before_convert=float(actual_total)
        actual_compare=round(actual_total_before_convert,1)
        print(f"This is the expected total {expected_compare}")
        print(f"This is the actual total {actual_compare}")

        if expected_compare != actual_compare:
            raise Exception("After applying 50% off coupon, the expected total and the actual total do not match! ")
        else:
            print("50 percent discount is now applied!")




