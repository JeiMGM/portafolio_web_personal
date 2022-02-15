from django.shortcuts import render, HttpResponse

# Create your views here.


def about_me(request):
    return render(request, "aboutme/aboutMe.html")
