from rest_framework.serializers import ModelSerializer
from users.models import User


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    # codificar password de texto plano y encriptarlo con el algoritmo: pbkdf2_sha256 iteraciones: 260000
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'password',
            'facebook',
            'twitter',
            'instagram',
            'website'
        ]


class UserProfileTareasComentariosSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
        ]


class UserUpdateProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'facebook',
            'twitter',
            'instagram',
            'website',
        ]
