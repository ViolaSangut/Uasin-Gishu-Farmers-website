from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import equipment, lands, Farmers,requestequip,vetrequest,equiprental,landrequest,vetsession,vetreply, forum
from django.forms import ModelForm





class landsearchForm(forms.Form):
    land_location=forms.CharField(max_length=200)
    land_size=forms.IntegerField()

class vetrequestForm(forms.ModelForm):
    Vet_ID=forms.IntegerField() 
    My_FarmerID=forms.IntegerField()
    class Meta:
        model=vetrequest
        fields=['Vet_ID','My_FarmerID']

class vetsessionForm (forms.ModelForm):
    request_id=forms.IntegerField()
    MPESA_code= forms.CharField(max_length=200)
    my_question=forms.CharField(max_length=200)

    class Meta:
        model=vetsession
        fields=['request_id','MPESA_code','my_question']


class vetreplyForm(forms.ModelForm):
    Message_ID=forms.IntegerField()
    reply=forms.CharField(widget=forms.Textarea)

    class Meta:
        model=vetreply
        fields=['Message_ID','reply']
class commentForm(forms.ModelForm):
    comment= forms.CharField(widget=forms.Textarea)
    My_FarmerID=forms.IntegerField()

    class Meta:
        model=forum
        fields= ['My_FarmerID','comment']

class landrequestForm(forms.ModelForm):
    My_FarmerID=forms.IntegerField()
    My_name=forms.CharField(max_length=200)
    Land_id=forms.IntegerField()
    desired_lease_period=forms.IntegerField()

    class Meta:
        model=landrequest
        fields=['My_FarmerID','My_name','Land_id','desired_lease_period']



class equipmentregisterForm(forms.ModelForm):
    equipment_name= forms.CharField(max_length=200)
    farmerID=forms.IntegerField()
    price_per_day= forms.IntegerField()
    Equipmemt_current_status= forms.CharField(max_length=200)
    equipment_image=forms.FileField(required=False)
    class Meta:
        model=equipment
        fields=['equipment_name','farmerID','price_per_day','Equipmemt_current_status','equipment_image']
    


class equipsearchForm(forms.Form):
    equipment_name= forms.CharField(max_length=200)

class equiprentalForm(forms.ModelForm):
    request_ID=forms.IntegerField()
    MPESA_code=forms.CharField(max_length=200)
    class Meta:
        model=equiprental
        fields=['request_ID','MPESA_code']
    
class LandsregisterForm(forms.ModelForm):
    farmerID=forms.IntegerField()
    land_size=forms.IntegerField()
    price_per_acre =forms.IntegerField()
    land_location=forms.CharField(max_length=200)
    more_info=forms.CharField(max_length=200)
    land_image=forms.FileField(required=False)
    

    class Meta:
        model=lands
        fields=['farmerID','land_size','price_per_acre','land_location','more_info','land_image']
    # def save(self, commit=True):
    #     lands =super(LandsregisterForm, self).save(commit=False)
    #     lands.Owners_id =self.cleaned_data['Owners_id']
    #     lands.land_size =self.cleaned_data['land_size']
    #     lands.price=self.cleaned_data['price']
    #     lands.land_location=self.cleaned_data['land_location']
    #     lands.Specifics=self.cleaned_data['Specifics']
    #     lands.image1=self.cleaned_data['image1']
    #     lands.image2=self.cleaned_data['image2']
        
    #     if commit:
    #         lands.save()
    #     return lands


class NewUserForm (UserCreationForm):
    email =forms.EmailField(required=True)
    class Meta:
        model =User
        fields =("username", "email", "password1", "password2")

    def save(self, commit=True):
        user =super(NewUserForm, self).save(commit=False)
        user.email =self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class equiprequestsForm(forms.ModelForm):
    My_FarmerID=forms.IntegerField(required=True)
    equipment_id=forms.IntegerField(required=True)
    desired_rental_period=forms.IntegerField()
    class Meta:
        model=requestequip
        fields=['My_FarmerID','equipment_id','desired_rental_period']


class FarmerForm (forms.ModelForm):
    
    National_ID =forms.IntegerField(required=True)
    phone_number=forms.IntegerField(required=True)
    subcounty = forms.CharField(max_length=200)
    image=forms.FileField(required=False )
    class Meta:
        model =Farmers
        fields =['National_ID','phone_number','subcounty','image']
    



