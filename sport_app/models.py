from django.db import models

# Create your models here.


class SportSection(models.Model):
    name = models.TextField()
    info = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return "name = {0}, info = {1}, price = {2}".format(self.name, self.info, self.price)


class Location(models.Model):
    location = models.TextField()
    map_location = models.TextField()
    section_id = models.ForeignKey(SportSection)

    def __str__(self):
        return "location = {0}, map_location = {1}, section_id = {2}".format(self.location, self.map_location, self.section_id.__str__())
