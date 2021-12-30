from django.shortcuts import render,redirect
from .form import UserForm, UserRegister,imgform
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import dashboard, Register

def home(request):
    info = "Hi there!  Ajay prajapati here"
    data = {"msg": info}
    return render(request, 'Home.html', context=data)


def adduser(request):
    uform = UserForm()
    rform = UserRegister()
    if request.method=='POST':
        role = request.POST['role']
        print(role)

        uform = UserForm(request.POST)
        rform = UserRegister(request.POST)
        if uform.is_valid() and rform.is_valid():
            email = request.POST.get('email')
            if User.objects.filter(email=email).exists():              # email unique and restriction
                messages.warning(request, 'This email already exist')
            else:
                uobj = uform.save(commit=True)
                uobj.set_password(uobj.password)
                uobj.save()
                robj = rform.save(commit=False)
                robj.user = uobj
                robj.save()

                if role == 'student':
                    std = Group.objects.get(name='student')
                    uobj.groups.add(std)
                elif role == 'teacher':
                    teach = Group.objects.get(name='teacher')
                    uobj.groups.add(teach)
                elif role == 'admin':
                    admin = Group.objects.get(name='admin')
                    uobj.groups.add(admin)
                messages.success(request,'Registration success')
                redirect('/add')
    return render(request, 'register.html', {'Uform': uform, 'Rform2': rform})


def userlogin(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST['username']
        passcode = request.POST['password']
        user=authenticate(username=username,password=passcode)
        if user!=None:
            login(request,user)
            # return render(request,'dashboard.html',{'user': request.user})
            return redirect('/dash/')
        else:
            msg = "Invalid username or password"
            return render(request,'Login.html', {'msg':msg,'form':form} )
    return render(request, 'Login.html',{"form":form})


def logoutuser(request):
    print('..............',request.user)
    logout(request)

    return redirect('/')
def addimg(request):
    imgdata = imgform()
    if request.method == 'POST':
        print(request.POST, request.FILES)
        imgdata = imgform(request.POST , request.FILES)
        if imgdata.is_valid():
            imgdata.save(commit=True)
            print("Image added success")
    return render(request, 'dashboard.html', {'images':imgdata})


def showimg(request):
    # userobj = Register.objects.get(user= request.user)
    # print(userobj)
    # data = dashboard.objects.filter(student=userobj)
    # print(data)
    # data = dashboard.objects.filter(name=request.user)
    data = dashboard.objects.all()
    return render(request, 'showimg.html',{'data':data})
# username = User.objects.get('username')
# print(username)
# Create your views here.
