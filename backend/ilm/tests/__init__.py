import unittest


def suite():
    """
    Discovers all test cases within the current
    directory and subdirectories.
    
    Returns a unittest.TestSuite object containing
    the discovered tests.
    """
    return unittest.TestLoader().discover('.', pattern="test*.py")
