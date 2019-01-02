from django.db import models
#from user.models import User
from django.contrib import auth
from cryptography.fernet import Fernet
from password_manager.getusername import current_request
from django.urls import reverse_lazy
# Create your models here.

class Manager(models.Model):
    """Create user password_manager model."""

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    website_name = models.CharField(max_length=30, help_text="e.g Facebook")
    website_link = models.CharField(max_length=50, help_text="e.g facebook.com")
    username = models.CharField(max_length=1000, verbose_name='Username/Email')
    password = models.CharField(max_length=1000, blank=True)
    key = models.CharField(max_length=55, blank=True)

    def __str__(self):
        return str(self.user.username)

    def get_object(self):
        return self.request.user

    def save(self, *args, **kwargs):

        dkey = Fernet.generate_key()
        cipher_suite = Fernet(dkey)
        encoded_password = cipher_suite.encrypt(str.encode(self.password))
        encoded_username = cipher_suite.encrypt(str.encode(self.username))
        #decoded_text = cipher_suite.decrypt(encoded_text)
        self.key = dkey.decode('utf-8')
        self.password = encoded_password.decode('utf-8')
        self.username = encoded_username.decode('utf-8')
        self.user = current_request().user
        print(self.user)
        #print(dkey, decoded_text, encoded_text)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('manager:detail', kwargs={'pk':self.id})
