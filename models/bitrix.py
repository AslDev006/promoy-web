# import requests
# import environ
# env = environ.Env()
# environ.Env.read_env()
# BITRIX_DOMAIN=env('BITRIX_DOMAIN')
# BITRIX_USER_ID=env('BITRIX_USER_ID')
# WEBHOOK_KEY=env('WEBHOOK_KEY')
# def send_form_data(form_id, data):
#     url = f"https://{BITRIX_DOMAIN}/rest/{BITRIX_USER_ID}/{WEBHOOK_KEY}/crm.lead.add.json"
#     payload = {
#         "fields": {
#             "TITLE": f"Web saytdan {data['plans']} ta'rifi {data['count']} ta boks",
#             "NAME": data['name'],
#             "STATUS_ID": "NEW",
#             "OPENED": "Y",
#             "ASSIGNED_BY_ID": 1,
#             "CURRENCY_ID": "USD",
#             "OPPORTUNITY": str(data['currency']),
#             "PHONE": [{"VALUE": data['phone_number'].__str__(), "VALUE_TYPE": "WORK"}],
#             "WEB": [{"VALUE": "www.mysite.com", "VALUE_TYPE": "WORK"}]
#         }
#     }

#     response = requests.post(url, json=payload)