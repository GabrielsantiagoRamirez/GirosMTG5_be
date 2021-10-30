from Backend.GirosMtApp.models.account import Account
from rest_framework import serializers
from GirosMtApp.models.user import User


class UserSerializer(serializers.ModelSerializer):
    account = User()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'account']


    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = user.objects.get(user=obj.id)
        return {
                    'id': user.id,
                    'username': user.username,
                    'name': user.name,
                    'email': user.email,
                    'account': {
                        'id': account.id,
                        'balance': account.balance,
                        'lastChangeDate': account.lastChangeDate,
                        'isActive': account.isActive
                    }
                }