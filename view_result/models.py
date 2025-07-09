from django.db import models
class Student_database(models.Model):
    roll = models.IntegerField()
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    gender = models.CharField(max_length=70)
    absence_days = models.IntegerField()
    weekly_self_study_hours = models.IntegerField()
    career_aspiration = models.CharField(max_length=70)
    math_score = models.IntegerField()
    history_score = models.IntegerField()
    physics_score = models.IntegerField()
    chemistry_score = models.IntegerField()
    biology_score = models.IntegerField()
    english_score = models.IntegerField()
    geography_score = models.IntegerField()

