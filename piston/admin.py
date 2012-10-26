from django.contrib import admin
from piston.models import Nonce, Token, Consumer

admin.site.register(Nonce)
admin.site.register(Token, raw_id_fields=('user', 'consumer'))
admin.site.register(Consumer, raw_id_fields=('user',))
