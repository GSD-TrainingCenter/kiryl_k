from django.shortcuts import render

from interests.models import Interest

# Create your views here.
def home(request):

	interests_list = Interest.objects.order_by('name')
	user_interests_list = Interest.objects.filter(users=request.user).order_by('name')

	context = {
		'interests': interests_list,
		'user_interests': user_interests_list
	}

	return render(request, 'default/home.html', context)
