from django.shortcuts import render
from django.http import HttpResponse

from interests.models import Interest, Page

# Create your views here.
def home(request):

	interests_list = Interest.objects.order_by('name')

	for interest in interests_list:
		interest.url = interest.name.replace(' ', '_')

	user_interests_list = Interest.objects.filter(users=request.user).order_by('name')

	# for interest in interests_list:
	# 	interest.url = interest.name.replace(' ','_')

	context = {
		'interests': interests_list,
		'user_interests': user_interests_list,
	}

	return render(request, 'default/home.html', context)


def interest(request, interest_name_url):
	interest_name = interest_name_url.replace('_', ' ')
	context = {
		'interest_name': interest_name,
	}

	try:
		interest = Interest.objects.get(name=interest_name)
		pages = Page.objects.filter(interest=interest)
		context['pages'] = pages
		context['interest'] = interest
	except Interest.DoesNotExist:
		pass

	return render(request, 'default/interest.html', context)