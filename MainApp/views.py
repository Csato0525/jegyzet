from django.shortcuts import render

# Create your views here.

def VIEW(request):
	return render(request, "index.html", {})