from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
import uuid
from django.contrib.auth.mixins import LoginRequiredMixin

from PIL import Image

class Books(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  cover = models.ImageField(upload_to='covers/', blank=True)

  class Meta:
    verbose_name_plural = "Books"

  def __str__(self):
    return self.title

  def get_absolute_url(self):
      return reverse("book_detail", args=[str(self.id)])
  
  def save(self, *args, **kwargs):
    super(Books, self).save(*args, **kwargs)
    
    img = Image.open(self.cover.path)  # opens the image of current instance
    
    if img.height > 400 and img.width > 400:
      output_size = (400, 400)
      img.thumbnail(output_size)
      img.save(self.cover.path)

class Review(models.Model):
  book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='reviews')
  review = models.CharField(max_length=255)
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  def __str__(self):
      return self.review
    

