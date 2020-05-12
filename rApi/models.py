from django.db import models

# Create your models here.

class User(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=50)
    age = models.IntegerField()
    image = models.ImageField(upload_to="rApi/images", default="")

    def __str__(self):
        return f"{self.emp_name} {self.emp_id}"
