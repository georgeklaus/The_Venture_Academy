from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages



# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')


def faq(request):
    return render(request, 'faq.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def team(request):
    return render(request, 'team.html')

def contact(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone_number')
        subject = request.POST.get('msg_subject')
        message = request.POST.get('message')
        agreement = request.POST.get('gridCheck')  # This will be 'on' if checked
        
        # Validate required fields
        if not all([name, email, subject, message, agreement]):
            messages.error(request, "All fields are required, including agreement to terms")
            return render(request, 'contact-us.html')
        
        # Create email content
        email_body = f"""
        New Contact Form Submission:
        
        Name: {name}
        Email: {email}
        Phone: {phone}
        Subject: {subject}
        
        Message:
        {message}
        
        Sent from: {settings.SITE_NAME}.
        """
        
        # Send email to site owner
        send_mail(
            subject=f"New Contact: {subject}",
            message=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        
        # Send confirmation to user
        confirmation_body = f"""
        Hello {name},
        
        Thank you for contacting us! We've received your message and will get back to you soon.
        
        Here's a copy of your message:
        
        Subject: {subject}
        Message: {message}
        
        Best regards,
        {settings.SITE_NAME} Team
        """
        
        send_mail(
            subject=f"Thank you for contacting {settings.SITE_NAME}",
            message=confirmation_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )
        
        messages.success(request, "Your message was sent successfully! A confirmation email has been sent to you.")
    return render(request, 'contact-us.html')
