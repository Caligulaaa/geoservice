from django.db import models
from user.models.users import User
from .mixins import InfoMixin
from django.utils import timezone

#################################
# PAGE TO REGISTER
################################
class Page(InfoMixin):
    admin = models.OneToOneField(User,on_delete=models.CASCADE,related_name='page_admin',verbose_name='ADMIN')
    employees = models.ManyToManyField(User,related_name='page_employees',
                                       verbose_name='employees',  #    передавать значенния пустой строки

                                    #    передавать значенния пустой строки
                                       blank=True,through="Employee"
                                    #  null - true зберігати дані в бд тру дозволяє пустоту в бд
                                       )
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
        ordering = ('admin',)
        

    def __str__(self):
        return str(self.admin.username)

###############################################
## EMPLOYEES
###############################################
class Employee(models.Model):
    page = models.ForeignKey(Page,on_delete=models.CASCADE,related_name='employee_info')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='organisation_info')
    # position = models.ForeignKey(Position,on_delete=models.RESTRICT,related_name='employee_position')
    date_join = models.DateField('date join',default=timezone.now)
    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'
        ordering = ('-date_join',)
        unique_together = (('page','user'),)

    def __str__(self):
        return f"employee..{self.user.username}"
    
##################################
#   GROUPS
##################################
class Group(InfoMixin):
    page = models.ForeignKey(Page,on_delete=models.CASCADE,related_name='group_page')   
    name = models.CharField('Name',max_length=30)
    # polygon mtm


    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        ordering = ('name',)

    def __str__(self):
        return self.name
    