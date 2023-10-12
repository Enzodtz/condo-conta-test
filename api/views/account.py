from rest_framework import viewsets
from api.serializers import AccountSerializer
from api.models import Account


class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows accounts to be viewed.
    """

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
