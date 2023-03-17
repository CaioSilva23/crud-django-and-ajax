from django.contrib import admin
from clientes.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')


admin.site.register(Cliente, ClienteAdmin)