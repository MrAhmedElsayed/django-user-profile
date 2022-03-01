from django.db import models


class UserProfileModel(models.Model):
    """
    User profile model
    """
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username