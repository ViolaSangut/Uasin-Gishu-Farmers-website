"""Uasingishu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:''
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .import views
#from django.core.urlresolvers import reverse_lazy



app_name = "Smallscale"

urlpatterns = [

    path('',views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'), 
    path('about/', views.about, name='about'),
    path('contacts/',views.contacts, name='contacts'),
    path('saidia/',views.saidia, name='saidia'),
    path('ministry/',views.ministry, name='ministry'),
    path('agric/',views.agric, name='agric'),
    path('news/',views.news, name='news'),
    path('topstories/',views.topstories, name='topstories'),
    path('landsregister/',views.landsregister, name='landsregister'),
    path('landsearch/',views.landsearch, name='landsearh'),
    path('vetsearch/',views.vetsearch, name='vetsearh'),
    path('equipmentregister/',views.equipmentregister, name='equipmentregister'),
    path('equipsearch/',views.equipsearch, name='equipsearch'),
    path('farmereg/',views.farmereg, name='farmereg'),
    path('equiprequests/',views.equiprequests, name='equiprequests'),
    path('vetrequests/',views.vetrequests, name='vetrequests'),
    path('vet/', views.vet, name='vet'),
    path('vetaccount/', views.vetaccount, name='vetaccount'),
    path('landrequests/', views.landrequests, name='landrequests'),
    path('account/', views.account, name='account'),
    path('landrequeststatus/', views.landrequeststatus, name='landrequeststatus'),
    path('mylandrequests/', views.mylandrequests, name='mylandrequests'),
    path('equiprequeststatus/', views.equiprequeststatus, name='equiprequeststatus'),
    path('myequiprequests/', views.myequiprequests, name='myequiprequests'),
    path('myvetrequests/', views.myvetrequests, name='myvetrequests'),
    path('vetrequeststatus/', views.vetrequeststatus, name='vetrequeststatus'),
    path('paymentconfirm/', views.paymentconfirm, name='paymentconfirm'),
    path('mymessages/',views.mymessages, name='mymessages'),
    path('mylands/',views.mylands, name='mylands'),
    path('myequipment/',views.myequipment, name='myequipment'),
    path('myveterinary/',views.myveterinary, name='myveterinary'),
    path('reply/',views.reply, name='reply'),
    path('comments/',views.comments, name='comments'),
    path('initialreceipt/',views.initialreceipt, name='initialreceipt'),

    ]

