from django.shortcuts import render

from interests.models import Interest

# Create your views here.
def home(request):

	interests_list = Interest.objects.order_by('name')

	context = {'interests': interests_list}

	return render(request, 'default/home.html', context)
