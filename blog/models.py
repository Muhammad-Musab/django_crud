import uuid
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
# Create your models here.
class blog(models.Model):
    uuid = models.UUIDField(unique=True, default = uuid.uuid4, editable=False)
    title = models.CharField(max_length=20)
    author = models.ForeignKey(
        'auth.user',
        on_delete= models.CASCADE,
    )
    post = models.TextField(blank=False)
    
    def __str__(self):
        return self.title.Capatilalize
    def get_absolute_url(self):
        return reverse("detail-page", kwargs={"pk": self.pk})
     