class NewJsonObject(object):
    discount_code = ''
    expiration_date = ''
    usage_limit = ''
    usage_count = ''
    value_type = ''
    value = ''
    entitled_variant_ids = ''
    def __init__(self , pr_data , dc_data):
        pr = pr_data.get('price_rule')
        pr_value = pr.get('value')
        pr_value_type = pr.get('value_type')
        pr_entitled_variant_ids = pr.get('entitled_variant_ids')
        pr_end_date = pr.get('ends_at')
        pr_usage_limit = pr.get('usage_limit')
        for code in dc_data.get('discount_codes'):
            dc_code = code.get('code')
            dc_usage_count = code.get('usage_count')

        self.discount_code = dc_code
        self.expiration_Date = pr_end_date
        self.usage_limit = pr_usage_limit
        self.usage_count = dc_usage_count
        self.value_type = pr_value_type
        self.value = pr_value
        self.entitled_variant_ids = pr_entitled_variant_ids
    
