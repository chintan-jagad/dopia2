from django.http.response import HttpResponse

def home(request):
    return HttpResponse('Hello World! Devops IA2')
