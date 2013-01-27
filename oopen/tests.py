from oopen import OOpen

import unittest


class TestOOpen(unittest.TestCase):

    def setUp(self):
        self.file = OOpen('test.txt')
        pass

    def tearDown(self):
        pass

    def TestExample(self):
        pass

    # TestCase methods:
    # assertEqual(a, b)   a == b
    # assertNotEqual(a, b)    a != b
    # assertTrue(x)   bool(x) is True
    # assertFalse(x)  bool(x) is False
    # assertIs(a, b)  a is b  2.7
    # assertIsNot(a, b)   a is not b  2.7
    # assertIsNone(x) x is None   2.7
    # assertIsNotNone(x)  x is not None   2.7
    # assertIn(a, b)  a in b  2.7
    # assertNotIn(a, b)   a not in b  2.7
    # assertIsInstance(a, b)  isinstance(a, b)    2.7
    # assertNotIsInstance(a, b)   not isinstance(a, b)    2.
    # assertAlmostEqual(first, second, places=7, msg=None, delta=None)
    # assertNotAlmostEqual(first, second, places=7, msg=None, delta=None)

    # assertRaises(exc, fun, *args, **kwds)   fun(*args, **kwds) raises exc
    # assertRaisesRegexp(exc, re, fun, *args, **kwds) fun(*args, **kwds) raises exc and the message matches re    2.7

    # Decorators:
    # unittest.skip(reason)
    #     Unconditionally skip the decorated test. reason
    #     should describe why the test is being skipped.

    # unittest.skipIf(condition, reason)
    #     Skip the deco  rated test if condition is true.

    # unittest.skipUnless(condition, reason)
    #     Skip the decorated test unless condition is true.

    # unittest.expectedFailure()
    #     Mark the test as an expected failure. If the
    #     test fails when run, the test is not counted as a failure.

if __name__ == '__main__':
    unittest.main()
