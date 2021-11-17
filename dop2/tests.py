from django.test import TestCase
from django.http import HttpRequest
from dop.views import home

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
            request = HttpRequest()  #1
            response = home(request)  #2
            assert response.status_code == 200