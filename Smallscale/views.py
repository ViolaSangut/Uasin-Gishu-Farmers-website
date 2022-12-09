from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import vetrequestForm,vetreplyForm,equiprentalForm,commentForm,equiprequestsForm,landrequestForm,NewUserForm,FarmerForm,LandsregisterForm,landsearchForm, equipmentregisterForm, equipsearchForm, vetsessionForm
from django.contrib.auth.models import User
from .models import equipment, lands,equiprental, Farmers, veterinaries, forum,vetrequest,landrequest,requestequip,vetsession,vetreply
from django.contrib.auth.decorators import login_required
#from django.http import Http404, HttpResponseForbidden
#from django.views.generic.edit import FormMixin
#from django.views.generic import DetailView, ListView



# Create your views here.



def homepage(request):
    return render(request=request,
                  template_name="main/home.html")



    
def register(request):
    if request.method == "POST":
        form=NewUserForm(request.POST)
        farmer_form= FarmerForm(request.POST, request.FILES or None )
        if form.is_valid() and farmer_form.is_valid():
            user = form.save()
            
            profile=farmer_form.save(commit=False)
            profile.user=user

            profile.save()

            username =form.cleaned_data.get('username')
            messages.success(request, f"new account created:{username}")
            login(request, user)
            messages.info(request, f"you are now logged in as:{username}")
            return redirect("Smallscale:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages [msg]}")
    else:
        form=NewUserForm()
        farmer_form= FarmerForm()
    return render(request=request,
                  template_name="main/register.html",
                  context={"form":form,
                           "farmer_form":farmer_form})

def account(request):
  return render(request=request,
                  template_name="main/account.html")

def myveterinary(request):
  return render(request=request,
                  template_name="main/myveterinary.html")

def mylands(request):
  return render(request=request,
                  template_name="main/mylands.html")

def myequipment(request):
  return render(request=request,
                  template_name="main/myequipment.html")



def farmereg(request):
    if request.method == "POST":
        form=FarmerForm(request.POST, request.FILES or None)
        if form.is_valid():
            farmers = form.save()
            messages.success(request, f"your farmers profile has successfully been created")
            messages.info(request, f"you can view your farmer profile by clicking your username on the menu above ")
            return redirect("Smallscale:farmereg")
    else:
        form=FarmerForm()
        
    return render (request,
                   template_name="main/farmereg.html",
                   context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "successfully logged out!")
    return redirect("Smallscale:homepage") 



def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            password =form.cleaned_data.get('password')
            username =form.cleaned_data.get('username')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are now logged in as:{username}")
                return redirect("Smallscale:homepage") 
            else:
                messages.error(request,"invalid username or password")
        else:
            messages.error(request,"invalid username or password")    
    form = AuthenticationForm()
    return render(request, "main/login.html",
    {"form":form})  

def about(request):
    return render(request,
                  template_name="main/about.html")

def contacts(request):
    return render(request,
                  template_name="main/aboutus/contacts.html")

def saidia(request):
    return render(request,
                  template_name="main/aboutus/saidia.html")

def agric(request):
    return render(request,
                  template_name="main/aboutus/agric.html")

def ministry(request):
    return render(request,
                  template_name="main/aboutus/ministry.html")

def news(request):
    if request.method == "POST":
        form=commentForm(request.POST, request.FILES or None)
        if form.is_valid():
            forum = form.save()
            return redirect("Smallscale:farmereg")
    else:
        form=commentForm()

    return render(request,
                  template_name="main/habari/news.html",
                  context={"form":form})

def comments(request):
    queryset_list=forum.objects.all().order_by("-timestamp")

    paginator = Paginator(queryset_list, 5) 
    page_number = request.GET.get('page')
    comment_list = paginator.get_page(page_number)
    page_request_var="page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    return render(request,
                  template_name="main/habari/comments.html",
                  context={"comment_list":queryset,
                            "page_request_var":page_request_var})

def topstories(request):
    return render(request,
                  template_name="main/habari/stopstories.html")

