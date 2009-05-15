#!/usr/bin/env python

import unittest, sys

if __name__ == '__main__':
    dtl = unittest.defaultTestLoader

    import test_blocks
    import test_minimal_lp
    import test_corner
    import test_tiny_lp

    ts = unittest.TestSuite([
            dtl.loadTestsFromModule(test_blocks),
            dtl.loadTestsFromModule(test_minimal_lp),
            dtl.loadTestsFromModule(test_corner),
            dtl.loadTestsFromModule(test_tiny_lp)])

    if '--verbose' in sys.argv:
        unittest.TextTestRunner(verbosity=2).run(ts)
    else:
        unittest.TextTestRunner().run(ts)
