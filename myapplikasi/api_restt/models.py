from django.db import models

# Create your models here.

class Personal(models.Model):
    pid     = models.CharField(max_length=30)
    nama    = models.CharField(max_length=40)
    alamat  = models.CharField(max_length=50)
    Pass    = models.CharField(max_length=30)

    class Meta:
        db_table =  "personal"

    def __str__(self):
        return"{}".format(self.nama)