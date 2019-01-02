from django.contrib.auth.models import User

class Objects(object):
    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        """Get authenticated user information."""

        context = super().get_context_data(**kwargs)
        context['logged_user'] = User.objects.filter(username = self.request.user)
        context['Users'] = User.objects.all()

        return context
