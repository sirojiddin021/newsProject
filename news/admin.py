from django.contrib import admin
from news.models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Bookmark)
admin.site.register(Category)