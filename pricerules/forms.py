from django import forms
from .choices import *
from functools import partial
from datetimewidget.widgets import DateTimeWidget
import datetime
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class PriceRuleForm(forms.Form):

    title = forms.CharField(label="title", max_length = 50)
    target_type = forms.ChoiceField(choices = TARGET_TYPE_CHOICES, label="target type")
    target_selection = forms.ChoiceField(choices = TARGET_SELECTION_CHOICES, label="target selection")
    allocation_method = forms.ChoiceField(choices = ALLOCATION_METHOD_CHOICES, label = "allocation method")
    value_type = forms.ChoiceField(choices = VALUE_TYPE_CHOICES, label = "value type")
    value = forms.IntegerField(label="Value")
    once_per_customer = forms.ChoiceField(choices = ONCE_PER_CUSTOMER_CHOICES, label = "once per customer?")
    usage_limit = forms.IntegerField(label="Usage Limit")
    customer_selection = forms.ChoiceField(choices = CUSTOMER_SELECTION_CHOICES, label ="Customer Selection")
    # prerequisite_Subtotal_range = forms.IntegerField
    # prerequisite_shipping_price_range =
    # prerequisite_saved_search_ids
    entitled_product_ids = forms.MultipleChoiceField(choices = PRODUCT_CHOICES, label="product ids []", required=False, widget=forms.CheckboxSelectMultiple)
    entitled_variant_ids = forms.MultipleChoiceField(choices = VARIANT_CHOICES, label="variant ids []", required=False, widget=forms.CheckboxSelectMultiple)
    entitled_collection_ids = forms.IntegerField(label="collection ids []", required=False)
    entitled_country_ids = forms.IntegerField(label="country Ids []", required=False)
    starts_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'datetimepicker'}))
    ends_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'datetimepicker'}))

    def clean(self):
        form_data = self.cleaned_data
        if form_data['target_type'] == 'shipping_line' and form_data['allocation_method'] == 'each':
            self._errors['allocation_method'] = ["Allocation Method can only be 'each' when target_type is equal to line_item"]
            del form_data['allocation_method']
        if form_data['target_type'] != 'shipping_line' and form_data['value_type'] == 'percentage':
            self._errors['value_type'] = ['Target Type must be shipping_line in order for Value Type to be a percentage']
            del form_data['value_type']
        if form_data['value'] > 0:
            self._errors['value'] = ['Value must be less than 0']
            del form_data['value']
        if form_data['target_type'] == 'shipping_line' and form_data['value'] != -100:
            self._errors['value'] = ['While target_type is equal to shipping_line , value can only be equal to -100']
            del form_data['value']
        if form_data['usage_limit'] < 1 :
            self._errors['usage_limit'] = ['Usage Limit must be an integer over 0']
            del form_data['usage_limit']
        return form_data
