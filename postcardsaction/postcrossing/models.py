from django.db import models


class PCUser(models.Model):
    username = models.CharField(
        help_text="The username of postcrossing user",
        unique=True,
        max_length=100,
    )

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["username"]
        verbose_name = "Postcrossing User"



class PCPostCard(models.Model):
    pc_id = models.CharField(
        "Postcrossing ID",
        help_text="The Key at poscrossing", max_length=100, unique=True
    )
    from_user = models.ForeignKey(
        PCUser, on_delete=models.SET_NULL, related_name="from_user", null=True
    )
    to_user = models.ForeignKey(
        PCUser, on_delete=models.SET_NULL, related_name="to_user", null=True
    )

    def __str__(self):
        return self.pc_id

    @property
    def url(self):
        """
        Returns URL for a postcrossing postcard
        """
        return "https://www.postcrossing.com/postcards/{}".format(self.pc_id)

    class Meta:
        ordering = ["-pc_id"]
        verbose_name = "Postcrossing Card"

