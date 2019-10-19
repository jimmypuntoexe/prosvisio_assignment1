import unittest
import check_functions

class TestCheck (unittest.TestCase):

    def test_check_id(self):

        self.assertTrue(check_functions.check_user('CF00000000000001'),msg=None)
        self.assertTrue(check_functions.check_user('CF00000000000002'),msg=None)
        self.assertFalse(check_functions.check_user('89ER4'),msg=None)
        self.assertFalse(check_functions.check_user('876'),msg=None)

    #def test_check_nome(self):



if __name__ == '__main__':
    unittest.main()