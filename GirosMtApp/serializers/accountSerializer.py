from GirosMtApp.models.account import Account
from rest_framework import serializers
from GirosMtApp.models.user import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:


        model = Account
        fields = ['balance', 'lastChangeDate', 'isActive']
    
    def to_representation(self, obj):
        account = Account.objects.get(id=obj.id)
        user = Account.objects.get(id=account.user_id)
        return{
            'id': user.id,
                    'username': user.username,
                    'name': user.name,
                    'email': user.email,
                    'user': {
                        'id': account.id,
                        'name': account.name,
                    }
                }
        
