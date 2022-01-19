
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
#from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Course, Outline, Results
import requests
from bs4 import BeautifulSoup
from googlesearch import search
#import re, urllib.request

#from .forms import CourseForm

"""courses = [
    {'id': 1, 'name': 'Python'},
    {'id': 2, 'name': 'Javascript'},
    {'id': 3, 'name': 'C++'}
]"""



# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try: 
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            login(request, user)
            #print(str(user_id))
            return redirect('addcourse')
        else:
            messages.error(request, 'Username or Password does not exist')
    context = {}
    return render(request, 'base/index.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')

@login_required(login_url='index')
def addcourse(request):
    user = request.user.id
    #user = User.objects.get(request.user.id==pk)
    courses = Course.objects.filter(user=user)
    if request.method == 'POST':
        course = request.POST["course"]
        
        addCourse = Course(user=user, name=course)
        print(request.POST["course"])
        addCourse.save()
        #return redirect('addcourse')
    context = {'courses': courses}
    return render(request, 'base/addcourse.html', context) 

def updatecourse(request, pk):
    course = Course.objects.get(id=pk)
    #edit = Course(name=course)

    if request.method == 'POST':
        course.name = request.POST["item"]
        #user = User.objects.get(pk=request.user.id)
        #edit =  Course.name
        course.save()
        if 'next' in request.GET:
            return redirect(request.GET['next'])
        #return redirect('addcourse')
    context = {'course': course, 'obj': course}
    return render(request, 'base/edit.html', context)

def deletecourse(request, pk):
    course = Course.objects.get(id=pk)

    if request.method == 'POST':
        course.delete()
        return redirect('addcourse')
    return render(request, 'base/delete.html', {'obj': course})

@login_required(login_url='index')
def outline(request, pk):
    course = Course.objects.get(id=pk)
    outlines = Outline.objects.filter(course__name=course)

    if request.method == 'POST':
        topic = request.POST["topic"]
        addOutline = Outline(course=course, courseOutline=topic)
        print(request.POST["topic"])
        addOutline.save()
        #return redirect('outline')    
    context = {'course': course, 'outlines': outlines}
    
    return render(request, 'base/outline.html', context)

def updatetopic(request, pk):
    #course = Course.objects.get(id=pk)
    topic = Outline.objects.get(id=pk)
    #edit = Course(name=course)

    if request.method == 'POST':
        topic.courseOutline = request.POST["item"]
        #user = User.objects.get(pk=request.user.id)
        #edit =  Course.name
        topic.save()
        if 'next' in request.GET:
            return redirect(request.GET['next'])
    context = {'topic': topic, 'obj': topic}
    return render(request, 'base/edit.html', context)

def deletetopic(request, pk):
    topic = Outline.objects.get(id=pk)

    if request.method == 'POST':
        topic.delete()
        #return redirect('')
        if 'next' in request.GET:
            return redirect(request.GET['next'])
    context = {'obj': topic}
    return render(request, 'base/delete.html', context)

@login_required(login_url='index')
def chat(request, pk): 
    topic = Outline.objects.get(id=pk)
    commands = request.GET.get("command")
    name = Outline.objects.get(courseOutline=topic)
    
    #url = "https://www.google.com/search?q=python+.pdf"
    #response = requests.get(url)
    #soup = BeautifulSoup(response.content, "html.parser")
    #links = soup.find_all('div', {'class': 'yuRUbf'})
    #print("working")
    print(name)
    #print(links)
    #links = div.find_all('a')
    pdf_links = []
    vid_links = []
    if commands == "pdfs" or commands == "Pdfs":
        query = str(name)+" .pdf"
    
    #g_search = GoogleSearch()
        if request.method == 'GET':
            for link in search(query, num=10, stop=10, pause=2):
                pdf_links.append(link)

    elif commands == "videos" or commands == "Videos":
        query = str(name)+" .video"
        if request.method == 'GET':
            for link in search(query, num=10, stop=10, pause=2):
                vid_links.append(link)

    print(pdf_links)
    context = {'topic': topic, 'commands': commands, 'pdf_links': pdf_links, 'vid_links': vid_links}
    return render(request, 'base/chat.html', context)

#def getpdf(request, pk):
    topic = Outline.objects.get(id=pk)
    
    context = {'topic': topic}
    return render(request, 'base/chat.html', context)

def profile(request):
    return render(request, 'base/profile.html')

def signup(request):
    return render(request, 'base/signup.html') 

