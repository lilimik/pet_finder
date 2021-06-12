from django.contrib import admin

from users.models import CustomUser, Pet, FinderFormsModel

admin.site.register(CustomUser)
admin.site.register(Pet)
admin.site.register(FinderFormsModel)
