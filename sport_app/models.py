from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class SportSection(models.Model):
    name = models.TextField()
    info = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='C:/Users/Karim/PycharmProjects/sport/sport_app/templates/img', blank=True)

    def __str__(self):
        return "name = {0}, info = {1}, price = {2}".format(self.name, self.info, self.price)


class Location(models.Model):
    location = models.TextField()
    map_location = models.TextField()
    section_id = models.ForeignKey(SportSection, on_delete=models.PROTECT)

    def __str__(self):
        return "location = {0}, map_location = {1}, section_id = {2}".format(self.location, self.map_location,
                                                                             self.section_id)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(SportSection, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return "user_id = {0}, section_id = {1}, rating = {2}".format(self.user_id, self.section_id, self.rating)


class Review(models.Model):
    section_id = models.ForeignKey(SportSection, on_delete=models.CASCADE)
    review = models.TextField()

    def __str__(self):
        return "section_id = {0}, review = {1}".format(self.section_id_id, self.review)
