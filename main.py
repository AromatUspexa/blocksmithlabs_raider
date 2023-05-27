import asyncio

import aiohttp

from api import submit_raid


async def process_token(session: aiohttp.ClientSession, token: str, token_number: int, raid_id: str):
    try:
        response = await submit_raid(session, token, raid_id)
        print(f"[{token_number}]: {response}")
    except Exception as e:
        print(f"[{token_number}]: Непредвиденная ошибка!")


async def main():
    with open('tokens.txt', 'r') as file:
        tokens = [token.strip() for token in file.readlines() if token != "\n"]
    raid_id = input('Введите ID рейд: ')
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, token in enumerate(tokens):
            token_number = i + 1
            tasks.append(asyncio.create_task(process_token(session, token, token_number, raid_id)))
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
