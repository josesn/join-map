import datetime

from decimal import Decimal
from django.shortcuts import render, redirect
from .models import Target
from .forms import TargetForm

def target_map(request):
    if request.method == "POST":
        print(request.POST)
        form = TargetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TargetForm()
        
    targets = list(Target.objects.values('name', 'geocode', 'expire_date'))
    context = {'targets': targets, 'form': form}
    return render(request, 'index.html', context)