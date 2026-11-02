from django.shortcuts import redirect, render
from app.models import Doctor
from django.contrib import messages
from .models import ContactMessage,Newsletter,Appointment
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def contact(request):
    return render(request, 'frontend/contact.html')


def doctors_list(request):
    doctors = Doctor.objects.all()  # fetch all doctors
    return render(request, 'frontend/doctors.html', {'doc': doctors})


def blog_single(request):
    return render(request, 'frontend/blog-single.html')

def services(request):  
    return render(request, 'frontend/services.html')



def contact_submission(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')

    

        # Save to DB
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message_text,
        )

      
       
        return redirect("contact")

    return render(request, 'frontend/contact.html')




def appointment(request):

    specializations = Doctor.objects.values_list("specialization", flat=True).distinct()

    name = email = phone = message = date = ""
    selected_specialization = None
    selected_doctor = None
    doctors = Doctor.objects.none()

    if request.method == "POST":

        

        # Get all form fields
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        date = request.POST.get("date")

        selected_specialization = request.POST.get("specialization")
        

        # Load doctors when department selected
        if selected_specialization:
            doctors = Doctor.objects.filter(specialization=selected_specialization)
        
        selected_doctor = request.POST.get("doctor")

       
        if selected_doctor and date:
            Appointment.objects.create(
                name=name,
                email=email,
                phone=phone,
                doctor=Doctor.objects.get(id=selected_doctor),
                date=datetime.strptime(date, "%m/%d/%Y").date(),
                message=message
            )
            
            return redirect("appointment")

    context = {
        "specializations": specializations,
        "selected_specialization": selected_specialization,
        "doctors": doctors,
        "selected_doctor": selected_doctor,


        "name": name,
        "email": email,
        "phone": phone,
        "message": message,
        "date": date,
    }

    return render(request, "frontend/appointment.html", context)





def about(request):
    return render(request, 'frontend/about.html')


def newsletter_subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if Newsletter.objects.filter(email=email).exists():
            messages.error(request, "Email already subscribed!")
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, "Subscribed successfully!")

        return redirect(request.META.get("HTTP_REFERER")) 




