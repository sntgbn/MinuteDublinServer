from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse


class TestStops(TestCase):

    """
    This class contains tests that convert measurements from one
    unit of measurement to another.
    """

    def setUp(self):
        """
        This method runs before the execution of each test case.
        """
        self.client = Client()
        self.url = reverse("stop:fetch")

    def test_fetching_train_stations_connection(self):
        """
        This method test if it is possible to fetch data from IrishRail
        """

        data = {
            "input_unit": "centimetre",
            "output_unit": "metre",
            "input_value": round(8096.894, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 80.969)
