from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

from bknd.spectaculars.urls import urlpatterns as doc_urls
# from map.urls import urlpatterns as map_urls
# from statistic.urls import urlpatterns as statistic_url
from organisation.urls import urlpatterns as organisation_url
from user.urls import urlpatterns as user_url

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

urlpatterns += doc_urls
# urlpatterns += map_urls
# urlpatterns += statistic_url
urlpatterns += organisation_url
urlpatterns += user_url