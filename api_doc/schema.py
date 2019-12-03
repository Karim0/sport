import coreapi
from rest_framework.schemas import AutoSchema
from django import forms


class SportSectionSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ["post", "put"]:
            extra_fields = [
                coreapi.Field('name', type='string', location='query', description='name'),
                coreapi.Field('info', type='string', location='query', description='info'),
                coreapi.Field('price', type='integer', location='query', description='price'),
                coreapi.Field('img', type='file', location="formData", description='img')
            ]

            manual_fields = super().get_manual_fields(path, method)
            return manual_fields + extra_fields


class CommentSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ["post", "put"]:
            extra_fields = [
                # coreapi.Field('user_id', type='long', location='query', description='user_id'),
                coreapi.Field(name='conn_id', type='integer', description='section_id'),
                coreapi.Field(name='comment', type='string', description='comment'),
                coreapi.Field(name='typeComment', type='integer', description='typeComment'),
            ]

            manual_fields = super().get_manual_fields(path, method)
            return manual_fields + extra_fields


class LocationSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ["post", "put"]:
            extra_fields = [
                coreapi.Field('section', type='integer', description='section_id'),
                coreapi.Field('location', type='string', description='address'),
                coreapi.Field('map_location', type='string', description='map lat and lon'),
            ]

            manual_fields = super().get_manual_fields(path, method)
            return manual_fields + extra_fields


class RatingSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ["post", "put"]:
            extra_fields = [
                coreapi.Field('user', type='integer', description='user_id'),
                coreapi.Field('section', type='integer', description='section_id'),
                coreapi.Field('rating', type='integer', description='rating'),
            ]

            manual_fields = super().get_manual_fields(path, method)
            return manual_fields + extra_fields


class CoachSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ["post", "put"]:
            extra_fields = [
                coreapi.Field('user', type='integer', description='user_id'),
                coreapi.Field('section', type='integer', description='section_id'),
                coreapi.Field('rating', type='integer', description='rating'),
            ]

            manual_fields = super().get_manual_fields(path, method)
            return manual_fields + extra_fields


class FoodSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ["post", "put"]:
            extra_fields = [
                coreapi.Field('name', type='string', description='name'),
                coreapi.Field('desc', type='string', description='description'),
            ]

            manual_fields = super().get_manual_fields(path, method)
            return manual_fields + extra_fields


class RewardSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ["post", "put"]:
            extra_fields = [
                coreapi.Field('name', type='string', description='name'),
                coreapi.Field('desc', type='string', description='description'),
            ]

            manual_fields = super().get_manual_fields(path, method)
            return manual_fields + extra_fields


class AchievementSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ["post", "put"]:
            extra_fields = [
                coreapi.Field('name', type='string', description='name'),
                coreapi.Field('desc', type='string', description='description'),
            ]

            manual_fields = super().get_manual_fields(path, method)
            return manual_fields + extra_fields


class InfoAboutCoachSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ["post", "put"]:
            extra_fields = [
                coreapi.Field('id', type='integer', description='id'),
                coreapi.Field('info', type='string', description='name'),
            ]

            manual_fields = super().get_manual_fields(path, method)
            return manual_fields + extra_fields
