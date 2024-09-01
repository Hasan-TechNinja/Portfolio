from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactModelForm
from .models import Contact, Footer, Experience, About
from django.contrib import messages
from datetime import date


def HomeView(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            subject = 'New message from Portfolio'
            message_body = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            sender_name = form.cleaned_data['name']  # Assuming you have a 'name' field in your form
            recipient_list = ['hasantechninja@gmail.com']

            # Format the message to include the sender's name and email
            message = f"Sender Name: {sender_name}\nSender Email: {from_email}\n\nMessage:\n{message_body}"

            # Send the email
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            messages.success(request, 'Successfully sent your message!')
            return redirect('home')
    else:
        form = ContactModelForm()
        
    about = About.objects.last()
    data = Footer.objects.all()
    experience = Experience.objects.all() 
    today = date.today()
    year = today.year
    

    context = {
        'about':about,
        'form':form,
        'data':data,
        'experience':experience,
        'year':year
    }
    
    return render(request, 'home.html', context)
