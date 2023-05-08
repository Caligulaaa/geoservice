from django.contrib import admin

from user.models.users import User 
# Register your models here.
#######################################
# USER
#####################################
@admin.register(User)
class OMyUserAdmin(admin.ModelAdmin):
    pass