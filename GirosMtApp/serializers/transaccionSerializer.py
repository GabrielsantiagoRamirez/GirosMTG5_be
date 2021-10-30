from GirosMtApp.models.account     import Account
from GirosMtApp.models.user        import User
from GirosMtApp.models.transaccion import Transaccion
from rest_framwork import serializers


class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields =["origin_account " ,"destiny_account" , "amount" ,"registar_date  " ,"note"]


    def to_representation(self, obj):
        transaccion = Transaccion.objects.get(id=obj.id)
        oigin_account = Account.objects.get(id=transaccion.origin_account_id)
        destiny_account = Account.objects.get(id=transaccion.destiny_origin)
        destiny_user = User.objects.get(id=destiny_account.user_id)