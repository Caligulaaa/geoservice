from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view,extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser

from drf_spectacular.utils import extend_schema_view,extend_schema

from organisation.models.geoobjects import GeoObject
from organisation.serializers.organisations import geometry

from organisation.permissions import IsGroupGeometry

from organisation.filters import GeometrysForGroup,MyGeometryGroup

@extend_schema_view(get=extend_schema(summary='all Geometry',tags=['Geometry']),
                    post=extend_schema(summary='create Geometry',tags=['Geometry']),)
class GeometryListCreateView(generics.ListCreateAPIView):
    queryset = GeoObject.objects.all()
    serializer_class = geometry.GeometryListSerializer
    permission_classes = [IsGroupGeometry,]
    pagination_class = None

    filter_backends = (
        GeometrysForGroup,
        MyGeometryGroup,
    )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return geometry.GeometryListSerializer
        return geometry.GeometryCreateSerializer
    
### RETRIVE
@extend_schema_view(get=extend_schema(summary='retrive Geometry',tags=['Geometry']),
                    patch=extend_schema(summary='update Geometry',tags=['Geometry']),
                    delete=extend_schema(summary='delete Geometry',tags=['Geometry']),
                    )
class GeometryRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeoObject.objects.all()
    serializer_class = geometry.GeometryRetriveSerializer
    permission_classes = [IsGroupGeometry,]
    pagination_class = None
    http_method_names = ('get','patch','delete')

    filter_backends = (
        GeometrysForGroup,
        MyGeometryGroup,
    )
    def get_serializer_class(self):
        if self.request.method in ['PATCH']:
            return geometry.GeometryUpdateSerializer
        return geometry.GeometryRetriveSerializer