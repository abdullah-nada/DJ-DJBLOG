from django.contrib import admin
from .models import Post,Category,Comments
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','draft']
    list_filter = ['draft',]
    search_fields = ['title']

 

admin.site.register(Post,ProductAdmin) 
admin.site.register(Category)
admin.site.register(Comments)