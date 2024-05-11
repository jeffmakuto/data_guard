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

    def test_question_creation(self):
        """
        Verifies that a question can be created.
        """
        question = Question.objects.create(
            quiz=self.quiz,
            text='Test question text',
            correct_answer='Option A',
            options=['Option A', 'Option B', 'Option C']
        )
        self.assertEqual(question.quiz, self.quiz)
        self.assertEqual(question.text, 'Test question text')
        self.assertEqual(question.correct_answer, 'Option A')
        self.assertListEqual(question.options, ['Option A', 'Option B', 'Option C'])
