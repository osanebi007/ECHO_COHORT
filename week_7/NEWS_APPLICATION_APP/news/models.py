from django.db import models
from users.models import User

# Create your models here.
class News(models.Model):
    author = models.ForeignKey(User, related_name="news_course", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    # cover_image = models.FileField(upload_to='media/')
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name="new_likes") 
    created_at = models.DateTimeField(auto_now_add=True)