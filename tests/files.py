import os
from tempfile import NamedTemporaryFile
from unittest import TestCase

from stdlibx.files import *


class TestFiles(TestCase):

    def test_read(self):
        with open('tempfile0', 'w') as _tempfile:
            _tempfile.write('test')
        self.assertEqual(read(_tempfile.name), 'test')
        os.remove('tempfile0')

    def test_read_yaml(self):
        with open('tempfile1', 'w') as _tempfile:
            _tempfile.write('key:\n  value')
        self.assertDictEqual(read_yaml(_tempfile.name), {'key': 'value'})
        os.remove('tempfile1')

    def test_read_json(self):
        with open('tempfile2', 'w') as _tempfile:
            _tempfile.write('{"key":"value"}')
        self.assertDictEqual(read_json(_tempfile.name), {'key': 'value'})
        os.remove('tempfile2')

    def test_read_cfg(self):
        with open('tempfile3', 'w') as _tempfile:
            _tempfile.write('[key]\n  value_1 = "value_2"')
        self.assertDictEqual(
            read_cfg(_tempfile.name), {'key': {'value_1': 'value_2'}})
        os.remove('tempfile3')

    def test_read_extension(self):
        with open('temp.csv', 'w') as _tempfile:
            _tempfile.write('test')
        self.assertEqual(read_extension(_tempfile.name), 'test')
        os.remove('temp.csv')

        with open('temp.yaml', 'w') as _tempfile:
            _tempfile.write('key:\n  value')
        self.assertDictEqual(read_extension(_tempfile.name), {'key': 'value'})
        os.remove('temp.yaml')

        with open('temp.json', 'w') as _tempfile:
            _tempfile.write('{"key":"value"}')
        self.assertDictEqual(read_json(_tempfile.name), {'key': 'value'})
        os.remove('temp.json')

        with open('temp.cfg', 'w') as _tempfile:
            _tempfile.write('[key]\n  value_1 = "value_2"')
        self.assertDictEqual(
            read_cfg(_tempfile.name), {'key': {'value_1': 'value_2'}})
        os.remove('temp.cfg')
