from django.test import TestCase
from django.db.utils import IntegrityError
from surveys import models
from surveys.tests.mock_data import *


def createSurvey(owner):
    return models.Surveys.objects.create(owner=owner)


def createQuestion(question, q_no, survey):
    return models.SurveyQuestions.objects.create(
        question=question, question_number=q_no, survey=survey
    )


def createResponse(question, response, responder):
    return models.QuestionResponses.objects.create(
        question=question, response=response, response_by=responder
    )


class TestSurveysModel(TestCase):
    """
    Unit tests for the Surveys database model.
    """

    def setUp(self) -> None:
        self.survey_1 = createSurvey(user_1)
        self.survey_2 = createSurvey(user_2)
        question_1 = createQuestion(mock_question_1, 1, self.survey_1)
        question_2 = createQuestion(mock_question_2, 2, self.survey_1)
        response1 = createResponse(question_1, mock_response_1, unknown_user_1)
        response2 = createResponse(question_2, mock_response_2, unknown_user_1)
        response3 = createResponse(question_1, mock_response_1, unknown_user_2)
        response4 = createResponse(question_2, mock_response_2, unknown_user_2)

    def test_survey_owner(self):
        owner = self.survey_1.owner
        self.assertEqual(user_1, owner)

    def test_survey_questions(self):
        questions = self.survey_1.questions.all()
        self.assertEqual(questions[0].question, mock_question_1)
        self.assertEqual(questions[1].question, mock_question_2)

    def test_no_of_questions(self):
        no_of_questions = self.survey_1.no_of_questions
        self.assertEqual(no_of_questions, 2)

    def test_no_of_responses(self):
        n_responses = self.survey_1.no_of_responses
        self.assertEqual(n_responses, 2)


class TestSurveyQuestionsModel(TestCase):
    """
    Unit tests for the SurveyQuestions database model.
    """

    def setUp(self) -> None:
        self.survey_1 = createSurvey(user_1)
        self.question_1 = createQuestion(mock_question_1, 1, self.survey_1)

    def test_question(self):
        question = self.question_1.question
        self.assertEqual(question, mock_question_1)

    def test_question_owner(self):
        owner = self.question_1.survey.owner
        self.assertEqual(user_1, owner)

    def test_unique_question_number(self):
        with self.assertRaises(IntegrityError):
            test_question = createQuestion(mock_question_2, 1, self.survey_1)


class TestQuestionResponsesModel(TestCase):
    """
    Unit tests for QuestionResponses database model.
    """

    def setUp(self) -> None:
        survey = createSurvey(user_1)
        self.question = createQuestion(mock_question_2, 1, survey)
        self.response = createResponse(self.question, mock_response_1, unknown_user_1)

    def test_response(self):
        response = self.response.response
        self.assertEqual(response, mock_response_1)

    def test_one_response_per_user(self):
        with self.assertRaises(IntegrityError):
            duplicate_response = createResponse(self.question, mock_response_2, unknown_user_1)
