import unittest
from src.HelloWorld import HelloWorld


class HelloWorldTests(unittest.TestCase):
    def test_no_name(self):
        h = HelloWorld()
        self.assertEqual(str(h), 'Hello World!')

    def test_name(self):
        h = HelloWorld('Akx')
        self.assertEqual(str(h), 'Hello Akx!')


if __name__ == '__main__':
    unittest.main()
