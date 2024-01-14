
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Author
from django.shortcuts import render, redirect  
from .forms import EmployeeForm  
from .models import Employee 


def hello_world(request):
    return HttpResponse("Hello, World!")

def anime_waifu(request):
    return HttpResponse("Raphtalia")
def current_datetime(request):
    now = datetime.now()
    return render(request, 'hello_app/current_datetime.html', {'now': now})
from datetime import datetime, timedelta

def time_after_10_hours(request, hours):
    try:
        hours = int(hours)
    except ValueError:
        return HttpResponse("Invalid input. Please provide a valid integer.")

    current_time = datetime.now()
    time_after_10_hours = current_time + timedelta(hours=hours)

    return HttpResponse(f"Current Time: {current_time}<br>Time After {hours} Hours: {time_after_10_hours}")

def hello(request):
    context = {
        'name': 'Deversh',
        'age': 21,
    }
    return render(request, 'hello_app/hello.html', context)



def book_list(request):
    authors = Author.objects.all()
    return render(request, 'hello_app/book_list.html', {'authors': authors})



 
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'hello_app/index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"hello_app/show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'hello_app/edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'hello_app/edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  




