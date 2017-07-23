from django.shortcuts import render, redirect

# Create your views here.

def home_redirect(request):
	return redirect('home')
	
def home(request):
	return render(request, 'basis/home.html', {})

def members(request):
	return render(request, 'basis/members.html', {})

def guest(request):
	return render(request, 'basis/guest.html', {})