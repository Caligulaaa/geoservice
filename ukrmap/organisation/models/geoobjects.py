from django.contrib.gis.geos import MultiPolygon
from django.db import models
from organisation.models.organisations import Group
from django.contrib.gis.db import models as GeoModels
from organisation.models.mixins import InfoMixin

class GeoInfo(InfoMixin):
    group = GeoModels.ForeignKey(Group,on_delete=GeoModels.CASCADE,related_name='group_page')
    name = GeoModels.CharField('name',max_length=30)
    description = GeoModels.TextField(null=True,blank=True)

    is_active = GeoModels.BooleanField('is active',blank=True,default=True)


    def __str__(self):
        return str(self.name)

class GeoObject(GeoModels.Model):
    info = GeoModels.OneToOneField(GeoInfo,on_delete=GeoModels.CASCADE,related_name='geoObject_info')

    geometry = GeoModels.GeometryField('geometry')

    class Meta:
        verbose_name = 'geoObject'
        verbose_name_plural = 'geoObjects'
        ordering = ('info__group',)

    def __str__(self):
        return str(self.info.name) + " - " + str(self.info.group.name)