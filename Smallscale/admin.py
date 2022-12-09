from django.contrib import admin
from .models import equipment,Farmers,forum, veterinaries, lands, landrequest, requestequip, vetrequest,vetreply,vetsession, equiprental


# Register your models here.
admin.site.register(equipment)
admin.site.register(Farmers)
admin.site.register(veterinaries)
admin.site.register(lands)
admin.site.register(landrequest)
admin.site.register(requestequip)
admin.site.register(vetrequest)
admin.site.register(vetreply)
admin.site.register(vetsession)
admin.site.register(equiprental)
admin.site.register(forum)