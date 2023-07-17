from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .models import Article
# Create your views here.  


def home(request):
    
    
    objects=Article.objects.all()
    
    
    
    return render(request,"mainpage.html",{"objects":objects})


def signin(request):
    if request.method == "POST":
        
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user= authenticate(request,username=username,password=password)
    
        if user is not None:
            login(request,user)
        
            
            ### we need for use for futher used of user id
            user_id = user.id
            request.session['user_id'] = user_id
            return redirect("staff_view")
        else:
            return render(request,"signin.html",{})
        
    else:
        return render(request,"signin.html",{})
    

    


"""
def signin(request):
    
    return render(request,"signin.html")
"""

def logoutUser(request):
    
    logout(request)
    return redirect("home")



@login_required(login_url="signin")
def write(request):
    
    user_pk = request.session.get('user_id')
    
    
    if request.method == "POST":
        
        form = ArticleForm(request.POST or None)
        if form.is_valid():
            
            
            
            
            
            
            Article_Save=form.save(commit=False)
            Article_Save.user_id = user_pk
            Article_Save.save()
            
            messages.success(request,("your Article succesfully store"))
            return redirect("home")
        else:
            messages.success(request,("Please make sure your form not null"))
            return render(request,"write.html")
    
    else:
       return render(request,"write.html")
   


# must be adjust because the article cant get their own pharagraph
def article_view(request,pk):
    
    obj = Article.objects.get(id=pk)
    
    
    
    return render(request,"articleview.html",{"obj":obj})

@login_required(login_url="signin")
def staff_views(request):
    
    objects=Article.objects.all()
    
    return render(request,"adminview.html",{"objects":objects})


@login_required(login_url="signin")
def article_setting(request,pk):
    
    obj = Article.objects.get(id=pk)
    
    return render(request,"articlesetting.html",{"obj":obj})
    