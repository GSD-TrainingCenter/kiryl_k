from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import UserForm, UserProfileForm, CreateNewInterest

# Create your views here.
def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'avatar' in request.FILES:
				profile.avatar = request.FILES['avatar']

			profile.save()

			registered = True

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'interests/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def create_new_interest(request):
	if request.method == 'POST':
		new_interest = CreateNewInterest(data=request.POST)

		if new_interest.is_valid():
			new_interest.save()
			return HttpResponseRedirect('/')

		else:
			print(new_interest.errors)

	else:
		new_interest = CreateNewInterest

	return render(request, 'interests/newinterest.html', {'new_interest': new_interest})


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse('Your account is disabled.')

		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")

	else:
		return render(request, 'interests/login.html', {})


@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/login/')


@login_required
def update_profile(request):
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'avatar' in request.FILES:
				profile.avatar = request.FILES['avatar']

			profile.save()

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'interests/update_profile.html', {'user_form': user_form, 'profile_form': profile_form} )