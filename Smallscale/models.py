from django.db import models
from django.conf import settings
from django.db.models import Q
from django.contrib.auth.models import User


# Create your models here.
class Farmers(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    National_ID=models.IntegerField()
    phone_number=models.IntegerField()
    subcounty=models.CharField(max_length=200)
    image=models.FileField(null=True, blank=True )
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.user.username


class veterinaries(models.Model):
    subcounties = [
        ('AINABKOI', 'AINABKOI'),
        ('KAPSERET', 'KAPSERET'),
        ('KESSES', 'KESSES'),
        ('MOIBEN', 'MOIBEN'),
        ('SOY', 'SOY'),
        ('TURBO', 'TURBO'),]

    wards = [
        ('AINABKOI', 'AINABKOI'),
        ('KAPTAGAT', 'KAPTAGAT'),
        ('KAPSOYA', 'KAPSOYA'),
        ('SIMAT/KAPSERET', 'SIMAT/KAPSERET'),
        ('KIPKENYO', 'KIPKENYO'),
        ('MEGUN', 'MEGUN'),
        ('NGERIA', 'NGERIA'),
        ('CHEPTIRET/KIPMACHO', 'CHEPTIRET/KIPMACHO'),
        ('RACECOURSE', 'RACECOURSE'),
        ('TULWET/CHUIYAT', 'TULWET/CHUIYAT'),
        ('MEIBEKI', 'MEIBEKI'),
        ('KIMUMU', 'KIMUMU'),
        ('MOIBEN', 'MOIBEN'),
        ('SERGOIT', 'SERGOIT'),
        ('TEMBELIO', 'TEMBELIO'),
        ('KAPKURES', 'KAPKURES'),
        ('KIPSOMBA', 'KIPSOMBA'),
        ('KUINET', 'KUINET'),
        ('MIOS BRIDGE', 'MIOS BRIDGE'),
        ('SEGERO', 'SEGERO'),
        ('SOY', 'SOY'),
        ('ZIWA', 'ZIWA'),
        ('HURUMA', 'HURUMA'),
        ('KAMAGUT', 'KAMAGUT'),
        ('KIPLOMBE', 'KIPLOMBE'),
        ('KAPSAOS', 'KAPSAOS'),
        ('NGENYILEL', 'NGENYILEL'),
        ('TAPSAGOI', 'TAPSAGOI'),
        ('TARAKWA', 'TARAKWA'),]
    speciality=[
        ('POULTRY','POULTRY'),
        ('FISHERIES','FISHERIES'),
        ('ANIMAL MEDICINE','ANIMAL MEDICINE'),
        ('ANIMAL HEALTH DIAGNOSTICS','ANIMAL HEALTH DIAGNOSTICS'),
        ('ANIMAL WELFARE','ANIMAL WELFARE'),
        ('ANIMAL DENTISTRY','ANIMAL DENTISTRY'),
        ('VETERINARY EMERGENCY/INTENSIVE CARE','VETERINARY EMERGENCY/INTENSIVE CARE'),
        ('ANIMAL NUTRITION','ANIMAL NUTRITION'),
        ]
    Vet_Name= models.CharField(max_length=200)
    ID_number= models.IntegerField()
    Email_address=models.EmailField()
    Mobile_Number=models.IntegerField()
    image=models.FileField(null=True, blank=True )
    Specialization=models.CharField(max_length=200,choices=speciality)
    subcounty=models.CharField(
        max_length=200,
        choices=subcounties)
    ward=models.CharField(max_length=200, choices=wards)
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)


class vetrequest(models.Model):
    Vet_ID=models.ForeignKey(veterinaries,on_delete=models.CASCADE)
    My_FarmerID=models.ForeignKey(Farmers,on_delete=models.CASCADE)
    request_status=models.BooleanField(default=0)
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)

class vetsession(models.Model):
    request_id=models.ForeignKey(vetrequest,on_delete=models.CASCADE)
    MPESA_code= models.CharField(max_length=200)
    my_question=models.CharField(max_length=200)
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)


class vetreply(models.Model):
    Message_ID=models.ForeignKey(vetsession,on_delete=models.CASCADE)
    reply=models.TextField()
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)

    
class lands(models.Model):
    farmerID=models.ForeignKey(Farmers,on_delete=models.CASCADE)
    land_size=models.IntegerField()
    price_per_acre=models.IntegerField()
    land_location=models.CharField(max_length=200)
    more_info=models.CharField(max_length=200)
    land_image=models.FileField(null=True, blank=True )
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)

    
class landrequest(models.Model):
    My_FarmerID=models.ForeignKey(Farmers,on_delete=models.CASCADE)
    Land_id=models.ForeignKey(lands,on_delete=models.CASCADE)
    desired_lease_period=models.IntegerField()
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
    request_status=models.BooleanField(default=0)


class equipment(models.Model):
    #equipment_id= models.AutoField(primary_key=True)
    equipment_name= models.CharField(max_length=200)
    farmerID=models.ForeignKey(Farmers,on_delete=models.CASCADE)
    price_per_day= models.IntegerField()
    Equipmemt_current_status= models.CharField(max_length=200)
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
    equipment_image=models.FileField(null=True, blank=True )

    def __str__(self):
        return self.equipment_name


class requestequip(models.Model):
    My_FarmerID= models.ForeignKey(Farmers,on_delete=models.CASCADE)
    request_status=models.BooleanField(default=0)
    equipment_id=models.ForeignKey(equipment,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
    desired_rental_period=models.IntegerField()

    
class equiprental(models.Model):
    request_ID=models.ForeignKey(requestequip,on_delete=models.CASCADE)
    MPESA_code=models.CharField(max_length=200)
    payment_status=models.BooleanField(default=0)
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)


class forum(models.Model):
    My_FarmerID= models.ForeignKey(Farmers,on_delete=models.CASCADE)
    comment= models.TextField()
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)