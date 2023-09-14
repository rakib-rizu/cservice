from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from .forms import RegistrationForm, LoginForm, ServiceForm, TestimonialForm, ProfileForm, ContactForm, FeedbackForm
from .models import Service, Testimonial, Profile, Contact
from django.core.mail import send_mail
from datetime import datetime

def notAuthenticated(user):
    return not user.is_authenticated

def home(request):
    profile = Profile.objects.first()
    services = Service.objects.order_by('-id')
    testimonials = Testimonial.objects.order_by('-id')
    return render(request, 'views/home.html', {'profile': profile, 'services': services, 'testimonials': testimonials})

def services(request):
    profile = Profile.objects.first()
    services = Service.objects.order_by('-id')
    return render(request, 'views/services.html', {'profile': profile, 'services': services})

@user_passes_test(notAuthenticated, login_url=reverse_lazy('home'))
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'views/register.html', {'form': form})

@user_passes_test(notAuthenticated, login_url=reverse_lazy('home'))
def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'views/login.html', {'form': form})

def logoutView(request):
    logout(request)
    return redirect('login')

def addService(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ServiceForm()
        
def updateService(request, serviceId):
    service = get_object_or_404(Service, id=serviceId)

    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ServiceForm(instance=service)
        
def deleteService(request, serviceId):
    if request.method == 'POST':
        service = get_object_or_404(Service, id=serviceId)
        service.delete()
        return redirect('dashboard')
    
def addTestimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TestimonialForm()
        
def updateTestimonial(request, testimonialId):
    testimonial = get_object_or_404(Testimonial, id=testimonialId)

    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TestimonialForm(instance=testimonial)
        
def deleteTestimonial(request, testimonialId):
    if request.method == 'POST':
        testimonial = get_object_or_404(Testimonial, id=testimonialId)
        testimonial.delete()
        return redirect('dashboard')

def dashboard(request):
    profile = Profile.objects.first()
    services = Service.objects.order_by('-id')
    testimonials = Testimonial.objects.order_by('-id')
    contacts = Contact.objects.order_by('-id')
    return render(request, 'views/dashboard.html', {'profile': profile, 'services': services, 'testimonials': testimonials, 'contacts': contacts})

def updateInformation(request):
    profile, created = Profile.objects.get_or_create(pk=1)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)

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
