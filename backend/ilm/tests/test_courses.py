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

    def test_course_unique_constraint(self):
        """
        Verifies the course titles are unique
        """
        with self.assertRaises(Exception):
            Course.objects.create(title='Test Course with description')

    def test_course_update(self):
        """
        Verifies course and title can be updated
        """
        self.course_with_description.title = 'Updated Title'
        self.course_with_description.description = 'Updated Description'
        self.course_with_description.save()
        self.assertEqual(
            self.course_with_description.title, 'Updated Title'
        )
        self.assertEqual(
            self.course_with_description.description, 'Updated Description'
        )

    def test_course_deletion(self):
        """
        Verifies that a deleted course also deletes
        associated modules
        """
        course_id = self.course_with_description.id
        self.course_with_description.delete()
        self.assertFalse(
            Module.objects.filter(course_id=course_id).exists()
        )

    def test_course_query(self):
        """
        Verifies querying courses by title and description.
        """
        queried_course = Course.objects.filter(title='Test Course with Description').first()
        self.assertEqual(queried_course, self.course_with_description)

        queried_courses = Course.objects.filter(description__icontains='test')
        self.assertIn(self.course_with_description, queried_courses)
