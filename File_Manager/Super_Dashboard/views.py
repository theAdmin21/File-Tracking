from django.shortcuts import render

# Create your views here.
def Super_View(request):
    return render(request, 'Super_Dashboard.html')