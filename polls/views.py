from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic 
from .models import Question, Choice 
# Create your views here.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "lastest_question_list"

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by('-pub_date')[:5]


# def index(request):
#     questions = get_list_or_404(Question)
#     return render(request, "polls/index.html", context={
#         'lastest_question_list': questions
#     })


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    context_object_name = "question"


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", context={
#         "question": question
#     })


class ResultView(DetailView):
    template_name = "polls/results.html"


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", context={
#         "question": question
#     })

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", context={
            "question": question, 
            "error_message": "No elegiste une respuesta"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))