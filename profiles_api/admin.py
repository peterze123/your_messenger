from django.contrib import admin

from profiles_api import models

admin.site.register(models.userInfo)
admin.site.register(models.profileFeed)
admin.site.register(models.articles)