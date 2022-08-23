from multiprocessing import context
import re
from django.shortcuts import redirect, render

# Create your views here.

from django.contrib.auth import authenticate, login,logout

from django.http import HttpResponse

from app.models import User, Task
from .forms import LoginForm, RegisterForm, AddTasks,WritterForm
from django.contrib import messages

def index(request):
    return render(request,'index.html')


def home(request):

    return render(request,'home.html')

# register view


def register(request):
    msg = None

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'User created successfully'
            return redirect('login_view')
        else:
            msg = 'Form invalid'
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form, 'msg': msg})

# login view


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_client:
                login(request, user)
                return redirect('client')
            elif user is not None and user.is_writter:
                login(request, user)
                return redirect('writter')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    if not request.user.is_admin:
        return redirect('login_view')
    return render(request,'admin/admin.html')

def all_client(request):

    users = User.objects.filter(is_client=True)

    context = {
        'users': users
    }

    
    return render(request,'admin/clients.html',context)

def all_writter(request):

    users = User.objects.filter(is_writter=True)

    context = {
        'users': users
    }

    return render(request,'admin/writters.html',context)

# clents view   
def client(request):
    if not request.user.is_client:
        return redirect('login_view')

    return render(request,'Client/client.html')

# all task

def all_task(request):
    # querydb

    tasks = Task.objects.all()

    context = {
        'tasks': tasks
    }
    if request.user.is_admin:
        return render(request,'admin/alltasks.html',context)
    elif request.user.is_client:
        return render(request,'Client/alltasks.html',context)
    elif request.user.is_writter:
        return render(request,'writter/alltasks.html',context)
    
    return redirect('login_view')


def writerForm(request,id):
    tasks = Task.objects.get(id=id)
    if request.method == 'POST':
        form = WritterForm(request.POST,request.FILES)
        if form.is_valid():
            status = form.cleaned_data['status']
            file = form.cleaned_data['file']

            task = Task.objects.get(id=id)
            task.status = status
            task.file = file
            task.save()
            

          
            return redirect('view',id=id)
        else:
            return HttpResponse('error')
    context = {
            
            'tasks': tasks,
            'form': WritterForm()
        }
    
        
        
    return render(request,'writter/view.html',context)

def addtasks(request):

    if request.method == 'POST':
        form = AddTasks(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['description']
            file = form.cleaned_data['file']
            client_amt = form.cleaned_data['client_amount']
            due = form.cleaned_data['due_date']

            Task(title=title,description=desc,file=file,client_amount=client_amt,due_date=due).save()


            return redirect('all_task')
        else:
            messages.error(request, 'Form invalid')

    context = {
        'form': AddTasks()
    }

    return render(request,'Client/addtasks.html',context)


# Writter view
def writter(request): 
    if not request.user.is_writter:
        return redirect('login_view')


    tasks = Task.objects.all()

    context = {
        'tasks':tasks
    }

    return render(request,'writter/writter.html',context)




# client update.

def client_task_update(request,id):
    task = Task.objects.get(id=id)
    
    
    form = AddTasks(instance=task)
    return render(request,'writter/update.html',{'form': form})



def writter_view(request,id):
    tasks = Task.objects.get(id=id)

    

    context = {
        'tasks':tasks
    }

    return render(request,'writter/view.html',context)


def admin_view(request,id):
    tasks = Task.objects.get(id=id)

    

    context = {
        'tasks':tasks
    }

    return render(request,'admin/view.html',context)

def done_task(request):
    tasks = Task.objects.all()

    context = {
        'tasks':tasks
    }
    
    return render(request,'Client/done.html',context)

# logout

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")
