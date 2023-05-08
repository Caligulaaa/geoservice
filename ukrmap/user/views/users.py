from user.models.users import User
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view,extend_schema
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView,ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from user.serializers import users

@extend_schema_view(post=extend_schema(summary='user register',tags=['login & logout']),)
class RegistrationView(CreateAPIView):
    queryset=User.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = users.RegistrationSerializer

@extend_schema_view(
    post=extend_schema(
        request = users.ChangePasswordSerializer,
        summary='change pass',tags=['login & logout']),
        )
class ChangePassView(APIView):
    permission_classes = [IsAuthenticated,]
    # http_method_names = ('post')

    def post(self,request):
        user = request.user
        serializer = users.ChangePasswordSerializer(
            instance = user,data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@extend_schema_view(
    get=extend_schema(summary='user profile',tags=['Profile']),
    patch=extend_schema(summary='litle change profile',tags=['Profile']),
    )
class MeView(RetrieveUpdateAPIView):
    queryset=User.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = users.MeListSerializer
    http_method_names = ('get','patch')

    def get_serializer_class(self):
        # if self.request.method in ['PATCH']:
        #     return users.MeUpdateSerializer
        return users.MeListSerializer
    def get_object(self):
        return self.request.user
    
#############################################
## ALL USERS
#############################################
@extend_schema_view(get=extend_schema(summary='all users',tags=['App Dict']),)
class UsersView(ListAPIView):
    queryset=User.objects.all()
    permission_classes = [IsAdminUser,]
    serializer_class = users.UserListSerializer
    pagination_class = None