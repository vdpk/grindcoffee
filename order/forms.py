from django import forms

from order.models import ProductOrder


class OrderForm(forms.ModelForm):
    class Meta:
        model = ProductOrder
        exclude = [
            'customer_id',
            'cart_id',
        ]

    def clean(self):
        data = self.cleaned_data
        return data


    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
