from django.shortcuts import render

# Create your views here.
# registration/views.py
from django.shortcuts import render, redirect
from .forms import ExamRegistrationForm

def exam_registration(request):
    if request.method == 'POST':
        form = ExamRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the data
            # For now, just print it
            print(form.cleaned_data)
            # Redirect after successful form submission (POST-redirect pattern)
            return redirect('success')
    else:
        form = ExamRegistrationForm()
    return render(request, 'exam_registration.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')
