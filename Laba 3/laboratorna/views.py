from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from . models import Student, Profile

### Pages
def start(request):
	return render(request, 'laboratorna_app/startpage.html')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			profile = Profile(name='',surname='',username = username,location='',age='',img='',hobbies='')
			profile.save()
			return redirect('index')
	else:
	    form = UserCreationForm()
	context = {'form':form}
	return render(request,'registration/register.html',context)

def index(request):
	events = Student.objects.all()
	context = {'events':events}
	return render(request, 'laboratorna_app/index.html',context)

def myevents(request):
	events = Student.objects.all()
	context = {'events':events}
	return render(request, 'laboratorna_app/myevents.html',context)

def createEvent(request):
	events = Student.objects.all()
	context = {'events':events}
	return render(request, 'laboratorna_app/createEvent.html',context)

def profile(request):
	profiles = Profile.objects.all()
	context = {'profiles':profiles}
	return render(request, 'laboratorna_app/profile.html',context)

### Profile
def editprofile(request, id):
	profile = Profile.objects.get(id=id)
	context = {"profile":profile}
	return render(request, 'laboratorna_app/editprofile.html',context)

def updateprofile(request, id):
	profile = Profile.objects.get(id=id)
	profile.name = request.POST['name']
	profile.surname = request.POST['surname']
	profile.location = request.POST['location']
	profile.age = request.POST['age']
	profile.img = request.POST['img']
	profile.hobbies = request.POST['hobbies']
	profile.save()
	return redirect('profile')

def add(request):
    print(request.POST)
    event = Student(name = request.POST['name'],surname = request.POST['location'],mark = request.POST['date'],creator = request.user.username)
    event.save()
    return redirect('index')

def edit(request, id):
	event = Student.objects.get(id=id)
	context = {"event":event}
	return render(request, 'laboratorna_app/edit.html',context)

def update(request, id):
	event = Student.objects.get(id=id)
	event.name = request.POST['name']
	event.surname = request.POST['location']
	event.mark = request.POST['location']
	event.save()
	return redirect('index')

def destroy(request, id):
	event = Student.objects.get(id=id)
	event.delete()
	return redirect('index')