from email import message
from django import http
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_control

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    if 'user' in request.session:
        return render(request, 'indexp.html')
    else:
        return redirect('/ret404')

def summarizer(request):
    if 'user' in request.session:
        roviq_categories = ["Engine Control Room", "Compressor Room", "Interview - Security Officer", "Main Deck", "Interview Senior Officer", "Steering Gear", "Interview - Deck Rating", "Interview - Electrician / ETO", "Mooring Decks", "Interview - Engineer Officer", "Interview - Rating", "Interview - Deck Officer", "Cargo Control Room", "Bow Loading Area", "Chief Engineer's Office", "Lifeboat deck", "Engine Room", "Bridge", "Forecastle", "Emergency Headquarters.", "Internal Accommodation", "Interview - Galley Rating", "Documentation", "Pre-board", "Exterior Decks", "Approaching Vessel", "Interview - Engine Rating", "Cargo Manifold", "Pumproom", "Anywhere", "Aft Mooring Deck"]

        context = {"var1":roviq_categories}
        return render(request, 'summarizer.html', context)
    else:
        return redirect('/ret404')

def uploads(request):
    if 'user' in request.session:
         return render(request, 'uploads.html')
    else:
        return redirect('/ret404')

def inspection(request):
    if 'user' in request.session:
        return render(request, 'inspection.html')
    else:
        return redirect('/ret404')

def signuptemp(request):
    return render(request, "signup.html")

def handlesignup(request):

    #Form Data
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # return HttpResponse("Successfully Submitted")

        #Form Validate
        if len(username)>10:
            return 

        #User Creation
        
        new_user = User.objects.create_user(username, email, pass1)
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.save()

        messages.success(request, "Your Account has been successfully created")
        return redirect('/')
    else:
        return redirect('/ret404')

def handlelogin(request):
    loginusername = request.POST['username']
    loginpassw = request.POST['pass']
    user = authenticate(username=loginusername, password=loginpassw)
    if user is not None:
        request.session['user'] = loginusername
        login(request, user)
        return redirect('/home')
    else:
        return redirect('/')
    # return HttpResponse("Logged in!")

def ret404(request):
    return render(request, 'ret404.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def handlelogout(request):
    del request.session['user']
    logout(request)        

    return redirect('/')