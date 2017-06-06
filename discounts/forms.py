from django import forms

class DiscountForm(forms.Form):
    code = forms.CharField(label="code title" , max_length = 100)
