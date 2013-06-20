from p1.tests import *

class TestUzytkownikController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='uzytkownik', action='index'))
        # Test response...
