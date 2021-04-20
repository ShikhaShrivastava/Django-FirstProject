from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome_django(request):

	s1="<center><h1 style='color:red'> Hello </h1></center>"

	s2="<center><h1 style='color:blue'>Welcome to my first project in Django </h1></center>"

	s3=(s1,s2)

	return HttpResponse(s3)