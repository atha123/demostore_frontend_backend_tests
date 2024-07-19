import pytest
from ssqatest.src.pages.HomePage import HomePage
import  logging as log

pytestmark=[pytest.mark.feregression, pytest.mark.fesmoke]
@pytest.mark.usefixtures("init_driver")

class TestDropDown():
    """
    This is a test to check the sorting of the drop down in the main page.

    """
    @pytest.mark.lp009
    def test_home_dropdown(self):
        home= HomePage(self.driver)
        home.go_to_home_page()
        drop_down = home.get_sorting_dropdown_bottom_page()
        log.info("===== Testing the contents of the drop down! ============")
        print(f"drop_down has this: {drop_down}")
        contents = drop_down.splitlines()
        print(f"contents has this: {contents}")
        print(type(contents))
        expected_list = ['Default sorting', 'Sort by popularity', 'Sort by average rating', 'Sort by latest',
                         'Sort by price: low to high', 'Sort by price: high to low']

        # Validate first item in the drop down
        option_1=contents[0].lstrip()
        assert option_1 == expected_list[0], f"First item is not '{expected_list[0]}'"
        log.info(f"First item '{option_1}' matches the expected word: '{expected_list[0]}'")

        # Validate second item in the drop down
        option_2 = contents[1].lstrip()
        assert option_2 == expected_list[1], f"First item is not '{expected_list[1]}'"
        log.info(f"Second item '{option_2}' matches the expected word: '{expected_list[1]}'")

        # Validate third  item in the drop down
        option_3 = contents[2].lstrip()
        assert option_3 == expected_list[2], f"First item is not '{expected_list[2]}'"
        log.info(f"Third item '{option_3}' matches the expected word: '{expected_list[2]}'")

        # Validate fourth  item in the drop down
        option_4 = contents[3].lstrip()
        assert option_4 == expected_list[3], f"First item is not '{expected_list[3]}'"
        log.info(f"Fourth  item '{option_4}' matches the expected word: '{expected_list[3]}'")

        # Validate fifth item in the drop down
        option_5 = contents[4].lstrip()
        assert option_5 == expected_list[4], f"First item is not '{expected_list[4]}'"
        log.info(f"Fourth  item '{option_5}' matches the expected word: '{expected_list[4]}'")

        # Validate sixth item in the drop down
        option_6 = contents[5].lstrip()
        assert option_6 == expected_list[5], f"First item is not '{expected_list[5]}'"
        log.info(f"Fourth  item '{option_6}' matches the expected word: '{expected_list[5]}'")