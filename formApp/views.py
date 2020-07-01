
from django.shortcuts import render
from .forms import RecordForm

def index(request):
    form = RecordForm(request.POST or None)
    wasCreated = False
    if form.is_valid():
        form.save()
        form = RecordForm()
        wasCreated = True

    return render(request, "formApp/index.html", {"form":form,"wasCreated": wasCreated})