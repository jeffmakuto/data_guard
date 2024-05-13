from django.test import TestCase
from ilm.models.quiz import Quiz


class QuizModelTest(TestCase):
    """
    Test case for the Quiz model class.
    """
    def setUp(self):
        """
        Sets up the test environment by creating
        a quiz instance.
        """
        self.quiz = Quiz.objects.create(
            title='Test Quiz',
            description='This is a test quiz'
        )

    def test_quiz_creation(self):
        """
        Verifies that a quiz can be created.
        """
        self.assertEqual(self.quiz.title, 'Test Quiz')
        self.assertEqual(
            self.quiz.description, 'This is a test quiz'
        )