def landsearch(request):
    queryset_list = lands.objects.all().order_by("-timestamp")

    query=request.GET.get("q")
    if query:
      queryset_list=queryset_list.filter(land_location__icontains=query)

    paginator = Paginator(queryset_list, 2) 
    page_number = request.GET.get('page')
    lands_list = paginator.get_page(page_number)
    page_request_var="page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    
    form=landsearchForm()
    return render (request,
                   template_name="main/lands/landsearch.html",
                   context={"lands_list":queryset,
                            "page_request_var":page_request_var})
def landrequests(request):
    if request.method == "POST":
        form=landrequestForm(request.POST, request.FILES or None)
        if form.is_valid():
            landrequest = form.save()
            messages.success(request, f"your request has been successfully sent.")
            messages.info(request, f"Check your request status  on your account by clicking on your username on the menu above ")
            return redirect("Smallscale:landrequests")
    else:
        form=landrequestForm()

    form=landrequestForm()
    return render (request,
                   template_name="main/lands/landrequest.html",
                   context={"form":form})



@login_required
def landrequeststatus(request):
    mylandstatus=landrequest.objects.all()
    mylandstatus=mylandstatus.filter(My_FarmerID__user=request.user)

    return render (request,
                   template_name="main/lands/landrequeststatus.html",
                   context={"mylandstatus":mylandstatus})


    
@login_required
def mylandrequests(request):
    landreq=landrequest.objects.all()
    landreq=landreq.filter(Land_id__farmerID__user=request.user)

    return render (request,
                   template_name="main/lands/mylandrequests.html",
                   context={"landreq":landreq})



def equipmentregister(request):
    if request.method == "POST":
        form=equipmentregisterForm(request.POST, request.FILES or None)
        if form.is_valid():
           # equipment = form.save().
           instance=form.save(commit=False)
           instance.owners_id_number=request.farmers
           instance.save()
           messages.success(request, f"you have successfully registered your land!")
            
    form=equipmentregisterForm()
    return render (request,
                   template_name="main/equipment/equipmentregister.html",
                   context={"form":form})

def equipsearch(request):
    queryset_list = equipment.objects.all().order_by("-timestamp")

    query=request.GET.get("q")
    if query:
      queryset_list=queryset_list.filter(equipment_name__icontains=query)

    paginator = Paginator(queryset_list, 2) 
    page_number = request.GET.get('page')
    equip_list = paginator.get_page(page_number)
    page_request_var="page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    
    form=equipsearchForm()
    return render(request,
                 template_name="main/equipment/equipsearch.html",
                 context={"equip_list":queryset,
                         "page_request_var":page_request_var})

def equiprequests(request):
    form=equiprequestsForm()
    return render(request,
                  template_name="main/equipment/equiprequests.html",
                  context={"form":form})
@login_required
def equiprequeststatus(request):
    myequipstatus=requestequip.objects.all()
    
    myequipstatus=myequipstatus.filter(My_FarmerID__user=request.user)

    if request.method == "POST":
        form=equiprentalForm(request.POST, request.FILES or None)
        if form.is_valid():
            equiprental = form.save()
            messages.success(request, f"you have successfully made the initial payment for the equipment.")
            return redirect("Smallscale:equiprequeststatus")            
    else:
        form=equiprentalForm()

    return render (request,
                   template_name="main/equipment/equiprequeststatus.html",
                   context={"myequipstatus":myequipstatus,
                            "form":form})
    
@login_required
def myequiprequests(request):
    equipreq=requestequip.objects.all()
    
    equipreq=equipreq.filter(equipment_id__farmerID__user=request.user)

    return render (request,
                   template_name="main/equipment/myequiprequests.html",
                   context={"equipreq":equipreq})

@login_required
def initialreceipt(request):
    rental=equiprental.objects.all()

    rental=rental.filter(request_ID__My_FarmerID__user=request.user)

    return render (request,
                   template_name="main/equipment/initialreceipt.html",
                   context={"rental":rental})

