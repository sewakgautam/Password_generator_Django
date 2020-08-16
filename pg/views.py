from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request, 'index.html')
    
def password(request):
    
    characters = list('')
    if request.GET.get('lowercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))


    length=int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'password.html',{'password': thepassword})