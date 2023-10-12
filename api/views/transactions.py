from rest_framework import viewsets
from api.serializers import TransactionSerializer
from api.models import Transaction


class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow transactions to be viewed and created.
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
