from django.urls import path
from organisation.views.organisations import *
from organisation.views.geoobjects import *


urlpatterns = [
    # ORGANISATION
    path('mypage/manage/',PageMyView.as_view(),name='page' ),
    # EMPLOYEE
    path('mypage/manage/employees/',EmployeeView.as_view(),name='employee' ),
    path('mypage/manage/employee/<int:pk>',EmployeeRetrieveView.as_view(),name='retr_employee' ),
    # GROUP
    path('mypage/groups/',GroupListCreateView.as_view(),name='groups' ),
    path('mypage/group/<int:pk>',GroupRetriveView.as_view(),name='retr_group' ),
    # GEOMETRY
    path('mypage/group/<int:id_group>/geometrys',GeometryListCreateView.as_view(),name='geometry' ),
    # path('mypage/group/<int:pk>/geometrys/list/',GeometryListCreateView.as_view(),name='geometry' ),
    
    path('mypage/group/<int:id_group>/geometrys/<int:pk>',GeometryRetrieveView.as_view(),name='retr_geometry' ),


]
