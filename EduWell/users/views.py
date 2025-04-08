from django.shortcuts import render, redirect
from .forms import MoodForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

@login_required
def calendar(request):
    return render(request, 'core/calendar.html')

@login_required
def wellness_view(request):
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            # Save or process mood data
            return redirect('dashboard')
    else:
        form = MoodForm()
    return render(request, 'core/wellness.html', {'form': form})
