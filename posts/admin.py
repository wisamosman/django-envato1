from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from .models import Post,Review


class SomeModelAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'

admin.site.register(Post,SomeModelAdmin)
admin.site.register(Review)
# Register your models here.
