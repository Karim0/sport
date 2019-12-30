from django.db import models
from django.contrib.auth.models import User, AbstractUser
from sport import settings


# Create your models here.

class Coach(models.Model):
    name = models.TextField()
    info = models.TextField()
    img = models.ImageField(upload_to=settings.MEDIA_ROOT + '/img', blank=True)

    def __str__(self):
        return "name = {0}, info = {1}".format(self.name, self.info)


class TrainingSystem(models.Model):
    name = models.TextField()
    info = models.TextField()
    aim = models.TextField(null=True)
    time = models.TextField(null=True)
    cycle_duration = models.TextField(null=True)
    workouts_per_week = models.TextField(null=True)
    video = models.TextField(null=True)
    level = models.TextField(null=True)
    location = models.TextField(null=True)
    img = models.ImageField(upload_to=settings.MEDIA_ROOT + '/img', blank=True)

    def __str__(self):
        return "name = {0}, info = {1}".format(self.name, self.info)


class SportSectionType(models.Model):
    img = models.ImageField(upload_to=settings.MEDIA_ROOT + '/img', blank=True)
    description = models.TextField(max_length=56)

    def __str__(self):
        return self.description


class SportSection(models.Model):
    type = models.ForeignKey(SportSectionType, on_delete=models.CASCADE, null=True)
    name = models.TextField()
    info = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to=settings.MEDIA_ROOT + '/img', blank=True)

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


class TypeComment(models.Model):
    name = models.TextField()

    def __str__(self):
        return "name = {0}".format(self.name)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    conn_id = models.IntegerField()
    comment = models.TextField()
    typeComment = models.ForeignKey(TypeComment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "section_id = {0}, review = {1}".format(self.conn_id, self.comment)


class Food(models.Model):
    name = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to=settings.MEDIA_ROOT + '/img', blank=True)

    def __str__(self):
        return "name = {0}, description = {1}".format(self.name, self.desc)


class Achievement(models.Model):
    name = models.TextField()
    desc = models.TextField()

    def __str__(self):
        return "name = {0}, description = {1}".format(self.name, self.desc)


class Reward(models.Model):
    name = models.TextField()
    desc = models.TextField()

    def __str__(self):
        return "name = {0}, description = {1}".format(self.name, self.desc)


class Order(models.Model):
    name = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
