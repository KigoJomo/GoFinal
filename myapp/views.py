from django.shortcuts import render, redirect
from .models import Appointment, Inquiry

# Create your views here.
def index(request):
    return render(request,'index.html')

def service(request):
    return render(request,'service-details.html')

def starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def doctors(request):
    return render(request,'doctors.html')

def services(request):
    return render(request,'services.html')

def appointment(request):
    if request.method == 'POST':
        new_appointment = Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            dateTime = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message'],
        )

        new_appointment.save()
        return redirect('/appointment')
    
    else:
        return render(request, 'appointment.html')

def show(request):
    all_appointments = Appointment.objects.all()

    context = {
        'appointments': all_appointments
    }

    return render(request, 'show.html', context)

def delete(request, id):
    appointment_to_delete = Appointment.objects.get(id=id)
    appointment_to_delete.delete()

    return redirect('/show')

def contact(request):
    if request.method == 'POST':
        new_inquiry = Inquiry(
            name = request.POST['name'],
            email = request.POST['email'],
            subject= request.POST['subject'],
            message = request.POST['message'],
        )

        new_inquiry.save()
        return redirect('/contact')
    
    else:
        return render(request, 'contact.html')

