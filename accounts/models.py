from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from utiles.generate_code import genrate_code

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile_user', on_delete=models.CASCADE)
    image = models.ImageField( upload_to='profile' ,blank=True, null=True)
    phone_num = models.CharField( max_length=100, blank=True, null=True)
    address = models.CharField( max_length=200, blank=True, null=True)
    code = models.CharField( max_length=8 ,default=genrate_code)

    def __str__(self):
        return str(self.user)

@receiver(post_save,sender=User)
def profile_signal(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user = instance ,
        )



