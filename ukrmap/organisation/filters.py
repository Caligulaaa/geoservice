from django.db.models import Q
from rest_framework.filters import BaseFilterBackend
from crum import get_current_user


class MyEmployee(BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        user = request.user
        return queryset.filter(
            page__employees=user
            )


class OwnedByOrganisation(BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        org_id = request.parser_context['kwargs'].get('id_organisation')
        return queryset.filter(organisation_id=org_id)
    


class MyOrganisation(BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        user = request.user
        return queryset.filter(
            Q(admin=user) | Q(employees=user)
            )
    
    
class MyGroup(BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        user = request.user
        return queryset.filter(
            Q(page__admin=user) | Q(page__employees=user)
            )