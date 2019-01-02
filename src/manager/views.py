from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
    )
from django.views.generic.detail import DetailView as DV
from manager.models import Manager
from password_manager.contextobject import Objects
from django.urls import reverse_lazy
from cryptography.fernet import Fernet
from django.urls import reverse

# Create your views here.


class ListManager(LoginRequiredMixin, Objects, ListView):
    """View site login information."""

    template_name = 'manager/list.html'
    model = Manager
    def get_queryset(self):
        queryset = Manager.objects.filter(user=self.request.user)

        for j, i in enumerate(queryset):
            decoded_password = Fernet(str.encode(i.key)).decrypt(str.encode(i.password))
            decoded_username = Fernet(str.encode(i.key)).decrypt(str.encode(i.username))
            queryset[j].password=decoded_password.decode("utf-8")
            queryset[j].username=decoded_username.decode("utf-8")
            queryset[j].sn=j+1

        return queryset


class DetailManager(LoginRequiredMixin, DV):
    """Create site login information."""

    model = Manager
    #context_object_name = 'managerdetail'
    template_name = 'manager/detail.html'
    context_object_name = 'obj'

    def get_object(self):
        self.grab_id = str(str(self.request).replace("<WSGIRequest: GET '/manager/", '')).replace("'>", '')
        self.get_obj = self.get_queryset().get(id=self.grab_id)
        self.get_obj.password = (Fernet(str.encode(self.get_obj.key)).decrypt(str.encode(self.get_obj.password))).decode("utf-8")
        self.get_obj.username = (Fernet(str.encode(self.get_obj.key)).decrypt(str.encode(self.get_obj.username))).decode("utf-8")
        if 'http://' or 'https://' not in self.get_obj.website_link: self.get_obj.website_link = 'http://'+self.get_obj.website_link

        self.get_obj.value = str(self.request.user) == str(self.get_obj.user)
        return self.get_obj


class CreateManager(LoginRequiredMixin, CreateView):
    """Create site login information."""

    template_name = 'manager/create.html'
    model = Manager
    fields = ['website_name', 'website_link', 'username', 'password']


class DeleteManager(LoginRequiredMixin, DeleteView):
    """"Delete website manager object."""

    model = Manager
    success_url = reverse_lazy('manager:home')

    def get_queryset(self):
        qs = super(DeleteManager, self).get_queryset()
        return qs.filter(user=self.request.user)


class UpdateManager(LoginRequiredMixin, UpdateView):
    """Update website information"""

    model = Manager
    fields = ['website_name', 'username', 'password' ]
    template_name ='manager/update.html'

    def get_object(self):
#        print(self.request.GET)
        if self.request.POST:
            self.grab_id = str(str(self.request).replace("<WSGIRequest: POST '/manager/update/", '')).replace("'>", '')
        else:
            self.grab_id = str(str(self.request).replace("<WSGIRequest: GET '/manager/update/", '')).replace("'>", '')
        self.get_obj = self.get_queryset().get(id=self.grab_id)
        self.get_obj.password = (Fernet(str.encode(self.get_obj.key)).decrypt(str.encode(self.get_obj.password))).decode("utf-8")
        self.get_obj.username = (Fernet(str.encode(self.get_obj.key)).decrypt(str.encode(self.get_obj.username))).decode("utf-8")
        self.get_obj.value = str(self.request.user) == str(self.get_obj.user)
        return self.get_obj

class PasswordGenerator(LoginRequiredMixin, TemplateView):
    """Password Generator Class."""

    template_name = 'manager/password_generator.html'
