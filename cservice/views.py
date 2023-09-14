from django.shortcuts import render, redirect
from .forms import ContactForm, FeedbackForm
from .models import Service, Testimonial, Profile
from django.core.mail import send_mail

def home(request):
    profile = Profile.objects.first()
    services = Service.objects.order_by('-id')
    testimonials = Testimonial.objects.order_by('-id')
    return render(request, 'views/home.html', {'profile': profile, 'services': services, 'testimonials': testimonials})

def services(request):
    profile = Profile.objects.first()
    services = Service.objects.order_by('-id')
    return render(request, 'views/services.html', {'profile': profile, 'services': services})

def sendMessage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.first()
            form.save()  # Save the form data to the Contact model
            # Get the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            service = form.cleaned_data['service']
            # datetime_obj = datetime.strptime(form.cleaned_data['book_date'], '%Y-%m-%dT%H:%M')
            # datetime_obj = datetime_obj.replace(second=43)
            # formatted_datetime = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
            # bookDate = formatted_datetime
            bookDate = form.cleaned_data['book_date']
            # Compose the email
            subject = 'New Message from C-Service'
            message_body = f"Name: {name}\nEmail: {email}\nService: {service}\nAppointment Date: {bookDate}\n\nMessage: {message}"
            message_body2 = f"Your requested information of C-Service is:\n\nName: {name}\nEmail: {email}\nService: {service}\nAppointment Date: {bookDate}\n\nMessage: {message}"
            from_email = email # Use your own email address here
            to_email = [profile.email]  # Add recipient email addresses here
            # Send the email
            send_mail(subject, message_body, from_email, to_email)
            send_mail('Service confirmation to C-Service', message_body2, profile.email, [from_email])
            return redirect('services')  # Redirect to a success page after sending the email
    else:
        form = ContactForm()
        
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            profile = Profile.objects.first()
            # # Compose the email
            subject = 'Subscribed to C-Service'
            message_body = "You're subscribed to C-Service"
            from_email = profile.email # Use your own email address here
            to_email = [email]  # Add recipient email addresses here
            send_mail(subject, message_body, from_email, to_email)
            return redirect('home')  # Redirect to a success page after sending the email
    else:
        return redirect('home')

def feedback(request, email):
    return render(request, 'views/feedback.html', {'email': email})

def addFeedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeedbackForm()
