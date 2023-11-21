from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib import auth
from django.shortcuts import render,redirect
from .forms import TodoForm
from.models import Task
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.detail import DetailView


class TaskListview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'

class TaskDetailview(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name ='task'

def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})  # Redirect to a different URL, e.g., the homepage
    # else:
        # This is a GET request, so we'll retrieve all tasks and render the template.
        # task1 = Task.objects.all()
        # return render(request, 'home.html', {'task1':task1})
                                             
def delete(request,id):
    if request.method=='POST':
        task=Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=TodoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task':task})

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect("login")
    return render(request,"login.html")


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect ("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return redirect ("register")
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)


                user.save()
                return redirect('login')
            # print("user created")
        else:
            messages.info(request,"password not matching")
            return redirect("register")

        return redirect('/')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')