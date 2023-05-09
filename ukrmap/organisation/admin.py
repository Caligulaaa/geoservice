from django.contrib import admin


from organisation.models.organisations import *
from organisation.models.geoobjects import GeoObject,GeoInfo


#########################################
class EmployeeInline(admin.TabularInline):
    model = Employee
    fields = ('user','date_join') 


############################################
# MODELS
#########################################
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id','admin',)
    inlines = (EmployeeInline,)
    readonly_fields = ('created_at','created_by','updated_at','update_by','admin')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    readonly_fields = ('created_at','created_by','updated_at','update_by')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

#######################################
##  GEOMETRY + INFO
#######################################
@admin.register(GeoObject)
class GeoObjectAdmin(admin.ModelAdmin):
    # readonly_fields = ('created_at','created_by','updated_at','update_by')
    pass

# INFO
@admin.register(GeoInfo)
class GeoInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','created_by','updated_at','update_by')