from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from restaurant.views import MenuItemsView
from rest_framework.test import APIClient


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pasta", price=50, inventory=100)

    def test_getall(self):
        all_menus = Menu.objects.all()
        serialized_data = MenuSerializer(all_menus, many=True)
        self.assertIsNotNone(serialized_data)
