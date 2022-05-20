from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_word(request):
    name = request.GET.get('name', None)
    return render(request,'hello.html', {'name': name})