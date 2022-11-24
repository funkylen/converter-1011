from django import forms
from .convert_prices import convert_prices


units_list = set(map(lambda pair: pair[1], convert_prices.keys()))


class InputForm(forms.Form):
    a_value = forms.FloatField(label='Значение', initial=10)
    a_type = forms.ChoiceField(label='Выбор валюты', choices=[(str(i), str(i)) for i in units_list])
    b_value = forms.FloatField(label='Значение', initial=0)
    b_type = forms.ChoiceField(label='Выбор валюты', choices=[(str(i), str(i)) for i in units_list])
