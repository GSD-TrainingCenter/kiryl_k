from django.shortcuts import render

# Create your views here.
def home(request):
	context = {

	}
	return render(request, 'default/home.html', context)
