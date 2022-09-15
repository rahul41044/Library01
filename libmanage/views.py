from django.shortcuts import render,HttpResponseRedirect
from.forms import Signupform,Loginform,StudentRegistration
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from.models import Student
from django.contrib.auth.models import Group

def homepage(request):
    return render(request,'home.html')


# Signup
def user_signup(request):
    if request.method=='POST':
        form=Signupform(request.POST)
        if form.is_valid():
            messages.success(request,'You Are A Member Now....!')
            form.save()
            user=form.save()
            group=Group.objects.get(name='Student')
            user.groups.add(group)
    else:
        form=Signupform()
    return render(request,'signup.html',{'form':form})


# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=Loginform(request=request, data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/dashboard/')
        else:
            form=Loginform()
        return render(request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')


# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm=StudentRegistration(request.POST)
            if fm.is_valid():
                bk=fm.cleaned_data['book']
                au=fm.cleaned_data['author']
                it=fm.cleaned_data['issuedto']
                id=fm.cleaned_data['issueddate']
                reg=Student(book=bk,author=au,issuedto=it,issueddate=id)
                reg.save()
                fm=StudentRegistration()
        else:
            fm=StudentRegistration()
        stud=Student.objects.all()

        return render(request,"addshow.html",{'form':fm,'stu':stud})
    else:
        return HttpResponseRedirect('/login/')

# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


#this funcation udate/edit
def update_data(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Student.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'update.html',{'form':fm})


#this function will delete
def delete_data(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/dashboard/')
