from .models import user_accounts


def accuonts_list(request):
    accounts = user_accounts.objects.all()
    return {'accounts' : accounts}
