from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db.models.signals import pre_save, post_save
from app.choices import GENDER_CHOICE
from app.helper import unique_slug_generator, scramble_uploaded_image


# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    username = models.CharField(max_length=256, unique=True)
    phone_number = models.CharField(max_length=80, unique=True,
                                    validators=[
                                        RegexValidator('^\+\d{1,3}\d{3,}$', 'Make sure you add valid a phone number. '
                                                                            'Add country code in number e.g +234XXXX',
                                                       'invalid phone number')])
    email = models.CharField(max_length=80, null=True, blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default='o')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


def account_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, field=instance.username)


pre_save.connect(account_pre_save_receiver, sender=Account)


class Post(models.Model):
    user = models.ForeignKey(Account, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=scramble_uploaded_image, default='', blank=False)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title


def post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, field=instance.title)


pre_save.connect(post_pre_save_receiver, sender=Post)


class Comment(models.Model):
    user = models.ForeignKey(Account, default=1, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.user.username
