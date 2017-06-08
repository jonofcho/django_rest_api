from django import forms
from .choices import *
from functools import partial
from datetimewidget.widgets import DateTimeWidget
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
    starts_at = forms.SplitDateTimeField(widget=forms.DateTimeInput(attrs={'class': 'datetimepicker'}),required=False)
    ends_at = forms.SplitDateTimeField(widget=forms.DateTimeInput(attrs={'class': 'datetimepicker'}),required=False)
