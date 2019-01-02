from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView, UpdateView, TemplateView)
from manager.models import Manager
from password_manager.contextobject import Objects
from django.contrib.auth.models import User
# Create your views here.

class Home(LoginRequiredMixin, TemplateView):
    """Landing page class."""

    template_name = 'user/home.html'
    def get_objects(self):
        return self.request.user

    # def get_queryset(self):
    #     queryset = Manager.objects.filter(user = self.request.user)
    #
    #     return queryset
    def get_context_data(self, **kwargs):
        """Get authenticated user information."""

        context = super().get_context_data(**kwargs)
        context['stats'] = Manager.objects.filter(user = self.request.user)

        return context


class Profile(LoginRequiredMixin, UpdateView):
    """View and Update authenticated user profile."""

    model = User
    fields = ['first_name', 'last_name', ]
    template_name = 'user/base_profile.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self, **kwargs):
        return reverse_lazy('user:profile', kwargs={'slug':self.request.user})
