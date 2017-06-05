from django import forms

class PriceRuleForm(forms.Form):

    title = forms.CharField(label="title", max_length = 50)
    target_type = forms.CharField(label="target_type" ,max_length=200)

class PriceRuleUpdateForm(forms.Form):
    title = forms.CharField(label="title", max_length = 50)
