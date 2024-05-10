from django.test import TestCase
from ilm.models.courses import Course
from ilm.models.modules import Module


class ModuleModelTest(TestCase):
  """
  Test case for the modules model class
  """
  def setUp(self):
    """
    Create sample course and module for testing
    """
