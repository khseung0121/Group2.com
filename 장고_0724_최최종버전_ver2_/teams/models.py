from django.db import models


# Create your models here.
class Team(models.Model):
    t_name = models.CharField(max_length=30)
    t_major = models.CharField(max_length=30)
    t_captain = models.CharField(max_length=30)
    t_memCount = models.IntegerField(default=0)
    t_memo = models.TextField(null=False)

    def __str__(self):
        return self.t_name


class Recruit(models.Model):
    r_title = models.CharField(max_length=30)
    r_memo = models.CharField(max_length=255)
    r_writer = models.CharField(max_length=20)
    r_date = models.DateTimeField('작성일', auto_now_add=True)

    def __str__(self):
        return self.r_title


class Comment(models.Model):
    c_comment = models.CharField(max_length=255)
    c_date = models.DateTimeField('작성일', auto_now_add=True)
    c_writer = models.CharField(max_length=20, blank=True)
    c_recid = models.IntegerField(default=0)

    def __str__(self):
        return self.c_comment
