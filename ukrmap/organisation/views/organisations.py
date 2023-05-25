
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view,extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from organisation.models.organisations import *
from organisation.serializers.organisations import pages,groups,employees
from drf_spectacular.utils import extend_schema_view,extend_schema

from organisation.permissions import IsMyOrganisation,IsColleagues,IsMyGroups
from django.db.models import Count

from organisation.filters import MyOrganisation,OwnedByOrganisation,MyGroup,MyEmployee
################################
## PAGE VIEW
###############################
@extend_schema_view(get=extend_schema(summary='my page',tags=['Page']),)
class PageMyView(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = pages.PageMySerializer
    permission_classes = [IsMyOrganisation,]
    pagination_class = None

    filter_backends = (
        MyOrganisation,
    )


###############################
## GROUP
#################################
@extend_schema_view(get=extend_schema(description='informations about group get',summary='all groups',tags=['Groups']),
                    post=extend_schema(summary='create group',tags=['Groups']),)
class GroupListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = groups.GroupListSerializer
    permission_classes = [IsMyGroups,]
    pagination_class = None

    filter_backends = (
        MyGroup,
        DjangoFilterBackend,

    )
    filterset_fields = ('name',)
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return groups.GroupListSerializer
        return groups.GroupCreateSerializer

@extend_schema_view(get=extend_schema(summary='one group',tags=['Groups']),
                    patch=extend_schema(summary='update group',tags=['Groups']),
                    delete=extend_schema(summary='delete group',tags=['Groups']),
                    )
class GroupRetriveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    # serializer_class = OrganisationSerializer
    permission_classes = [IsMyGroups,]
    pagination_class = None
    http_method_names = ('get','patch','delete')

    filter_backends = (
        MyGroup,
    )

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return groups.GroupUpdateSerializer
        return groups.GroupListSerializer
    
################################
#   EMPLOYEE
###############################
@extend_schema_view(post=extend_schema(summary='create employee',tags=['employee']),
                    get=extend_schema(summary='list employee',tags=['employee']),
                    )
class EmployeeView(generics.ListCreateAPIView):
    permission_classes = [IsColleagues]

    queryset = Employee.objects.all()
    serializer_class = employees.OrganisationEmployeeListSerializer

    pagination_class = None

    
    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return employees.OrganisationCreateEmployeeSerializer
        return employees.OrganisationEmployeeListSerializer
        
    filter_backends = (
        MyEmployee,
    )

    def get_queryset(self):
        queryset = Employee.objects.select_related(
            'user'
            )
        return queryset
    
@extend_schema_view(get=extend_schema(summary='get employee',tags=['employee']),
                    patch=extend_schema(summary='update employee',tags=['employee']),
                    delete=extend_schema(summary='delete employee',tags=['employee']),
                    )
class EmployeeRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = employees.OrganisationEmployeeRetriverSerializer
    permission_classes = [IsColleagues,]#IsColleagues
    pagination_class = None
    http_method_names = ('get','patch','delete')
    
    filter_backends = (
        MyEmployee,
    )

    def get_serializer_class(self):
        if self.request.method in ['PATCH']:
            return employees.OrganisationEmployeeUpdateSerializer
        return employees.OrganisationEmployeeListSerializer
    
    # lookup_field = 'user_id'
    # lookup_url_kwargs = 'employee_id'
    # def get_queryset(self):
    #     user_id = self.kwargs['user_id']
    #     return Employee.objects.filter(user=user_id)