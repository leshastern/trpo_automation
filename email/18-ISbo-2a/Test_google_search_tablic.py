import unittest
import Decode
class Test_google(unittest.TestCase):
    def setUp(self):
        Decode.Decode_config('config.py.bak', ['SPREAD_SHEET_ID', 'CREDENTIALS_FILE'])
        Decode.Decode_files(['Example.json.bak'])

    def tearDown(self):
        Decode.Finish(['config.py', 'Example.json'])

    def test_search_tablic(self):
        from APIgoogle import search_tablic
        act=search_tablic('18-Исбо-2а','7','Лютый Максим Сергеевич')
        exp='P6'
        self.assertEqual(act, exp)

if __name__ == '__main__':
    unittest.main()
