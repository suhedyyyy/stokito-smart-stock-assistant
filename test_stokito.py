import tempfile
import unittest
from pathlib import Path
import main


class StokitoLogicTests(unittest.TestCase):
    def setUp(self):
        self.old_base = main.BASE_DIR
        self.old_data_dir = main.DATA_DIR
        self.old_data_file = main.DATA_FILE
        self.old_revenue_file = main.REVENUE_FILE
        self.temp = tempfile.TemporaryDirectory()
        main.BASE_DIR = Path(self.temp.name)
        main.DATA_DIR = main.BASE_DIR / "data"
        main.DATA_FILE = main.DATA_DIR / "products.json"
        main.REVENUE_FILE = main.DATA_DIR / "daily_revenue.json"
        main.products = {}
        main.daily_revenue = 0.0
        main.save_data()

    def tearDown(self):
        main.BASE_DIR = self.old_base
        main.DATA_DIR = self.old_data_dir
        main.DATA_FILE = self.old_data_file
        main.REVENUE_FILE = self.old_revenue_file
        self.temp.cleanup()

    def test_add_product(self):
        main.add_product("Notebook", 10, 50, 30, 3, 20)
        self.assertEqual(main.products["Notebook"]["stock"], 10)

    def test_duplicate_product_rejected(self):
        main.add_product("Notebook", 10, 50, 30, 3, 20)
        with self.assertRaises(ValueError):
            main.add_product("notebook", 2, 50, 30, 1, 5)

    def test_sale_updates_stock_and_revenue(self):
        main.add_product("Notebook", 10, 50, 30, 3, 20)
        product, revenue = main.sell_product("Notebook", 2)
        self.assertEqual(product["stock"], 8)
        self.assertEqual(revenue, 100)
        self.assertEqual(main.daily_revenue, 100)

    def test_cannot_sell_more_than_stock(self):
        main.add_product("Notebook", 1, 50, 30, 0, 10)
        with self.assertRaises(ValueError):
            main.sell_product("Notebook", 2)

    def test_restock_updates_stock(self):
        main.add_product("Notebook", 10, 50, 30, 3, 20)
        product, cost = main.restock_product("Notebook", 5)
        self.assertEqual(product["stock"], 15)
        self.assertEqual(cost, 150)


if __name__ == "__main__":
    unittest.main()
