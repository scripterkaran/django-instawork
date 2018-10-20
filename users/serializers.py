from users.models import User
from utils.serializers import CustomHyperLinkedModelSerializer


class UserSerializer(CustomHyperLinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'phone_number', 'role', 'email',)
