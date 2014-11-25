from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from purplealpaca.models import Account
from purplealpaca.permissions import IsOwner
from purplealpaca.serializers import AccountSerializer, UserSerializer, UserDelSerializer
from rest_framework.decorators import api_view

# Model Viewset for the account model. Allows 
class AccountViewSet(viewsets.ModelViewSet):
    
    # Define the queryset to act on for the account models
    queryset = Account.objects.all()

    # Define the serializer used to serialize/de-serialize the data
    serializer_class = AccountSerializer
    
    # Define the permissions required for Account view requests to be provided
    permission_classes = [IsAuthenticated, IsOwner]

    # Assign the account object owner upon account object creation
    def pre_save(self, obj):
        obj.owner = self.request.user

    # Define the queryset to be provided for the authenticated user to act on
    def get_queryset(self):
        return self.request.user.accounts.all()

# Modell Viewset for the User model. 
class UserViewSet(viewsets.ModelViewSet):
    model = User
    # Serializer used to delete the User model (Destroying main user account).
    serializer_class = UserDelSerializer

    # All requests to the user view must be authenticated
    permission_classes = [IsAuthenticated]

    # The queryset to act on will be all user object of the requested user. 
    queryset = User.objects.all()    
    def get_queryset(self):
        return User.objects.filter(username=self.request.user)    

# Define the POST view to create a new main user account
@api_view(['POST'])
# Exempt csrf tokens in the headers as they are not needed for this request
@csrf_exempt
def create_auth(request):

    # User serializer for the incoming create account request
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['username'],
            serialized.init_data['email'],
            serialized.init_data['password']
        )
        return Response(status=status.HTTP_201_CREATED)
    else:
        # User account already exists. 
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
