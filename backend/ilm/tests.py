from django.test import TestCase
from models.courses import Course

class CourseModelTest(TestCase):
    """
    Test case for the course model class.
    """

    def setUp(self):
        """
        Method to initialize test features.
        """
        self.course = Course.objects.create(
            title='Test course',
            description='Test description'
        )

    def test_course_creation(self):
        """
        Test to know whether a course has been created.
        """
        self.assertEqual(
