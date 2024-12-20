from django.shortcuts import render, redirect
from .models import Appointment, Inquiry, User
from .forms import AppointmentForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        if User.objects.filter(
            username=request.POST["username"], password=request.POST["password"]
        ).exists():
            return render(request, "index.html")
        else:
            return render(request, "login.html")
    else:
        return render(request, "login.html")


def service(request):
    return render(request, "service-details.html")


def starter(request):
    return render(request, "starter-page.html")


def about(request):
    return render(request, "about.html")


def doctors(request):
    return render(request, "doctors.html")


def services(request):
    return render(request, "services.html")


def appointment(request):
    if request.method == "POST":
        new_appointment = Appointment(
            name=request.POST["name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            date=request.POST["date"],
            department=request.POST["department"],
            doctor=request.POST["doctor"],
            message=request.POST["message"],
        )

        new_appointment.save()
        return redirect("/appointment")

    else:
        return render(request, "appointment.html")


def show(request):
    all_appointments = Appointment.objects.all()

    context = {"appointments": all_appointments}

    return render(request, "show.html", context)


def delete(request, id):
    appointment_to_delete = Appointment.objects.get(id=id)
    appointment_to_delete.delete()

    return redirect("/show")


def contact(request):
    if request.method == "POST":
        new_inquiry = Inquiry(
            name=request.POST["name"],
            email=request.POST["email"],
            subject=request.POST["subject"],
            message=request.POST["message"],
        )

        new_inquiry.save()
        return redirect("/contact")

    else:
        return render(request, "contact.html")


def edit(request, id):
    appointment_to_edit = Appointment.objects.get(id=id)

    context = {"appointment": appointment_to_edit}

    return render(request, "edit.html", context)

def update(request, id):
    updateinfo = Appointment.objects.get(id=id)
    form = AppointmentForm(request.POST, instance=updateinfo)

    if form.is_valid():
        form.save()
        return redirect("/show")
    else:
        return render(request, "edit.html", {"appointment": updateinfo})


def register(request):
    if request.method == "POST":
        new_user = User(
            name = request.POST["name"],
            username = request.POST["username"],
            password = request.POST["password"],
        )

        new_user.save()
        return redirect("/login")

    else:
        return render(request, "register.html")

def login(request):
    return render(request, "login.html")