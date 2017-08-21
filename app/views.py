from django.shortcuts import render
from .models import profile

def home(request):
    profiles = profile.objects.all()
    pat = request.GET
    context = {'profiles': profiles, 'pat': pat}
    template = "index.html"
    return render(request, template, context)

def get(request, id):
    if request.method == "GET":
        profiles = profile.objects.filter(pk=id)

    context = {'profiles': profiles}
    template = "index.html"
    return render(request, template, context)