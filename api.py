import requests

def get_raid_ids():
    url = "https://raven.blocksmithlabs.io/api/projects/all"
    payload = "\"all\""
    response = requests.request("POST", url, data=payload)
    list_form_json = response.json()
    id_list = [ID['_id'] for ID in list_form_json['data']]
    return id_list


def sign_request(token: str, ID: str) -> None:
    url = f"https://raven.blocksmithlabs.io/api/tweet/{ID}/enter"
    payload = ""
    headers = {
        "cookie": f"__Secure-next-auth.session-token={token}"}
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 502:
        print('Попробуйте перезапусть програму, не удалось нажать кнопку')
        return
    response_date = response.json()
    if 'success' in response_date:
        print(response_date['success'])
    else:
        print(response_date['error'])
