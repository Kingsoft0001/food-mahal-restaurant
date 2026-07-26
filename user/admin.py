from django.contrib import admin
from .models import *

# Register your models here.
class tblcontactAdmin(admin.ModelAdmin):
    list_display=("id","name","mobile","email","message")

admin.site.register(tblcontact,tblcontactAdmin)

class tblgalleryAdmin(admin.ModelAdmin):
    list_display=("id","title","picture")

admin.site.register(tblgallery,tblgalleryAdmin)

class tblteamAdmin(admin.ModelAdmin):
    list_display=("id","name","picture","about_chef")

admin.site.register(tblteam,tblteamAdmin)

class tblcategoryAdmin(admin.ModelAdmin):
    list_display=("id","category_name","category_picture")

admin.site.register(tblcategory,tblcategoryAdmin)

class tbl_bookingAdmin(admin.ModelAdmin):
    list_display=("id","customer_name","mobile","email","no_of_people","amount","message","date","booking_date","time","address")    

admin.site.register(tbl_booking,tbl_bookingAdmin)

class tblproductAdmin(admin.ModelAdmin):
    list_display=("id","category","name","price","discounted_price","description","picture","added_date")

admin.site.register(tblproduct,tblproductAdmin)

class tbl_feedbackAdmin(admin.ModelAdmin):
    list_display=("id","name","email","message","picture")

admin.site.register(tbl_feedback,tbl_feedbackAdmin)