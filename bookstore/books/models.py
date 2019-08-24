from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/book_images/book_name/<filename>
    return 'book_images/{0}'.format(instance.book_name)

class book(models.Model):
	book_name=models.CharField(max_length=100)
	author_name=models.CharField(max_length=50)
	published_date=models.DateField(null=True)
	publisher=models.CharField(max_length=100)
	Category=models.CharField(max_length=100)
	book_description=models.CharField(max_length=1000)
	book_image=models.ImageField(upload_to=user_directory_path,blank=True)