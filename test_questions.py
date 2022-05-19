# tests check the return type of each function in "questions module"
import unittest
import questions


class TestQuestions(unittest.TestCase):

    def test_question_one(self):

        self.assertIsInstance(questions.question_one(), type((i for i in range(1, 5))))
    

    def test_question_two(self):

        value = questions.question_one()
        self.assertIsInstance(questions.question_two(value), type(list()))


    def test_question_three(self):

        value = questions.question_one()
        self.assertIsInstance(questions.question_three(value), type(dict()))


    def test_question_four(self):
        
        value = questions.question_one()
        self.assertIsInstance(questions.question_four(value), type((i for i in range(1, 5))))




unittest.main()