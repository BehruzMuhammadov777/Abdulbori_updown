from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminService(admin.ModelAdmin):
    list_display = ['id', 'nomi', 'eski_narxi', 'yangi_narxi', 'manzil', 'xonalar', 'rasm', 'vaqt']

admin.site.register(Service,AdminService)




class AdminClients(admin.ModelAdmin):
    list_display = ['id', 'ismi', 'fam', 'malumot', 'lavozimi', 'rasmi']

admin.site.register(Clients,AdminClients)





class AdminAgents(admin.ModelAdmin):
    list_display = ['id', 'ismi', 'fami', 'lavozimi', 'rasm']

admin.site.register(Agents,AdminAgents)






class AdminBlogs(admin.ModelAdmin):
    list_display = ['id', 'nomi',  'maydoni', 'rasm', 'malumot', 'vaqt']

admin.site.register(Blogs,AdminBlogs)





class AdminMurojat(admin.ModelAdmin):
    list_display = ['id', 'name',  'mail', 'subject', 'messege', 'vaqt']

admin.site.register(Murojat, AdminMurojat)
