import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import app as tested_app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get_hello_endpoint(self):
        r = self.app.get('/')
        self.assertEqual(r.data, b'Hello World!')


    def test_sq_rect_success(self):
        r = self.app.get('/calc_rect?a=4&b=3')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'12.0')
    
    def test_sq_triangle_success(self):
        r = self.app.get('/calc_triangle?a=4&b=3&c=5')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'6.0')

    def test_sq_triangle_inequality_error(self):
        r = self.app.get('/calc_triangle?a=4&b=3&c=8')
        self.assertEqual(r.data, 'такого треугольника не существует'.encode())



if __name__ == '__main__':
    unittest.main()