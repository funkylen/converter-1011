from django.shortcuts import render
from .forms import InputForm
from currency_converter import CurrencyConverter
from django.views.generic import TemplateView


converter = CurrencyConverter()


from .convert_prices import convert_prices


def convert_function(value, currency, new_currency) -> tuple:
    return value * convert_prices[('RUB', currency)] / convert_prices[('RUB', new_currency)]


class TestPageView(TemplateView):
    template_name = 'test.html'


# Create your views here.
def get_conversion_result(request):
    if request.method == 'POST':
        recieved_form = InputForm(request.POST)
        if recieved_form.is_valid():
            recieved_form = recieved_form.clean()
            a_value, a_type = recieved_form['a_value'], recieved_form['a_type']
            b_type = recieved_form['b_type']
            b_value = convert_function(a_value, a_type, b_type)
            new_form = InputForm(initial={
                'a_value': a_value,
                'a_type': a_type,
                'b_type': b_type,
                'b_value': b_value
            })
            return render(request, 'test.html', {'form': new_form})
        
    form = InputForm
    return render(request, 'test.html', {'form': form})
