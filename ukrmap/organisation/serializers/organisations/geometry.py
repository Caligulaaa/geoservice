from rest_framework import serializers
import pdb
from django.db import transaction
from organisation.serializers.mixins import GeoInfoMixin


from rest_framework_gis.serializers import GeoFeatureModelSerializer
from organisation.models.geoobjects import GeoInfo,GeoObject
from organisation.models.organisations import Group

####################
#   LIST GEOMETRY
#####################
class GeometryListSerializer(GeoFeatureModelSerializer):
    info = GeoInfoMixin()
    class Meta:
        model = GeoObject
        geo_field = "geometry"
        id_field=False
        # auto_bbox = True
        # bbox_geo_field = 'bbox_geometry'
        fields = ('id','info',)

########################
#   CREATE GEOMETRY
#######################
class GeometryCreateSerializer(GeoFeatureModelSerializer):
    # group = serializers.IntegerField(write_only=True)
    # name = serializers.CharField(write_only=True)
    # description = serializers.CharField(write_only=True)
    info = GeoInfoMixin()
    class Meta:
        model = GeoObject
        geo_field = "geometry"
        id_field=False
        # auto_bbox = True
        # bbox_geo_field = 'bbox_geometry'
        # fields = ('group','name','description',)
        fields = ('info',)


    def create(self, validated_data):
        with transaction.atomic():
            # group_name = Group.objects.filter(
            #     id=self.context['view'].kwargs.get('pk')).first()
        
            group_name = Group.objects.filter(
                id=34).first()
        

        #     # # pdb.set_trace()
        #     # if not group_name:
        #     #     raise serializers.ValidationError({"error": "group not found"})

            geoinfo = GeoInfo.objects.create(
                group = group_name,
                description = validated_data['info']['description'],
                name = validated_data['info']['name']
                )
            geoinfo.save()
            print(validated_data['geometry'])
            geoobject = GeoObject.objects.create(info=geoinfo,geometry=validated_data['geometry'])
        return geoobject
