from decouple import config
from django.test import SimpleTestCase


class TestProductsView(SimpleTestCase):
    def setUp(self) -> None:
        # self.home_url = reverse("home")
        self.username = config("DJANGO_ADMIN_USER")
        self.password = config("DJANGO_ADMIN_PASSWORD")

    def setup_databases(self, **kwargs):
        """Override the database creation defined in parent class"""
        pass

    def teardown_databases(self, old_config, **kwargs):
        """Override the database teardown defined in parent class"""
        pass

    def test_ws(self):
        ...
