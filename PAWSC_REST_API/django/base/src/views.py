from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from base.src.serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView, Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class InitViewSet(APIView):
    
    def get(self, request, format=None):
       
        PAWS_dict = {
        'jsonrpc': '2.0',
        'id': '45455',
        'error': {
            'message': 'NOT_REGISTERED'
        }
    }
        return Response(PAWS_dict)

    def post(self, request, format=None):
        PAWS_dict = {
            'jsonrpc': '2.0',
            'id': '45455',
            'error': {
                'message': 'NOT_REGISTERED'
            }
        }
        return Response(PAWS_dict)
