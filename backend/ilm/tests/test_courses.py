from django.test import TestCase
from ilm.models.courses import Course


class CourseModelTest(TestCase):
    """
    Test case for the course model class.
    """

    def setUp(self):
        """
        Creates sample courses with and without descriptions
        for testing.
        """
        self.course_with_description = Course.objects.create(
            title='Test Course with Description',
            description='This is a test description'
        )

        self.course_without_description = Course.objects.create(
            title='Test Course without Description'
        )

    def test_course_creation(self):
        """
        Verifies that courses can be created with and without
        descriptions.
        """
        self.assertIsNotNone(self.course_with_description.title)
        self.assertEqual(
            self.course_with_description.title, 'Test Course with Description'
        )

        # Test for description existence
        self.assertIsNotNone(self.course_with_description.description)
        self.assertEqual(
            self.course_with_description.description, 'This is a test description'
        )

        # Test for handling None description
        self.assertIsNotNone(self.course_without_description.title)
        self.assertEqual(
            self.course_without_description.title, 'Test Course without Description'
        )
        self.assertIsNone(self.course_without_description.description)

