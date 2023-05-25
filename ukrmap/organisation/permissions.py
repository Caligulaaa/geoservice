from rest_framework.permissions import BasePermission,SAFE_METHODS, IsAuthenticated
import pdb

class OrganisationMixin(IsAuthenticated):
    def has_permission(self, request,view):
        try:
            user = request.user
            if user.is_anonymous:
                return False
            
            if user.role == 'admin':
                return True
            
            return False
        except KeyError:
            return True
        
class IsMyOrganisation(BasePermission):

    message = ("you have not corporate account,write to admin")

    def has_object_permission(self, request,view,obj):
        
        if obj.admin == request.user:

            return True
        
        # if request.method in SAFE_METHODS:
        #     return request.user in obj.employees.all()

        return False
    

class IsColleagues(OrganisationMixin):
    message = ("you have not perm to account")

    def has_object_permission(self, request, view, obj):

        if obj.page.admin == request.user or obj.page.employees.user.role == 'admin':
            return True

        # if request.method in SAFE_METHODS:
        #     return request.user in obj.page.employees.all()
        return False



        
class IsMyGroups(IsAuthenticated):

    message = ("you have not permissions to account,write to admin")

    def has_permission(self, request,view):
        role = ('admin','manager')
        try:
            user = request.user
            if user.is_anonymous:
                print(1)
                return False
            
            if user.role in role:
                print(2)
                return True
            
            if request.method in SAFE_METHODS:
                print(3)
                return True
            return False
        except KeyError:
            return True

    def has_object_permission(self, request,view,obj):
        role = ('admin','manager')
        print(request.user)
        if obj.page.admin == request.user:
            print(1)
            return True
        
        if request.user in obj.page.employees.all() and request.user.role in role:
            print(2)
            return True
        
        if request.method in SAFE_METHODS:
            print(3)
            return request.user in obj.page.employees.all()
        
        # if request.method in SAFE_METHODS:
        #     return obj.organisation.employees.all(user=request.user).exists()


        return False
    
class IsGroupGeometry(IsAuthenticated):

    message = ("you have not permissions to account,write to admin")

    def has_permission(self, request,view):
        role = ('admin','manager')
        
        try:
            user = request.user
            group_id = request.parser_context['kwargs'].get('id_group')
            
            if user.is_anonymous:
                return False
            
            if user.page_employees.first().group_page.filter(id=group_id) and user.role in role:
                return True
            
            if user.page_employees.first().group_page.filter(id=group_id) and request.method in SAFE_METHODS:
                return True

                        
            return False
        except KeyError:
            return True

    def has_object_permission(self, request,view,obj):
        role = ('admin','manager')
        
        if obj.info.group.page.admin == request.user:
            print(1)
            return True
        
        if request.user in obj.info.group.page.employees.all() and request.user.role in role:
            print(2)
            return True
        
        if request.method in SAFE_METHODS:
            print(3)
            return request.user in obj.info.group.page.employees.all()
        
        # if request.method in SAFE_METHODS:
        #     return obj.organisation.employees.all(user=request.user).exists()


        return False