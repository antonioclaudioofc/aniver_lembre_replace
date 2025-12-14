from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from contacts.models import Contact
from contacts.forms import ContactForm
from reminders.forms import ReminderForm
from reminders.models import Remiders


def index(request):
    contacts = Contact.objects.all()
    reminders = Remiders.objects.select_related(
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


def create_reminder(request):
    if request.method != 'POST':
        return redirect(reverse('dashboard:index'))

    contact_form = ContactForm(request.POST)
    reminder_form = ReminderForm(request.POST)

    if contact_form.is_valid() and reminder_form.is_valid():
        contact = contact_form.save(commit=False)
        contact.save()
        reminder = reminder_form.save(commit=False)
        reminder.contact = contact
        reminder.save()
        messages.success(request, 'Contato e lembrete criados com sucesso!')
    else:
        messages.error(
            request, 'Erro ao criar. Verifique os dados do contato e do lembrete.')

    return redirect(reverse('dashboard:index'))
