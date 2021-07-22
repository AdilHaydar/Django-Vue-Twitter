from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

def upload_to(instance, filename):
    username = instance.user.username
    return '%s/%s/%s' %('profilePhoto',username,filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=120, null=False, blank=False)
    bio = models.CharField(max_length=300, blank=True, null=True)
    sehir = models.CharField(max_length=120, blank=True, null=True)
    foto = models.ImageField(null=True, blank=True, upload_to=upload_to)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.foto:
            img = Image.open(self.foto.path)
            output_size = (48,48)
            img.thumbnail(output_size)
            img.save(self.foto.path)

    def __str__(self):
        return self.user.username
