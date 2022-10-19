from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _ 


class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password, **kwargs):
        if not username:
            raise ValidationError(_("User must have a username"))

        if not email:
            raise ValidationError(_("User must have a email"))

        if not first_name:
            raise ValidationError(_("User must have a first name"))

        if not last_name:
            raise ValidationError(_("User must have a last name"))
        
        if not password: 
            raise ValidationError(_("User must have a password"))

        email = self.normalize_email(email)
        user = self.model(username=username, first_name=first_name, last_name=last_name, email=email, **kwargs)
        user.set_password(password)
        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_superuser", False) 
        user.save()
        return user 

    def create_superuser(self, username, email, first_name, last_name, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True) 
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is not True: 
            raise ValidationError(_("Superuser must be staff"))

        if kwargs.get("is_active") is not True: 
            raise ValidationError(_("Superuser must be active"))

        if kwargs.get("is_superuser") is not True: 
            raise ValidationError(_("Superuser must have is_superuser=True"))

        email = self.normalize_email(email)
        user = self.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user 

    