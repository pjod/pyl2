from p1.tests import *

class TestGoscController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='gosc', action='index'))
        # Test response...
