from django.db import models
from django.utils import timezone
from user.models.users import User
from crum import get_current_user
import pdb

class DateMixin(models.Model):
    created_at = models.DateTimeField(verbose_name='create_at',null=True)
    updated_at = models.DateTimeField(verbose_name='update_at',null=True)

    class Meta:
        abstract = True

    def save(self,*args,**kwargs):
        if not self.pk and not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(DateMixin,self).save(*args,**kwargs)
    
class InfoMixin(DateMixin):
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,
        related_name='created_%(app_label)s_%(class)s',verbose_name='create_by',null=True)
    update_by = models.ForeignKey(User,on_delete=models.SET_NULL,
        related_name='updated_%(app_label)s_%(class)s',verbose_name='update_by',null=True)
    class Meta:
        abstract = True

    def save(self,*args,**kwargs):


        user = get_current_user()

        # pdb.set_trace()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.update_by = user
        super().save(*args,**kwargs)