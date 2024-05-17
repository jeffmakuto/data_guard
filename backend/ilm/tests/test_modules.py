from django.test import TestCase
from django.db.utils import IntegrityError
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
    self.course.save()

    self.module1 = Module.objects.create(
      course = self.course,
      title='Module 1'
    )
  
    self.module2 = Module.objects.create(
      course = self.course,
      title='Module 2',
      description='This is module 2 description'
    )

  def test_module_creation(self):
    """
    Verifies modules can be created with or without
    descriptions
    """
    self.assertIsNotNone(self.module1.title)
    self.assertEqual(self.module1.title, 'Module 1')
    self.assertIsNone(self.module1.description)

    self.assertIsNotNone(self.module2.title)
    self.assertEqual(self.module2.title, 'Module 2')
    self.assertIsNotNone(self.module2.description)
    self.assertEqual(
      self.module2.description, 'This is module 2 description'
    )

  def test_module_foreign_key_constraint(self):
    """
    Verifies that modules are associated with existing courses.
    """
    with self.assertRaises(IntegrityError):
      Module.objects.create(title='Test Module', course_id=999)

  def test_module_update(self):
    """
    Verifies that module title and description can be updated.
    """
    self.module1.title = 'Updated Module Title'
    self.module1.description = 'Updated Module Description'
    self.module1.save()
    self.assertEqual(self.module1.title, 'Updated Module Title')
    self.assertEqual(
      self.module1.description, 'Updated Module Description'
    )

  def test_module_deletion(self):
    """
    Verifies that deleting a module doesn't affect other modules
    or the course itself.
    """
    module_id = self.module1.id
    self.module1.delete()
    self.assertFalse(Module.objects.filter(id=module_id).exists())
    self.assertTrue(Course.objects.filter(id=self.course.id).exists())

  def test_module_query(self):
    """
    Verifies querying modules by title, description, and associated course.
    """
    queried_module = Module.objects.filter(title='Module 1').first()
    self.assertEqual(queried_module, self.module1)

    queried_modules = Module.objects.filter(description__icontains='module 2')
    self.assertIn(self.module2, queried_modules)

    queried_modules = Module.objects.filter(course=self.course)
    self.assertIn(self.module1, queried_modules)
    self.assertIn(self.module2, queried_modules)
