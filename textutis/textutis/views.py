#I have Created this file Anuraj
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request, 'index.html')
    #return HttpResponse("Home")

def about(request):
    
    return HttpResponse("Anuraj")

def remove_punc(request):
    djtext = request.GET.get('text', 'default')
    print(djtext)
    return HttpResponse("remove punc")

def cap_first(request):
    return HttpResponse("cap first")

def new_line_remove(request):
    return HttpResponse("new line remove")

def space_remove(request):
    return HttpResponse("space remove")

def char_count(request):
    return HttpResponse("char count")