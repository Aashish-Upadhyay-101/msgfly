from django.db import models
from msgfly.settings import AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _ 
from django.dispatch import receiver
from django.db.models.signals import post_save 


User = get_user_model()

class Profile(models.Model):

    class Gender(models.TextChoices):
        MALE = "Male", _("Male")
        FEMALE = "Female", _("Female")
        OTHER = "Other", _("Other")

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    about_me = models.TextField(verbose_name=_("About me"), max_length=256)
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, default=Gender.OTHER, max_length=10)


    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


