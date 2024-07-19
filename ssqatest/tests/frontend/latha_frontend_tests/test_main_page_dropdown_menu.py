import pytest
from ssqatest.src.pages.HomePage import HomePage
import  logging as log

pytestmark=[pytest.mark.feregression, pytest.mark.fesmoke]
@pytest.mark.usefixtures("init_driver")

class TestDropDown():
    """
    This is a test to check that the expected strings show up in the drop down menu of the main page.

    """
    @pytest.mark.lp008
    def test_home_dropdown(self):
        home= HomePage(self.driver)
        home.go_to_home_page()
        drop_down = home.get_sorting_dropdown_bottom_page()
        contents = drop_down.splitlines()
        expected_list = ['Default sorting', 'Sort by popularity', 'Sort by average rating', 'Sort by latest',
                         'Sort by price: low to high', 'Sort by price: high to low']
        log.info("===== Testing the contents of the drop down! ============")

        # THIS FAILED!
        # import pdb; pdb.set_trace()
        # expected_list= ['Default sorting', 'Sort by popularity', 'Sort by average rating','Sort by latest','Sort by price: low to high','Sort by price: high to low'  ]
        # for i in contents:
        #     i=i.lstrip()
        #     for j in expected_list:
        #         assert i == j, f"{i} no match for {j}"
        #     print("done")

        # Validate each option in the drop down list with assertions and print it out
        assert 'Default sorting' in drop_down, "The list does not have 'Default sorting'"
        log.info("=========== Contains the text:'Default sorting'")
        
        assert 'Sort by popularity' in drop_down, "The list does not have 'Sort by popularity'"
        log.info("=========== Contains the text: 'Sort by popularity'")

        assert 'Sort by average rating' in drop_down, "The list does not have ' Sort by average rating'"
        log.info("=========== Contains the text: 'Sort by average rating'")

        assert 'Sort by latest' in drop_down, "The list does not have 'Sort by latest'"
        log.info("=========== Contains the text: 'Sort by latest'")

        assert 'Sort by price: low to high' in drop_down, "The list does not have 'Sort by price: low to high is there'"
        log.info("=========== Contains the text: 'Sort by price: low to high'")

        assert 'Sort by price: high to low' in drop_down, "The list does not have 'Sort by price: high to low' is there"
        log.info ("=========== Contains the text: 'Sort by price: high to low'")
