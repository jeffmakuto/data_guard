import unittest

def suite():
    """Find all test cases within this directory and sub-dirs
    Return a unittest.TestSuite object containing the discovered tests
    """
    return unittest.TestLoader().discover('.', pattern="test_*.py")