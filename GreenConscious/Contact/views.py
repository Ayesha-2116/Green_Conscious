from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('contact_success')  # Redirect to a success page after saving the form
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})
