from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("you're looking at the question %s." % question_id)


def results(request, question_id):
    response = "you're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("you're  voting on the question %s." % question_id)
