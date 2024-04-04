from django.contrib import admin
from django.utils.html import format_html
from django.utils.html import mark_safe
from .models import Data_movie
from .models import Data_list
from .models import Category



class Data_movie_Admin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['status_list']
    list_display = ('id','display_image','name', 'category' ,'status_list') # display_image ได้มาจาก image ใน models.py ที่เป็นชื่อเก่าของฟิลด์รูปภาพ ถ้าใช้ชื่อปัจจุบันจะบัคไม่แสดงรูปในหน้า admin 
    
    def display_image(self, obj):
        return format_html('<img src="{0}" width="110px" height="150px">'.format(obj.image.url))
    
class Data_list_Admin(admin.ModelAdmin):
    search_fields = ['name']
    raw_id_fields = ('main_id',) # แสดงผล main_id เป็นแบบกรอก id เอง 
    list_display = ('movie_id','display_image','name','part')

    # แสดง id ของ Data_movie
    def movie_id(self, obj):
        return f"{obj.main_id.id}"
    
    # แสดง image ของ Data_movie
    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.main_id.image.url}" width="110px" height="150px" />')

admin.site.register(Data_movie, Data_movie_Admin)
admin.site.register(Data_list, Data_list_Admin)
admin.site.register(Category)