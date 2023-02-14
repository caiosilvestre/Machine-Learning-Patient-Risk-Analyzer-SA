from .dict_etl import dict_etl

# Change key names in the document based in dict_etl.py
def etl_forms(form):
    dict_patient = {}

    for kv_pair in form.key_value_pairs:
        if kv_pair.key:
            if kv_pair.key.content in dict_etl.keys():
                if kv_pair.value:
                    dict_patient[f'{dict_etl[f"{kv_pair.key.content}"]}'] = kv_pair.value.content
            else:
                if kv_pair.value:
                    dict_patient[f'{kv_pair.key.content.replace(":","")}'] = kv_pair.value.content
                else:
                    dict_patient[f'{kv_pair.key.content}'] = 'none'

    return dict_patient
