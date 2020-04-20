import unittest
from base_WorkWithLetters import SendJSONForCheck

class TestSendJSONForCheck(unittest.TestCase):
    def setUp(self):
        print('l')

    def test_SendJSONForCheck(self):
        self.assertEqual('l', 'l')


if __name__ == "__main__":
    unittest.main()
