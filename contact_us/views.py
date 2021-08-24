from django.http import request
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_us/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, "contact_us/contact_us.html",context)