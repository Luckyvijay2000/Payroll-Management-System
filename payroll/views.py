from django.shortcuts import render, redirect
from .models import Employee, Salary


from django.shortcuts import render, redirect
from .forms import ContactForm



def home(request):

    return render(request, 'payroll/home.html')


def about(request):
    return render(request, 'payroll/about.html')





def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'payroll/employee_list.html', {'employees': employees})





def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'payroll/contact.html', {'form': form})

def success(request):
    return render(request, 'payroll/success.html')






