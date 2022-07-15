from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=125, null=True, blank=True)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=124, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name