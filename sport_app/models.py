from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TrainingSystem(models.Model):
    name = models.TextField()
    info = models.TextField()

    def __str__(self):
        return "name = {0}, info = {1}".format(self.name, self.info)


class Coach(models.Model):
    name = models.TextField()
    info = models.TextField()
    img = models.ImageField(upload_to='C:/Users/Karim/PycharmProjects/sport/static/img', blank=True)

    def __str__(self):
        return "name = {0}, info = {1}".format(self.name, self.info)


#
# class ReviewToCoach(models.Model):
#     coach_id = models.ForeignKey(Coach, on_delete=models.CASCADE)
#     review_text = models.TextField()
#
#     def __str__(self):
#         return "coach_id = {0}, review_text = {1}".format(self.coach_id, self.review_text)


class SportSection(models.Model):
    name = models.TextField()
    info = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='C:/Users/Karim/PycharmProjects/sport/static/img', blank=True)

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
    conn_id = models.IntegerField()
    comment = models.TextField()
    typeComment = models.ForeignKey(TypeComment, on_delete=models.CASCADE)

    def __str__(self):
        return "section_id = {0}, review = {1}".format(self.conn_id, self.comment)


class Food(models.Model):
    name = models.TextField()
    desc = models.TextField()

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
