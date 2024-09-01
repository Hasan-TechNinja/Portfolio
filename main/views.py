from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactModelForm
from .models import Contact, Footer
from django.contrib import messages

# Create your views here.

# def HomeView(request):
#     if request.method == 'POST':
#         form = ContactModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Send an email to hasantechninja@gmail.com
#             subject = 'New message from Portfolio'
#             message = form.cleaned_data['message']
#             from_email = form.cleaned_data['email']
#             recipient_list = ['hasantechninja@gmail.com']

#             send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#             messages.success(request, 'Successfully sent your message!')
#             return redirect('home')
#     else:
#         form = ContactModelForm()

#     data = Footer.objects.all()

#     context = {
#         'form':form,
#         'data':data,
#     }

#     return render(request, 'home.html', context)

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
        
    data = Footer.objects.all()

    context = {
        'form':form,
        'data':data,
    }
    
    return render(request, 'home.html', context)
