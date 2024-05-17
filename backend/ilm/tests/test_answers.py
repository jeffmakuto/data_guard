from django.test import TestCase
from ilm.models.answers import Answer, AnswerOption
from ilm.models.quiz import Quiz
from ilm.models.questions import Question
from django.core.exceptions import ValidationError


class AnswerOptionModelTest(TestCase):
  """
  Test case for the AnswerOption model class.
  """

  def setUp(self):
    self.question = Question.objects.create(text="Test Question")

  def test_answer_option_creation(self):
    """
    Verifies that an answer option can be created.
    """
    option = AnswerOption.objects.create(
      question=self.question, text="Option A"
    )

    self.assertEqual(option.question, self.question)
    self.assertEqual(option.text, "Option A")

  def test_answer_option_creation_with_order(self):
    """
    Verifies that an answer option can be created with an order.
    """
    option = AnswerOption.objects.create(
      question=self.question, text="Option B", order=2
    )

    self.assertEqual(option.question, self.question)
    self.assertEqual(option.text, "Option B")
    self.assertEqual(option.order, 2)

  def test_answer_option_unique_text_per_question(self):
    """
    Verifies that answer options for a question must have unique text.
    """
    AnswerOption.objects.create(question=self.question, text="Option A")
    with self.assertRaises(ValidationError):
      AnswerOption.objects.create(question=self.question, text="Option A")
  

class AnswerModelTest(TestCase):
    """
    Test case for the Answer model class.
    """

    def setUp(self):
        """
        Creates a sample question and answer option for testing.
        """
        self.quiz = Quiz.objects.create(title='Test Quiz')
        self.question = Question.objects.create(text='Test question text')
        self.option1 = AnswerOption.objects.create(question=self.question, text='Option A')

    def test_answer_creation(self):
        """
        Verifies that an answer can be created with a valid option.
        """
        answer = Answer.objects.create(question=self.question, text=self.option1.text)

        self.assertEqual(answer.question, self.question)
        self.assertEqual(answer.text, self.option1.text)
        # No need to check is_correct by default (can be added if relevant)

    def test_invalid_answer_creation_empty_text(self):
        """
        Verifies that an answer cannot be created with empty text.
        """
        with self.assertRaises(ValidationError):
            Answer.objects.create(question=self.question, text='')

    def test_invalid_answer_creation_nonexistent_option(self):
        """
        Verifies that an answer cannot be created with text not
        present as an option.
        """
        with self.assertRaises(ValidationError):
            Answer.objects.create(question=self.question, text='Invalid Option')
