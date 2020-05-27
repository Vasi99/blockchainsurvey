from django.db import models


class Surveys(models.Model):
    """
    Database model for the survey details.
    """

    owner = models.CharField(max_length=30)

    @property
    def no_of_questions(self):
        """No of questions in the survey."""
        return self.questions.count()

    @property
    def no_of_responses(self):
        """No of responses recorded for the survey."""
        all_questions = self.questions.all()
        question_1 = all_questions[0]
        return question_1.responses.count()

    @property
    def no_of_comments(self):
        """No of comments posted on the survey."""
        return self.comments.count()


class SurveyQuestions(models.Model):
    """
    Database model for storing the questions of the surveys.
    """

    question = models.TextField(max_length=1000)
    question_number = models.PositiveSmallIntegerField()
    survey = models.ForeignKey(
        Surveys, related_name="questions", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ["survey", "question_number"]


class QuestionResponses(models.Model):
    """
    Database model for storing each response to a question.
    """

    question = models.ForeignKey(
        SurveyQuestions, related_name="responses", on_delete=models.CASCADE
    )
    response = models.TextField()

    # Store sha256 of public key of the responder.
    response_by = models.CharField(max_length=64)

    class Meta:
        unique_together = ["question", "response_by"]
