from django.core.exceptions import ValidationError
from django.test import TestCase
from ilm.models.quiz import Quiz

class QuizModelTestCase(TestCase):
    def setUp(self):
        """
        Creating test data for Quiz.
        """
        self.quiz_data = {
            'title': 'Test Quiz',
            'description': 'This is a test quiz description'
        }

    def test_quiz_creation(self):
        """
        Test if a quiz can be created.
        """
        quiz = Quiz.objects.create(**self.quiz_data)
        self.assertEqual(quiz.title, self.quiz_data['title'])
        self.assertEqual(quiz.description, self.quiz_data['description'])

    def test_quiz_str_representation(self):
        """
        Test if the string representation of the quiz is correct.
        """
        quiz = Quiz.objects.create(**self.quiz_data)
        expected_str = f"{self.quiz_data['title']}: {self.quiz_data['description']}"
        self.assertEqual(str(quiz), expected_str)

    def test_quiz_description_optional(self):
        """
        Test if quiz creation succeeds even if description is not provided.
        """
        quiz_data_without_description = {
            'title': 'Test Quiz Without Description'
        }
        quiz = Quiz.objects.create(**quiz_data_without_description)
        self.assertEqual(quiz.title, quiz_data_without_description['title'])
        self.assertIsNone(quiz.description)

    def test_quiz_attributes_type(self):
        """
        Test if quiz attributes have the correct types.
        """
        quiz = Quiz.objects.create(**self.quiz_data)
        self.assertIsInstance(quiz.title, str)
        self.assertIsInstance(quiz.description, str)

    def test_blank_title_constraint(self):
        """
        Test blank constraint on title.
        
        Ensure that creating a quiz without a
        title raises a ValidationError.
        """
        quiz_data_without_title = {
            'description': 'Test description without title'
        }
        quiz = Quiz(**quiz_data_without_title)
        with self.assertRaises(ValidationError):
            quiz.full_clean()

    def test_quiz_description_max_length(self):
        """
        Test maximum length constraint on description.
        """
        long_description = "a" * 1001  # Exceeds the max length of TextField
        quiz_data_long_description = {
            'title': 'Quiz with Long Description',
            'description': long_description
        }
        quiz = Quiz(**quiz_data_long_description)
        with self.assertRaises(ValidationError):
            quiz.full_clean()

    def test_update_quiz(self):
        """
        Verify that you can update the attributes of an existing quiz.
        """
        quiz = Quiz.objects.create(**self.quiz_data)
        new_title = 'Updated Quiz Title'
        new_description = 'Updated Quiz Description'
        quiz.title = new_title
        quiz.description = new_description
        quiz.save()
        # Retrieve the quiz again from the database
        # to ensure changes are persisted
        updated_quiz = Quiz.objects.get(pk=quiz.pk)
        self.assertEqual(updated_quiz.title, new_title)
        self.assertEqual(updated_quiz.description, new_description)

    def test_delete_quiz(self):
        """
        Test deleting a quiz.
        """
        quiz = Quiz.objects.create(**self.quiz_data)
        quiz_id = quiz.id
        quiz.delete()
        with self.assertRaises(Quiz.DoesNotExist):
            Quiz.objects.get(pk=quiz_id)
