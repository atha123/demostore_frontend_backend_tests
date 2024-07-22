import pytest
from ssqatest.src.pages.HomePage import HomePage
import  logging as logger

pytestmark=[pytest.mark.feregression, pytest.mark.fesmoke]
@pytest.mark.usefixtures("init_driver")

class TestDropDown():
    """
    This is a test to check that the expected strings show up in the drop down menu of the main page using a for loop.

    """
    @pytest.mark.lp010
    def test_home_dropdown(self):
        home= HomePage(self.driver)
        home.go_to_home_page()
        drop_down = home.get_sorting_dropdown_bottom_page()
        print(drop_down)
        contents = drop_down.splitlines()
        length_contents = len(contents)
        logger.info("===== Testing the contents of the drop down! ============")
        expected_list = ['     Default sorting', '     Sort by popularity', '     Sort by average rating', '     Sort by latest',
                         '     Sort by price: low to high', '     Sort by price: high to low', '   ']

        logger.info(f"======== The UI has {length_contents} items in the drop down menu. ======== ")

        # Validation for the contents of the drop down menu
        for i in range(length_contents):
            assert contents[i] == expected_list[i], "No match. Something is wrong! "
            logger.info(f"Actual: '{contents[i]}' matched with Expected: '{expected_list[i]}'")
        logger.info("This Test has PASSED! ")



