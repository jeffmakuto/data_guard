from django.core.exceptions import ValidationError
from django.test import TestCase
from ilm.models import Course, Module


class ModuleModelTestCase(TestCase):
    def setUp(self):
        """
        Creating test data for Course and Module.
        """
        self.course = Course.objects.create(
            title='Test Course',
            description='This is a test course'
        )
        self.module_data = {
            'course': self.course,
            'title': 'Test Module',
            'description': 'This is a test module'
        }

    def test_module_creation(self):
        """
        Test if a module can be created.
        """
        module = Module.objects.create(**self.module_data)
        self.assertEqual(module.title, self.module_data['title'])
        self.assertEqual(module.description, self.module_data['description'])
        self.assertEqual(module.course, self.course)

    def test_module_str_representation(self):
        """
        Test if the string representation of the module is correct.
        """
        module = Module.objects.create(**self.module_data)
        module_title = self.module_data['title']
        course_title = self.course.title
        expected_str = f"{module_title} (Course: {course_title})"

        self.assertEqual(str(module), expected_str)

    def test_module_description_optional(self):
        """
        Test if module creation succeeds even if description is not provided.
        """
        module_data_without_description = {
            'course': self.course,
            'title': 'Test Module Without Description'
        }
        module = Module.objects.create(**module_data_without_description)
        self.assertEqual(
            module.title, module_data_without_description['title']
        )
        self.assertIsNone(module.description)

    def test_module_attributes_type(self):
        """
        Test if module attributes have the correct types.
        """
        module = Module.objects.create(**self.module_data)
        self.assertIsInstance(module.title, str)
        self.assertIsInstance(module.description, str)
        self.assertIsInstance(module.course, Course)

    def test_blank_title_constraint(self):
        """
        Test blank constraint on title.

        Ensure that creating a module without a
        title raises a ValidationError.
        """
        module_data_without_title = {
            'course': self.course,
            'description': 'Test description without title'
        }
        module = Module(**module_data_without_title)
        with self.assertRaises(ValidationError):
            module.full_clean()

    def test_module_description_max_length(self):
        """
        Test maximum length constraint on description.
        """
        long_description = "a" * 1001  # Exceeds the max length of TextField
        module_data_long_description = {
            'course': self.course,
            'title': 'Module with Long Description',
            'description': long_description
        }
        module = Module(**module_data_long_description)
        with self.assertRaises(ValidationError):
            module.full_clean()

    def test_update_module(self):
        """
        Verify that you can update the attributes of an existing module.
        """
        module = Module.objects.create(**self.module_data)
        new_title = 'New Module Title'
        new_description = 'New Module Description'
        module.title = new_title
        module.description = new_description
        module.save()
        # Retrieve the module again from the database
        # to ensure changes are persisted
        updated_module = Module.objects.get(pk=module.pk)
        self.assertEqual(updated_module.title, new_title)
        self.assertEqual(updated_module.description, new_description)

    def test_delete_module(self):
        """
        Test deleting a module.
        """
        module = Module.objects.create(**self.module_data)
        module_id = module.id
        module.delete()
        with self.assertRaises(Module.DoesNotExist):
            Module.objects.get(pk=module_id)
