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
    self.course = Course.objects.create(
      title='Test Course'
    )

    self.module1 = Module.objects.create(
      course = self.course,
      title='Module 1'
    )
  
    self.module2 = Module.objects.create(
      course = self.course,
      title='Module 2',
      description='This is module2'
    )
