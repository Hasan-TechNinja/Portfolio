from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactModelForm
from .models import Contact, SocialLink, Experience, About, SkillImage, Projects, PROJECT_CATEGORIES
from django.contrib import messages
from datetime import date


def HomeView(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
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

    about = About.objects.filter(status=True)
    project = Projects.objects.filter(status=True)
    skill_images = SkillImage.objects.filter(status=True)
    social_links = SocialLink.objects.filter(status=True)
    today = date.today()
    year = today.year
    experiences = Experience.objects.filter(status=True)

    experience_details = []
    for exp in experiences:
        experience_details.append({
            'experience': exp,
            'duration': exp.duration_display,
        })

    # Group skills by category for the template
    skill_categories = {}
    for img in skill_images:
        cat_display = img.get_category_display()
        if cat_display not in skill_categories:
            skill_categories[cat_display] = []
        skill_categories[cat_display].append(img)

    # Get only the categories that have active projects
    used_category_keys = project.values_list('category', flat=True).distinct()
    project_categories = [
        {'key': key, 'label': label}
        for key, label in PROJECT_CATEGORIES
        if key in used_category_keys
    ]

    context = {
        'about': about,
        'form': form,
        'data': social_links,
        'project': project,
        'skimg': skill_images,
        'skill_categories': skill_categories,
        'project_categories': project_categories,
        'experience': experiences.exists(),
        'year': year,
        'experience_details': experience_details,
    }

    return render(request, 'home.html', context)
