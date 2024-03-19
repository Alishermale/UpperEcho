from django.shortcuts import render
from .forms import TextDataForm


async def echo(request):
    if request.method == 'POST':
        form = TextDataForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            uppercased_message = text.upper()
            return render(request, 'input_text.html', {'form': form, 'my_text': uppercased_message})
    else:
        form = TextDataForm()
    return render(request, 'input_text.html', {'form': form})
