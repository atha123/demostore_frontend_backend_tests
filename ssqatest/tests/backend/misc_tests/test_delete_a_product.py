import pytest
from ssqatest.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from ssqatest.src.dao.products_dao import ProductsDAO
from ssqatest.src.utilities.genericUtilities import generate_random_string
import logging as log
pytestmark= [pytest.mark.backend]

"""
    This is a test to delete a product using API post call and then asserting it was deleted.
"""

@pytest.mark.be002
#create a payload and run a post API call to create a product
def test_create_a_product():
    payload=dict()
    payload["name"]=generate_random_string(5,"del_")
    payload["weight"]= "2"
    payload["regular_price"]= "10.00"
    # Make the API post call to create a product
    log.info("=============Creating a product ======================")

    product_create= ProductsAPIHelper().call_create_product(payload)
    log.info(f"=============Product created is : ======================")
    log.info(product_create)
    product_id= product_create["id"]
    product_name= product_create["name"]
    product_wight= product_create["weight"]
    product_price= product_create["regular_price"]
    log.info(f"The product id is: {product_id}")
    log.info(f"The price is: ${product_price}")


    # Verify that the product got created
    assert product_id, f"The product {payload['name']}never got created! This test needs to be looked into. "

    # Delete the product
    log.info(f"======== Deleting the product: '{product_name}'")
    pro_delete= ProductsAPIHelper()
    product_del= pro_delete.call_delete_product(product_id)
    # Verify that the product was deleted
    assert product_id == product_del['id'], f"Delete did not happen. Error code: {product_del['code']}"



