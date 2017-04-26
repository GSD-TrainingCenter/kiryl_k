from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from interests.models import Interest, Page

# Create your views here.
@login_required
def home(request):

	interests_list = Interest.objects.order_by('name')

	for interest in interests_list:
		interest.url = interest.name.replace(' ', '_')

	user_interests_list = Interest.objects.filter(users=request.user).order_by('name')

	for interest in user_interests_list:
		interest.url = interest.name.replace(' ', '_')

	context = {
		'interests': interests_list,
		'user_interests': user_interests_list,
	}

	return render(request, 'default/home.html', context)


def interest(request, interest_name_url):
	interest_name = interest_name_url.replace('_', ' ')

	interest = Interest.objects.filter(name=interest_name).values('name', 'description')

	context = {
		'interest': interest,
	}

	return render(request, 'default/interest.html', context)