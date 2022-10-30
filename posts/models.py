from django.db import models
import uuid
from users.models import Profile


# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField()
    # featured_image = models.ImageField(
    #     null=True, blank=True)
    # location
    # prices
    # demo_link = models.CharField(max_length=2000, null=True, blank=True)
    # source_link = models.CharField(max_length=2000, null=True, blank=True)
    # tags = models.ManyToManyField('Tag', blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title
