from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from purplealpaca.models import Account
from purplealpaca.permissions import IsOwner
from purplealpaca.serializers import AccountSerializer, UserSerializer
from rest_framework.decorators import api_view


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def pre_save(self, obj):
        obj.owner = self.request.user

    def get_queryset(self):
        return self.request.user.accounts.all()


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer

@api_view(['POST'])
@csrf_exempt
def create_auth(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['username'],
            serialized.init_data['email'],
            serialized.init_data['password']
        )
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
