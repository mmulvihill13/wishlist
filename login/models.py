from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

#Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    
    order_count = models.PositiveIntegerField(default=0)
    free_drinks_avail = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user} Profile.'
    
    def increment_order_count(self): #ana- add to free drinks after 10
        self.order_count += 1
        if self.order_count % 10 == 0:
            self.free_drinks_available += 1
        self.save()
            
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            Profile.objects.create(user=instance, phone_number=None)
        else:
            Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()