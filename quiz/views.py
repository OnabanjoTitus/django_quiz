from django.forms import ModelForm
from django.shortcuts import render, redirect

from quiz.models import Question, Tweeter


# Create your views here.
def display(request):
    questions = Question.objects.all()
    context = {
        "questions": questions
    }
    return render(request, "quiz/home.html", context)


def submit(request):
    return render(request, "quiz/submit_page.html")


def allTweets(request):
    if request.method == 'POST':
        form = NewTweets(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all')
    tweets = Tweeter.objects.all()
    form = NewTweets()
    context = {
        "tweets": tweets,
        "form": form
    }
    return render(request, "quiz/homePage.html", context)


class NewTweets(ModelForm):
    class Meta:
        model = Tweeter
        fields = "__all__"
