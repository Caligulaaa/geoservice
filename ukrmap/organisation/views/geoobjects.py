from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view,extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser

from drf_spectacular.utils import extend_schema_view,extend_schema

from organisation.models.geoobjects import GeoObject
from organisation.serializers.organisations import geometry

from organisation.permissions import IsMyOrganisation,IsColleagues,IsMyGroups

from organisation.filters import MyOrganisation,OwnedByOrganisation,MyGroup,MyEmployee

@extend_schema_view(get=extend_schema(summary='all Geometry',tags=['Geometry']),
                    post=extend_schema(summary='create Geometry',tags=['Geometry']),)
class GeometryListCreateView(generics.ListCreateAPIView):
    queryset = GeoObject.objects.all()
    serializer_class = geometry.GeometryListSerializer
    permission_classes = [AllowAny,]
    pagination_class = None

    # filter_backends = (
    #     MyGroup,
    #     DjangoFilterBackend,

    # )
    # filterset_fields = ('name',)
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return geometry.GeometryListSerializer
        return geometry.GeometryCreateSerializer
