from django.shortcuts import render
from django.http import HttpResponse

from .models import Profile

# Create your views here.

def index(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    context = {'nickname': profile.nickname, 'status': profile.status, 'premium': profile.premium}
    return render(request, 'profilepage/index.html', context)