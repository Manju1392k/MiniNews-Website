from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'addblogs.html')