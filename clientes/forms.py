from django import forms
from clientes.models import Cliente


class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


        widgets = {
                'nome': forms.TextInput(attrs={'class':'form-control', 'id': 'nome_id'}),
                'email': forms.EmailInput(attrs={'class':'form-control', 'id': 'email_id'}),
                'telefone': forms.NumberInput(attrs={'class':'form-control', 'id': 'telefone_id'}),
            }