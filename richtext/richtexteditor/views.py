
from .forms import RichTextModelForm

from django.shortcuts import render, redirect
from .forms import YourForm
from .models import YourModel

def save_form_view(request):
    if request.method == 'POST':
        form = YourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rich-text-editor')  # Replace with your success page URL
        else:
            print(form.errors)
    else:
        form = YourForm()

    return render(request, 'richtext.html', {'form': form})

def show_saved_data(request):
    saved_data = YourModel.objects.all()  # Assuming you have at least one saved instance
    return render(request, 'show.html', {'saved_data': saved_data})




def rich_text_editor(request):
    if request.method == 'POST':
        form = RichTextModelForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or handle success as needed
    else:
        form = RichTextModelForm()

    return render(request, 'richtext.html', {'form': form})