def landsregister(request):
   # farmer=Farmers.objects.get(id=pk)
    #form=LandsregisterForm(initial=("farmer".farmer))

    if request.method == "POST":
        form=LandsregisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            lands = form.save()
            messages.success(request, f"you have successfully registered your land!")
            return redirect("Smallscale:landsregister")
            
    # queryset=equipment.objects.all()    
    else:
      form=LandsregisterForm()
    
    return render(request, 
      template_name="main/lands/landsregister.html", 
      context={"form":form})
def vet(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            password =form.cleaned_data.get('password')
            username =form.cleaned_data.get('username')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are now logged in as:{username}")
                return redirect("Smallscale:vetaccount") 
            else:
                messages.error(request,"invalid username or password")
        else:
            messages.error(request,"invalid username or password")    
    form = AuthenticationForm()
    return render(request, "main/veterinary/vetlogin.html",
                {"form":form}) 

def vetaccount(request):
    return render(request,"main/veterinary/vetaccount.html") 

def myvetrequests(request):
    vetreq=vetrequest.objects.all()
    query=request.GET.get("q")
    if query:
      vetreq=vetreq.filter(Vet_ID=query)

    return render (request,
                   template_name="main/veterinary/myvetrequests.html",
                   context={"vetreq":vetreq})

@login_required
def vetrequeststatus(request):
    vetreqstatus=vetrequest.objects.all()
    
    vetreqstatus=vetreqstatus.filter(My_FarmerID__user=request.user)

    return render (request,
                   template_name="main/veterinary/vetrequeststatus.html",
                   context={"vetreqstatus":vetreqstatus})

def paymentconfirm(request):
    if request.method == "POST":
        form=vetsessionForm(request.POST, request.FILES or None)
        if form.is_valid():
            vetsession = form.save()
            messages.success(request, f"your message has been successfully sent")    
            return redirect("Smallscale:paymentconfirm")
    else:
        form=vetsessionForm()

     
    return render(request,
                   template_name="main/veterinary/paymentconfirm.html",
                   context={"form": form}) 

def mymessages(request):
    message=vetsession.objects.all()
    query=request.GET.get("q")
    if query:
      message=message.filter(request_id__Vet_ID=query)


    if request.method == "POST":
        form=vetreplyForm(request.POST, request.FILES or None)
        if form.is_valid:
            vetreply = form.save()
            messages.success(request, f"your reply has been sent to the farmer")    
            return redirect("Smallscale:mymessages")
    else:
        form=vetreplyForm()

     
    return render(request,
                   template_name="main/veterinary/mymessages.html",
                   context={"form": form,
                            "message":message})
@login_required
def reply(request):
    queryset=vetreply.objects.all()
    
    queryset=queryset.filter(Message_ID__request_id__My_FarmerID__user=request.user)

    return render(request,
                   template_name="main/veterinary/reply.html",
                   context={"queryset":queryset})

def vetsearch(request):
    queryset_list = veterinaries.objects.all().order_by("-timestamp")

    query=request.GET.get("q")
    if query:
      queryset_list=queryset_list.filter(Specialization__icontains=query)

    paginator = Paginator(queryset_list, 2) 
    page_number = request.GET.get('page')
    vet_list = paginator.get_page(page_number)
    page_request_var="page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    
    #form=vetsearchForm()
    return render(request,
                 template_name="main/veterinary/vetsearch.html",
                 context={"vet_list":queryset,
                         "page_request_var":page_request_var})
def vetrequests(request):
    if request.method == "POST":
        form=vetrequestForm(request.POST, request.FILES or None)
        if form.is_valid():
            vetrequest = form.save()
            messages.success(request, f"your request has been successfully sent.")
            messages.info(request, f"Check your request status  on your account by clicking on your username on the menu above ")
            return redirect("Smallscale:vetrequests")
    else:
        form=vetrequestForm()
        
    return render (request,
                   template_name="main/veterinary/vetrequest.html",
                   context={"form": form})