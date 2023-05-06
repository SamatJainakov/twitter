from rest_framework import serializers

from .models import User, Profile


class UserRegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=13)
    short_info = serializers.CharField()

    class Meta:
        model = User
        fields = ["username", "password", "profile_image", "phone_number", "short_info"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        if not len(value) >= 8:
            raise serializers.ValidationError("Пароль должен быть больше 8 символов")
        if '1234567890' not in value:
            raise serializers.ValidationError("Пароль должен содержать числа")
        if value.upper not in value:
            raise serializers.ValidationError("Пароль должен содержать заглавные буквы")
        if value.lower not in value:
            raise serializers.ValidationError("Пароль должен содержать прописные буквы")
        if '!@#$%^&*()_+=/|?/.,<>;:"' not in value:
            raise serializers.ValidationError("Пароль должен содержать спецсимвол")
        return value

    def validate(self, data):
        if not User.password == data:
            raise serializers.ValidationError("Пароль не совпадает")
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        profile_image = validated_data.get('profile_image')
        if profile_image:
            user.profile_image = profile_image
        user.set_password(validated_data['password'])
        user.save()
        try:
            profile = Profile.objects.create(
                user=user,
                phone_number=validated_data['phone_number'],
                short_info=validated_data['short_info']
            )
        except Exception as e:
            user.delete()
            raise e
        else:
            profile.username = user.username
            profile.profile_image = user.profile_image
        return profile
