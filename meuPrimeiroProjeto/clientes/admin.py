from django.contrib import admin
from clientes.models import Cliente
from clientes.models import Telefone
from clientes.models import CPF
from clientes.models import Colaborador
from clientes.models import Departamento
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    fields = ('nome', 'endereco')
    list_display = ('id', 'nome', 'endereco', 'email')
    #list_filter = ('departamentos')
    search_fields = ('id', 'nome', 'email', 'endereco')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Colaborador)
admin.site.register(Departamento)