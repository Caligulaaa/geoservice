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

####################
#   RETRIVE GEOMETRY
#####################
class GeometryRetriveSerializer(GeoFeatureModelSerializer):
    info = GeoInfoMixin()
    class Meta:
        model = GeoObject
        geo_field = "geometry"
        id_field=False
        fields = ('id','info',)

########################
#   CREATE GEOMETRY
#######################
class GeometryCreateSerializer(GeoFeatureModelSerializer):
    info = GeoInfoMixin()
    class Meta:
        model = GeoObject
        geo_field = "geometry"
        id_field=False
        # auto_bbox = True
        # bbox_geo_field = 'bbox_geometry'
        # fields = ('group','name','description',)
        fields = ('id','info',)


    def create(self, validated_data):
        group_id =self.context['view'].kwargs.get('id_group')
        with transaction.atomic():
            group_name = Group.objects.filter(
                id=group_id).first()

            if not group_name:
                raise serializers.ValidationError({"error": "group not found"})

            geoinfo = GeoInfo.objects.create(
                group = group_name,
                description = validated_data['info']['description'],
                name = validated_data['info']['name']
                )
            geoinfo.save()
            geoobject = GeoObject.objects.create(info=geoinfo,geometry=validated_data['geometry'])
        return geoobject
    
########################
#   UPDATE GEOMETRY
#######################
class GeometryUpdateSerializer(GeoFeatureModelSerializer):
    info = GeoInfoMixin()
    class Meta:
        model = GeoObject
        geo_field = "geometry"
        id_field=False
        # auto_bbox = True
        # bbox_geo_field = 'bbox_geometry'
        # fields = ('group','name','description',)
        fields = ('info',)


    def update(self, validated_data):
        info_data = validated_data.pop('info') if 'info' in validated_data else None
        with transaction.atomic():
            instance = super().update(instance,validated_data)

            if info_data:
                info = instance.info

                geometry_serializer = GeoInfoMixin(instance=info,
                                                    data=info_data,
                                                    partial=True) # дозволено частковий апдейт
                geometry_serializer.is_valid(raise_exception=True)
                geometry_serializer.save()

        return instance
