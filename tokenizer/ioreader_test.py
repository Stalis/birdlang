import unittest
from unittest import mock

from ioreader import IOReader

TEST_DATA = 'bubble'


class TestIOReader(unittest.TestCase):

    def setUp(self):
        with mock.patch('__main__.open',
                        mock.mock_open(read_data=TEST_DATA)) as m:
            f = open('foo', 'r')
            self.reader = IOReader(f)

    def test_read(self):
        readed = self.reader.read(1)
        self.assertEqual(readed, TEST_DATA[0])


if __name__ == '__main__':
    unittest.main()
