from django.contrib import admin

from appblog.models import Article,CustomUser,Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(CustomUser)
