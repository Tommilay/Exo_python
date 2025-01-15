from django.db import models

class Book(models.Model):
    class Genre(models.TextChoices):
        Romance = "R"
        Fiction = "F"
        Horreur = "H"
        Fantastique = "Fa"
        Dramatique = "D"
    titre = models.fields.CharField(max_length=100)
    auteur = models.fields.CharField(max_length=100)
    date_d_edition = models.fields.DateField()
    genre = models.fields.CharField(max_length=50)

    def __str__(self):
        return f"{self.titre}"

    