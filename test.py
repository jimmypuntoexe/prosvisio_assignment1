#!/usr/bin/env python
import unittest
import check_functions

class TestCheck (unittest.TestCase):

    def test_check_id(self):

        self.assertTrue(check_functions.check_user('CF00000000000001'),msg=None)
        self.assertTrue(check_functions.check_user('CF00000000000002'),msg=None)
        self.assertFalse(check_functions.check_user('89ER4'),msg=None)
        self.assertFalse(check_functions.check_user('876'),msg=None)

    def test_check_nome(self):

        self.assertFalse(check_functions.check_nome('Ale3sandro'))
        self.assertTrue(check_functions.check_nome('Alessandro'))
        self.assertFalse(check_functions.check_nome('Gian Piero'))
    
    def test_check_cognome(self):

        self.assertFalse(check_functions.check_nome('G%Uid?i'))
        self.assertTrue(check_functions.check_nome('Bianchi'))

    def  test_check_eta(self):

        self.assertTrue(check_functions.check_eta(15))
        self.assertTrue(check_functions.check_eta(24))
        self.assertFalse(check_functions.check_eta(0))
        self.assertFalse(check_functions.check_eta(150))

    def test_check_cf(self):

        self.assertTrue(check_functions.check_codice_fiscale("CF00000000123456"))
        self.assertTrue(check_functions.check_codice_fiscale("123456789ABCDERT"))
        self.assertFalse(check_functions.check_codice_fiscale("123456789AB"))
        self.assertFalse(check_functions.check_codice_fiscale("123456789ABCDERTefef"))

    def test_check_cinema(self):
        self.assertFalse(check_functions.check_number_cinema(10))
        self.assertFalse(check_functions.check_number_cinema(0))
        self.assertTrue(check_functions.check_number_cinema(1))
        self.assertTrue(check_functions.check_number_cinema(3))

    def test_check_film(self):
        self.assertFalse(check_functions.check_number_film(7))
        self.assertTrue(check_functions.check_number_film(6))
        
if __name__ == '__main__':
    unittest.main()