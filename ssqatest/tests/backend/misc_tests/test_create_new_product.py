import pytest
from ssqatest.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from ssqatest.src.dao.products_dao import ProductsDAO
from ssqatest.src.utilities.genericUtilities import generate_random_string
import logging as logger
pytestmark = [pytest.mark.backend]

"""
    This is a test to create a product using API post call and then asserting it was created.
"""

@pytest.mark.be001

def test_create_a_product():
    # create a payload and run a post API call to create a product
    payload = dict()
    payload["name"] = generate_random_string(5,"lp")
    payload["weight"] = "2"
    payload["regular_price"] = "10.00"

    # Make the API post call to create a product
    product_create = ProductsAPIHelper().call_create_product(payload)
    product_id =product_create["id"]
    product_name = product_create["name"]
    product_wight = product_create["weight"]
    product_price = product_create["regular_price"]
    logger.info("===================================")
    logger.info(f"The product id is: {product_id}")
    logger.info(f"The price is: ${product_price}")


    # Verify that the product got created
    assert product_id, f"The product {payload['name']} never got created! "
    logger.info(f"Product '{product_name}' was created with an id {product_id}")

    #Verify the name, price and weight are correct in the response
    assert product_name == payload["name"] , f"The name of the product is not  {payload['name']}!! "
    logger.info(f"Product name matches. Expected name '{payload['name']}' matches the Actual name'{product_name}'")
    assert product_price == payload["regular_price"] , f"The price of the product is not {payload['regular_price']}!! "
    logger.info(f"Price matches. Expected price: ${payload['regular_price']} matches the Actual price ${product_price}")
    assert product_wight == payload["weight"] , f"The weight of the product is not {payload['weight']}!! "
    logger.info(f"Weight matches. Expected weight: {payload['weight']} lbs matches the Actual weight {product_wight} lbs")



    # Fetch the product just created from the DB
    product_db=ProductsDAO().get_product_by_id(product_id)

    # Verify that the product id and the product name matches with the id and name sent in the payload during the Post API call
    assert product_db[0]["ID"] == product_id, "Product ids do not match"
    logger.info(f"Expected product id: {product_id} matches Actual product id:{product_db[0]['ID']} " \
             f"Expected product name: '{product_name}' matches Actual product id:{product_db[0]['post_title']}")

    assert product_db[0]["post_title"] == product_name, "Product name do not match"
    logger.info(f"Expected product name: {product_name} matches Actual product id:{product_db[0]['post_title']} ")


