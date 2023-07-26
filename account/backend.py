from django.contrib.auth.backends import ModelBackend
from .models import user_accounts
from django.db.models import Q

class EmailPhoneCodeMelliBackend(ModelBackend):
    def authenticate(self, request, username=None, codeMelli=None, password=None, **kwargs):
        try:
            user = user_accounts.objects.get(Q(email=username) | Q(codeMelli=codeMelli))
            if user.check_password(password):
                return user
        except user_accounts.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return user_accounts.objects.get(pk=user_id)
        except user_accounts.DoesNotExist:
            return None