from django.shortcuts import render, redirect
from .forms import MedicationForm
from .models import MedicationRecord
from datetime import datetime, timedelta

def add_record(request):
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker:report')
    else:
        form = MedicationForm()
    return render(request, 'tracker/add_record.html', {'form': form})

def report(request):
    one_week_ago = datetime.now() - timedelta(days=7)
    records = MedicationRecord.objects.filter(date__gte=one_week_ago).order_by('-date')
    total_dose = sum(record.dose for record in records)
    return render(request, 'tracker/report.html', {'records': records, 'total_dose': total_dose})

def home(request):
    return render(request, 'tracker/home.html')