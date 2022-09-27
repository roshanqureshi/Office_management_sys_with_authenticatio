from multiprocessing import context
from django.shortcuts import render,redirect
from Emp_Manage_sys_app.forms import EmployeeForm
from Emp_Manage_sys_app.models import Employee
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    templates_name='index.html'
    return render(request,templates_name)

@login_required(login_url='logined')
def all_emp(request): 
    obj=Employee.objects.all()
    context={'obj':obj}
    templates_name='all_emp.html'
    return render(request,templates_name,context)

@login_required(login_url='logined')
def add_emp(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('all_emp')
    form=EmployeeForm()
    context={'form':form}
    templates_name='add_emp.html'
    return render(request,templates_name,context)

@login_required(login_url='logined')
def remove_emp(request):
    obj=Employee.objects.all()
    context={'obj':obj}
    template_name='remove_emp.html'
    return render(request,template_name,context)


@login_required(login_url='logined')
def filter_emp(request):
    if 'q' in request.GET:
        q=request.GET['q']
        # data=Data.objects.filter(first_name__icontains=q)
        if q:
            multiple_q=Q(Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(phone__icontains=q))
            data=Employee.objects.filter(multiple_q)
    else:
        data=Employee.objects.all()
    context={
        'data':data
    }
    templates_name='filter_emp.html'
    return render(request,templates_name,context)



@login_required(login_url='logined')
def delete(request,id):
    obj=Employee.objects.get(id=id)
    obj.delete()
    return redirect('all_emp')

@login_required(login_url='logined')
def update_emp(request):
    obj=Employee.objects.all()
    templates_name='update_emp.html'
    context={'obj':obj}
    return render(request,templates_name,context)

@login_required(login_url='logined')
def update(request,id):
    obj=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=obj)
        if form.is_valid:
            form.save()
            return redirect('all_emp')
    form=EmployeeForm(instance=obj)
    context={'form':form}
    templates_name='update_forms.html'
    return render(request,templates_name,context)


def sign_up(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    form=UserCreationForm()
    context={"form":form}
    templates_name="signup.html"
    return render(request,templates_name,context)

def logined(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"Invalid credential")
    templates_name="login.html"
    return render(request,templates_name)

def log_out(request):
    logout(request)
    return redirect('logined')
