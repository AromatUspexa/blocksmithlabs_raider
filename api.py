import aiohttp


async def get_raid_ids(session: aiohttp.ClientSession):
    url = "https://raven.blocksmithlabs.io/api/projects/all"
    payload = "\"all\""
    response = await session.post(url, data=payload)
    list_form_json = await response.json()
    id_list = [ID['_id'] for ID in list_form_json['data']]
    return id_list


async def submit_raid(session: aiohttp.ClientSession, token: str, raid_id: str) -> str or None:
    url = f"https://raven.blocksmithlabs.io/api/tweet/{raid_id}/enter"
    headers = {"cookie": f"__Secure-next-auth.session-token={token}"}
    response = await session.post(url, headers=headers)
    if response.status == 502:
        return 'Не удалось нажать кнопку (ошибка 502): попробуйте позже'
    data = await response.json()
    if 'success' in data:
        if data['success']:
            return f"Успешно!"
        else:
            return f"Не удалось принять участие в рейде: не выполнены условия для участия"
    elif data["error"] == "You must link a wallet in the 'Account' page to enter raffles.":
        return "Вы не присоединили Phantom кошелек к аккаунту!"
    else:
        return data['error']
