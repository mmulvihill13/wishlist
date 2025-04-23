from django.test import TestCase
from .models import Category, Drink, Order, OrderItem
from decimal import Decimal

class ModelsTestCase(TestCase):
    
    def setUp(self):
        self.category = Category.objects.create(name="Iced")
        self.drink = Drink.objects.create(
            name="Latte",
            description="espresso with milk",
            price=Decimal("4.50"),
            category=self.category,
            in_stock=True,
            sizes=["Small", "Medium", "Large"],
            milk_options=["Whole", "Half and Half", "Almond", "Oat"],
            syrup_options=["Vanilla", "Caramel", "Mocha"],
            extra_shots=True
        )
        self.order = Order.objects.create(
            customer_name="Ana Sofia",
            customer_email="email@example.com"
        )
        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.drink,
            quantity=2,
            customizations={
                "size": "Medium",
                "milk": "Almond",
                "syrup": "Vanilla",
                "extra_shot": True
            }
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), "Iced")

    def test_drink_str(self):
        self.assertEqual(str(self.drink), "Latte")

    def test_order_item_total(self):
        expected_total = Decimal("4.50") * 2
        self.assertEqual(self.order_item.get_total(), expected_total)

    def test_drink_customization_fields(self):
        self.assertIn("Medium", self.drink.sizes)
        self.assertIn("Almond", self.drink.milk_options)
        self.assertIn("Vanilla", self.drink.syrup_options)
        self.assertTrue(self.drink.extra_shots)
