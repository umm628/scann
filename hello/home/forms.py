from django import forms

class OrderForm(forms.Form):
    items = forms.CharField(widget=forms.HiddenInput())
    total_price = forms.DecimalField(widget=forms.HiddenInput())

