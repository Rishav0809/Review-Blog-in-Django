from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import ReviewForm,ExpertProfileForm
from .models import Review,ExpertProfile,GenerateCode
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
import random 
from django.core.files.storage import FileSystemStorage

def home(request):
    reviews=Review.objects.all().order_by('?')[:6]
    profiles=ExpertProfile.objects.all().order_by('?')[:3]
    return render(request, 'review/home/index.html',{'reviews':reviews,'profiles':profiles})


def allexperts(request):
    reviews=Review.objects.all().order_by('?')
    profiles=ExpertProfile.objects.all().order_by('?')
    return render(request, 'review/all/experts.html',{'reviews':reviews,'profiles':profiles})
    

def allreviews(request):
    reviews=Review.objects.all().order_by('?')
    profiles=ExpertProfile.objects.all().order_by('?')
    return render(request, 'review/all/reviews.html',{'reviews':reviews,'profiles':profiles})
    
def profile(request, profile_pk):
    profile=get_object_or_404(ExpertProfile,pk=profile_pk)
    return render(request, "review/view/profile.html",{'profile':profile})


def review(request,review_pk):
    review=get_object_or_404(Review,pk=review_pk)
    profile=get_object_or_404(ExpertProfile,user=review.author)
    return render(request, "review/view/review.html",{'review':review,'profile':profile})


################################### AUTHENTICATION ##################################################



def signupuser(request):
    if request.method=='GET':
        return render(request, 'review/signup/signupuser.html')
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                profile=ExpertProfile()
                profile.name=request.POST['name']
                profile.number=request.POST['number']
                profile.category=request.POST['category']
                profile.photo=request.FILES['photo']
                profile.email=request.POST['email']
                profile.facebook=request.POST['facebook']
                profile.description=request.POST['description']
                profile.user=request.user
                profile.save()
                return redirect('userpanel')
            except IntegrityError:
                return render(request, 'review/signup/signupuser.html', {'error':'That username has already been taken. Please choose a new one.'})
        else:
            return render(request, 'review/signup/signupuser.html', {'error':'Passwords did not match'})



def loginuser(request):
    if request.method=='GET':
        return render(request, 'review/login/login.html')
    else:
        user=authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'review/login/login.html', {'error':'Username or Password is invalid.'})
        else:
            login(request, user)
            return redirect('userpanel')


@login_required
def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')


################################### END OF AUTHENTICATION ##################################################




################################### UPDATION ###############################################

@login_required
def updateprofilephoto(request):
    if request.method=='POST':
        profile=get_object_or_404(ExpertProfile,user=request.user)
        profile.photo=request.FILES['newphoto']
        # profile.user=request.user
        profile.save()
        return redirect('userpanel')


@login_required
def editreview(request,review_pk):
    data=get_object_or_404(Review,pk=review_pk)
    if request.method=='POST':
        return render(request,'review/createreview/edit.html',{'data':data})
    else:
        pass


@login_required
def update(request):
    if request.method=='POST':
        review=get_object_or_404(Review,author=request.user)
        review.title=request.POST['title']
        review.description=request.POST['review']
        review.mainphoto=request.FILES['mainphoto']
        review.photo1=request.FILES['photo1']
        review.photo2=request.FILES['photo2']
        review.photo3=request.FILES['photo3']
        review.photo4=request.FILES['photo4']
        review.save()
        return redirect('expertreviews')

@login_required
def updateprofile(request):
    if request.method=='POST':
        profile=get_object_or_404(ExpertProfile,user=request.user)
        profile.name=request.POST['name']
        profile.email=request.POST['email']
        profile.number=request.POST['number']
        profile.description=request.POST['description']
        profile.category=request.POST['category']
        profile.facebook=request.POST['facebook']
        profile.save()
        return redirect('userpanel')

################################### END OF UPDATION ###############################################



############################################ DASHBOARD #################################################
    
@login_required
def userpanel(request):
    profile=get_object_or_404(ExpertProfile,user=request.user)
    return render(request, 'review/userpanel/dashboard.html',{'profile':profile})


@login_required
def createreview(request):
    if request.method=='GET':
        return render(request,'review/createreview/index.html')
    else:
        try:
            data=Review()
            profile=get_object_or_404(ExpertProfile,user=request.user)

            if profile.Credits<=0:
                return render(request,'review/createreview/index.html',{'error':'You do not have enough credits to post a review. Kindly recharge.'})
            else:
                data.title=request.POST['title']
                data.description=request.POST['review']
                data.mainphoto=request.FILES['mainphoto']
                data.photo1=request.FILES['photo1']
                data.photo2=request.FILES['photo2']
                data.photo3=request.FILES['photo3']
                data.photo4=request.FILES['photo4']
                data.author=request.user
                data.save()
                profile.Credits-=1
                profile.save()
                return redirect('userpanel')  
        except ValueError:
            return render(request,'review/createreview/index.html',{'error':'Title too long'})




@login_required
def expertreviews(request):
    
    profile=get_object_or_404(ExpertProfile,user=request.user)
    reviews=Review.objects.filter(author=request.user)
    return render(request,"review/userpanel/reviews.html",{'profile':profile,'reviews':reviews})



############################################ END OF DASHBOARD #################################################




################################################### CREDIT SYSTEM ###############################################

@login_required
def generatecode(request):
    profile=get_object_or_404(ExpertProfile,user=request.user)
    if request.method=='POST':
        characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()0123456789')
        thepassword = ''
        for x in range(15):
            thepassword += random.choice(characters)

        credit=GenerateCode()
        credit.code=thepassword
        credit.value=request.POST['credit']
        credit.save()
        
        return render(request,'review/userpanel/dashboard.html',{'profile':profile,'code':thepassword})
    else:
        return render(request,'review/userpanel/dashboard.html',{'profile':profile,'code':'Generate Code'})
        

def redeemcode(request):
    profile=get_object_or_404(ExpertProfile,user=request.user)
    
    if request.method=='POST':
        credits=get_object_or_404(GenerateCode,code=request.POST['code'])
        if credits:
            profile.Credits += credits.value
            profile.save()
            credits.delete()
            return redirect('userpanel')


################################################### END OF CREDIT SYSTEM ###############################################




