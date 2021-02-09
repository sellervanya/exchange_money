from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta():
        model = Order
        fields = ('operation_type', 'currency', 'amount',)
        widgets = {
                'operation_type': forms.Select(attrs={
                    'class': 'form-control',
                    'onchange': 'id_summ.value=result()'
                    }),

                'currency': forms.Select(attrs={
                    'class': 'form-control',
                    'onchange': 'id_summ.value=result()'
                    }),

                'amount': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'onchange': 'id_summ.value=result()'
                    }),
        }
