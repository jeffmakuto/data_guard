from django.core.exceptions import ValidationError
from django.test import TestCase
from ilm.models import Course


class CourseModelTestCase(TestCase):
    def setUp(self):
        """
        Creating a dictionary with test data to use in
        tests, ensuring consistency and reducing redundancy.
        """
        self.course_data = {
            'title': 'Test Course',
            'description': 'This is a test course'
        }

    def test_course_creation(self):
        """
        Test if a course can be created.
        """
        course = Course.objects.create(**self.course_data)
        self.assertEqual(course.title, self.course_data['title'])
        self.assertEqual(course.description, self.course_data['description'])

    def test_course_str_representation(self):
        """
        Test if the string representation of the course is correct.
        """
        course = Course.objects.create(**self.course_data)
        title = self.course_data['title']
        description = self.course_data['description']
        expected_str = f"{title}: {description}"
        self.assertEqual(str(course), expected_str)

    def test_course_description_optional(self):
        """
        Test if course creation succeeds even if description is not provided.
        """
        course_data_without_description = {
            'title': 'Test Course Without Description'
        }
        course = Course.objects.create(**course_data_without_description)
        self.assertEqual(
            course.title, course_data_without_description['title']
        )
        self.assertIsNone(course.description)

    def test_course_attributes_type(self):
        """
        Test if course attributes have the correct types.
        """
        course = Course.objects.create(**self.course_data)
        self.assertIsInstance(course.title, str)
        self.assertIsInstance(course.description, str)

    def test_unique_title_constraint(self):
        """
        Test uniqueness constraint on title.

        Ensure that creating a course with a title
        that already exists raises a ValidationError.
        """
        Course.objects.create(**self.course_data)
        duplicate_course = Course(**self.course_data)
        with self.assertRaises(ValidationError):
            duplicate_course.full_clean()

    def test_blank_title_constraint(self):
        """
        Test blank constraint on title.

        Ensure that creating a course without a
        title raises a ValidationError.
        """
        course_data_without_title = {
            'description': 'Test description without title'
        }
        course = Course(**course_data_without_title)
        with self.assertRaises(ValidationError):
            course.full_clean()

    def test_update_course(self):
        """
        Verify that you can update the attributes of an existing course.
        """
        course = Course.objects.create(**self.course_data)
        new_title = 'New Title'
        new_description = 'New Description'
        course.title = new_title
        course.description = new_description
        course.save()
        # Retrieve the course again from the database
        # to ensure changes are persisted
        updated_course = Course.objects.get(pk=course.pk)
        self.assertEqual(updated_course.title, new_title)
        self.assertEqual(updated_course.description, new_description)

    def test_delete_course(self):
        """
        Test deleting a course.
        """
        course = Course.objects.create(**self.course_data)
        course_id = course.id
        course.delete()
        with self.assertRaises(Course.DoesNotExist):
            Course.objects.get(pk=course_id)

    def test_course_description_max_length(self):
        """
        Test maximum length constraint on description.
        """
        long_description = "a" * 1001  # Exceeds the max length of TextField
        course_data_long_description = {
            'title': 'Course with Long Description',
            'description': long_description
        }
        course = Course(**course_data_long_description)
        with self.assertRaises(ValidationError):
            course.full_clean()
