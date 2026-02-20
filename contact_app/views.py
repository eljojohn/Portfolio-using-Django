from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage


def contact_view(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send email to admin
        send_mail(
            subject=f"New Contact Message from {name}",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        # Send confirmation email to user
        send_mail(
            subject="Thank you for contacting",
            message="Your message has been received. I will contact you soon.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )

        return render(request, 'contact.html', {
            'success': True
        })

    return render(request, 'contact.html')
