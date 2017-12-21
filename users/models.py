from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.storage import ImageStorage

# Create your models here.
class User(AbstractUser):
    face_img = models.ImageField(upload_to='img/face/%Y/%m/%d', storage=ImageStorage(), verbose_name='上传头像')

    class Meta(AbstractUser.Meta):
        pass
