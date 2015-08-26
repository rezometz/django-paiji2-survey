from django.conf.urls import url  # , patterns

from .views import SurveyVoteView, SurveyListView


urlpatterns = [
    url(r'^vote$', SurveyVoteView.as_view(), name="survey-vote"),
    url(r'^archives$', SurveyListView.as_view(), name="survey-list"),
]
