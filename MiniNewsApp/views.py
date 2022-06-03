from django.shortcuts import redirect, render
from .models import Blogs
from .forms import FormBlog
from django.contrib import messages

# Create your views here.


def Home(request):
    return render(request, 'index.html')


def AddBlog(request):
    Form = FormBlog
    if request.method == 'POST':
        Form = FormBlog(request.POST)
        if Form.is_valid():
            Form.save()
            messages.success(request, 'Your Blogs has been added successfully')
            return redirect('AddBlog')
    return render(request, 'addblogs.html', {'Form': Form})


def BLogs(request):
    BLogs = Blogs.objects.all()
    return render(request, 'blogs.html', {'BLogs': BLogs})
