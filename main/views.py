from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactModelForm
from .models import Contact, Footer, Experience, About, Skill, SkillImage, Projects
from django.contrib import messages
from datetime import date


def HomeView(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            subject = 'New message from Portfolio'
            message_body = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            sender_name = form.cleaned_data['name']
            recipient_list = ['hasantechninja@gmail.com']

            message = f"Sender Name: {sender_name}\nSender Email: {from_email}\n\nMessage:\n{message_body}"

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            messages.success(request, 'Successfully sent your message!')
            return redirect('home')
    else:
        form = ContactModelForm()
        
    about = About.objects.last()
    skill = Skill.objects.last()
    project = Projects.objects.all()
    SkillImages = SkillImage.objects.all()
    data = Footer.objects.all()
    today = date.today()
    year = today.year
    experiences = Experience.objects.all() 
    
    experience_details = []
    for experience in experiences:
        days = experience.calculate_experience()
        years, remaining_days = experience.calculate_experience_years()
        experience_details.append({
            'experience': experience,
            'days': days,
            'years': years,
            'remaining_days': remaining_days,
        })

    context = {
        'about':about,
        'form':form,
        'data':data,
        'skill':skill,
        'project': project,
        'skimg': SkillImages,
        'experience':experience,
        'year':year, 
        'experience_details':experience_details
    }
    
    return render(request, 'home.html', context)
