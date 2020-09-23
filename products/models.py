from django.db import models

# Create your models here.

# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/<user_id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.id, filename)


class Proizvod(models.Model):
    Naziv = models.CharField(max_length = 40)
    Slika = models.FileField(upload_to = 'proizvods/')

class PodProizvod(models.Model):
    ProizvodId = models.ForeignKey(Proizvod, on_delete = models.CASCADE)
    Ime = models.CharField(max_length = 40)
