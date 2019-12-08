from django.db import models


class PCUser(models.Model):
    username = models.CharField(
        help_text="The username of postcrossingg user",
        unique=True,
        max_length=100,
    )


class PCPostCard(models.Model):
    pc_id = models.CharField(
        help_text="The Key at poscrossing", max_length=100, unique=True
    )
    user = models.ManyToManyField(PCUser)

    def __str__(self):
        return (self.pc_id)
