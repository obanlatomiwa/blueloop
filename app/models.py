from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from app.choices import GENDER_CHOICE


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=80, unique=True,
                                    validators=[
                                        RegexValidator('^\+\d{1,3}\d{3,}$', 'Make sure you add valid a phone number. '
                                                                            'Add country code in number e.g +234XXXX',
                                                       'invalid phone number')])
    email = models.CharField(max_length=80, null=True, blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default='o')
    country = models.CharField(max_length=80, default='Nigeria', null=True)
    state = models.ForeignKey(State, null=True, blank=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=256, null=True, blank=True)
    lga = models.CharField(max_length=256, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class State(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    display_name = models.CharField(max_length=256, null=True,
                                    blank=True)  # matches the names for DISPLAY_STATES commons
    country = models.CharField(max_length=256, default='Nigeria')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

