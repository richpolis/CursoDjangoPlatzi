from django.urls import path 

from . import views

app_name = 'polls'

urlpatterns = [
    path("", view=views.IndexView.as_view(), name="index"), 
    path("<int:pk>/", view=views.DetailView.as_view(), name="detail"), 
    path("<int:pk>/results/", view=views.ResultView.as_view(), name="results"), 
    path("<int:question_id>/vote/", view=views.vote, name="vote"), 

]

