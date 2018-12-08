from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):

    # return HttpResponse('HELLO FROM dataWorld')

    return render(request, 'dataworld/index.html')




