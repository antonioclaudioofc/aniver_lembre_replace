from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from contacts.models import Contact
from contacts.forms import ContactForm
from reminders.forms import ReminderForm
from reminders.models import Reminder


@login_required
def index(request):
    profile = request.user.profile

    contacts = Contact.objects.filter(owner=profile)
    reminders = Reminder.objects.filter(contact__owner=profile).select_related(
        'contact').order_by('-created_at')

    contact_form = ContactForm()
    reminder_form = ReminderForm()

    return render(request, 'dashboard/index.html',
                  {
                      'contacts': contacts,
                      'reminders': reminders,
                      'contact_form': contact_form,
                      'reminder_form': reminder_form,
                  })


@login_required
def create_reminder(request):
    if request.method != 'POST':
        return redirect(reverse('dashboard:index'))

    profile = request.user.profile
    contact_form = ContactForm(request.POST)
    reminder_form = ReminderForm(request.POST)

    if contact_form.is_valid() and reminder_form.is_valid():
        try:
            contact = contact_form.save(commit=False)
            contact.owner = profile
            contact.save()
            reminder = reminder_form.save(commit=False)
            reminder.contact = contact
            reminder.save()
            return redirect(reverse('dashboard:index'))
        except Exception:
            pass

    contacts = Contact.objects.filter(owner=profile)
    reminders = Reminder.objects.filter(contact__owner=profile).select_related(
        'contact').order_by('-created_at')

    return render(request, 'dashboard/index.html',
                  {
                      'contacts': contacts,
                      'reminders': reminders,
                      'contact_form': contact_form,
                      'reminder_form': reminder_form,
                      'show_dialog': True,
                  })
