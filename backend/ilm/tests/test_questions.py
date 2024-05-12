from django.test TestCase
from ilm.models.questions import Question
from ilm.models.answers import Answer
from ilm.models.quiz import Quiz


class QuestionModelTest(TestCase):
    """
    Test case for the Question model class.
    """
    def setUp(self):
        """
        Creates a sample quiz for testing.
        """
        self.quiz = Quiz.objects.create(
            title='Test Quiz'
        )

        question = Question.objects.create(
            quiz=self.quiz,
            text='Test question text',
            correct_answer='Option A',
            options=['Option A', 'Option B', 'Option C']
        )

    def test_question_creation(self):
        """
        Verifies that a question can be created.
        """
        self.assertEqual(question.quiz, self.quiz)
        self.assertEqual(question.text, 'Test question text')
        self.assertEqual(question.correct_answer, 'Option A')
        self.assertListEqual(
            question.options, ['Option A', 'Option B', 'Option C']
        )

    def test_question_answers_relationship(self):
        """
        Verifies that answers can be associated with a question.
        """
        answer1 = Answer.objects.create(
            question=self.question, text='Option A', is_correct=True
        )
        answer2 = Answer.objects.create(
            question=self.question, text='Option B', is_correct=False
        )

        self.assertIn(answer1, self.question.answers.all())
        self.assertIn(answer2, self.question.answers.all())
