from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = { 'boldtext': "Some Bold Text." }
    return render(request, 'pango/index.html', context_dict)
    # return HttpResponse("Pango says hey there world!<br/><a href='/pango/about/'>About Us</a>")

def about(request):
    return HttpResponse("This is the About us Page<br/><a href='/pango/'>Index</a>")
