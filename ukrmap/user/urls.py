from django.urls import path
from user.views.users import RegistrationView,ChangePassView,MeView,UsersView


urlpatterns = [
    path('user/register/',RegistrationView.as_view(),name='registr' ),
    path('user/change-pass/',ChangePassView.as_view(),name='change_password'),
    path('user/me/',MeView.as_view(),name='Me_user'),
    path('user/all/',UsersView.as_view(),name='all_users'),

]

