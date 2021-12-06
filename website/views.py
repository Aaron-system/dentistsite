from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject_something = "Subject: " + message

        # send email
        send_mail(
            name,
            subject_something,
            email,
            ['python.test.email.one@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'contact.html', {'name': name, 'email': email, 'message': message})

    else:
        return render(request, 'contact.html', {})


def portfolio(request):
    return render(request, 'portfolio.html')


def pricing(request):
    return render(request, 'pricing.html')


def services(request):
    return render(request, 'services.html')


def booking(request):
    return render(request, 'booking.html')


def thank_you(request):
    # The if statement does not work. Fix by watching the video!!!!!
    if request.method == "POST":
        name_booking = request.POST.get('name')
        email_booking = request.POST.get('email')
        date_booking = request.POST.get('date')
        time_booking = request.POST.get('time')
        appointment_for = request.POST.get('appointmentfor')

        appointment = "Name: " + name_booking + " " + "Email: " + email_booking + " " + "Date: " + date_booking + " " + "Time: " + time_booking + " " + "Appointment: " + appointment_for

        # send email #
        send_mail(
            "Appointment request",
            appointment,
            email_booking,
            ['python.test.email.one@gmail.com']
        )

        return render(request, 'thank_you.html', {
            'name': name_booking,
            'email': email_booking,
            'date': date_booking,
            'time': time_booking,
            'appointment_for': appointment_for
        })

    else:
        return render(request, 'thank_you.html', {})
