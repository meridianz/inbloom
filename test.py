# -*- coding: utf-8 -*-

from __future__ import absolute_import, division
import unittest
import pyblossom
# from binascii import hexlify

class PyBloomTestCase(unittest.TestCase):

    def test_dump_ex_memview(self):
        bloom = pyblossom.Filter(entries=1000, error=0.001)
        bloom.add('test')
        self.assertTrue(bloom.contains('test'))
        self.assertFalse(bloom.contains('fail'))

        entries, error, buf = pyblossom.dump_ex(bloom)
        # print entries, error, buf, len(buf)
        self.assertEquals(entries, 1000)
        self.assertEquals(error, 0.001)

        bloom = pyblossom.Filter(entries=entries, error=error, data=buf)
        self.assertTrue(bloom.contains('test'))
        self.assertFalse(bloom.contains('fail'))

    def test_dump_ex_string(self):
        bloom = pyblossom.Filter(entries=1000, error=0.001)
        bloom.add('test')
        self.assertTrue(bloom.contains('test'))
        self.assertFalse(bloom.contains('fail'))

        entries, error, buf = pyblossom.dump_ex(bloom)
        # print entries, error, buf, len(buf)
        self.assertEquals(entries, 1000)
        self.assertEquals(error, 0.001)
        buf = buf.tobytes()

        bloom = pyblossom.Filter(entries=entries, error=error, data=buf)
        self.assertTrue(bloom.contains('test'))
        self.assertFalse(bloom.contains('fail'))

'''
class InBloomTestCase(TestCase):
    def test_functionality(self):
        bf = inbloom.Filter(20, 0.01)
	keys = ["foo", "bar", "foosdfsdfs", "fossdfsdfo", "foasdfasdfasdfasdfo", "foasdfasdfasdasdfasdfasdfasdfasdfo"]
	faux = ["goo", "gar", "gaz"]
        for k in keys:
            bf.add(k)

        for k in keys:
            assert bf.contains(k)

        for k in faux:
            assert not bf.contains(k)

        expected = '02000C0300C2246913049E040002002000017614002B0002'
        actual = hexlify(bf.buffer()).upper()
        assert expected == actual

    def test_dump_load(self):
        bf = inbloom.Filter(20, 0.01)
        bf.add('abc')
        expected = '620d006400000014000000000020001000080000000000002000100008000400'
        actual = hexlify(inbloom.dump(bf))
        assert expected == actual

        bf = inbloom.load(inbloom.dump(bf))
        actual = hexlify(inbloom.dump(bf))
        assert expected == actual

        data = inbloom.dump(bf)
        data = str([0xff, 0xff]) + data[2:]

        with self.assertRaisesRegexp(inbloom.error, "checksum mismatch"):
            inbloom.load(data)

        data = data[:4]
        with self.assertRaisesRegexp(inbloom.error, "incomplete payload"):
            inbloom.load(data)
'''

if __name__ == '__main__':
    unittest.main()
