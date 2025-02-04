
from ssqatest.src.utilities.dbUtility import DBUtility
import random

class OrdersDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_order_lines_by_order_id(self, order_id):
        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}woocommerce_order_items 
                  WHERE order_id = {order_id};'''
        return self.db_helper.execute_select(sql)

    def get_order_items_details(self, order_item_id):
        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}woocommerce_order_itemmeta 
                  WHERE order_item_id = {order_item_id};'''
        rs_sql = self.db_helper.execute_select(sql)
        line_details = dict()
        for meta in rs_sql:
            line_details[meta['meta_key']] = meta['meta_value']

        return line_details

    def get_random_order_from_db(self, qty=1):
        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}wc_order_stats
                           ORDER BY order_id DESC LIMIT 5000;'''
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))
