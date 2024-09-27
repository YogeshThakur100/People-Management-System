from django.shortcuts import render , HttpResponse
from .models import Employee , Department , Role
from datetime import datetime
from django.db.models import Q

# Create your views here.
def hello(request): 
    return render(request , 'index.html')

def All_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps    
    }
    return render(request , 'All_emp.html' , context)

def Add_emp(request):
    if request.method == 'POST':
        emp_first_name = request.POST['emp_first_name']
        emp_last_name = request.POST['emp_last_name']
        dept = int(request.POST['dept'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role']) 
        phone = int(request.POST['phone'])
        new_emp = Employee(emp_first_name = emp_first_name , emp_last_name = emp_last_name , dept_id = dept , salary = salary , 
        bonus = bonus , role_id = role , phone = phone , hire_date = datetime.now())
        new_emp.save()
        return render(request , 'index.html')
    elif request.method == 'GET':
        return render(request , 'Add_emp.html')
    else:
        return HttpResponse("An unhandeled exception occured , Employee has not been added")

def Remove_emp(request , emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return render(request , 'Index.html')
        except:
            return HttpResponse("Please enter a valid employee id")
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request , 'Remove_emp.html' , context)

def Filter_emp(request):
    if request.method == 'POST':
        name = request.POST['emp_first_name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(emp_first_name__icontains = name) | Q(emp_last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__position__icontains = role)

        context = {
            'emps' : emps
        }
        return render(request , 'All_emp.html'  , context) 
    
    elif request.method == 'GET':
        return render(request , 'Filter_emp.html')
    
    else:
        return HttpResponse("An unhandled exception occured")
