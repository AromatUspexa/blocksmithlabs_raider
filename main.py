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
    async with aiohttp.ClientSession() as session:
        try:
            with open('tokens.txt', 'r') as file:
                tokens = [token.strip() for token in file if token.strip()]

            if not tokens:
                print("Файл tokens.txt пуст. Пожалуйста, заполните его.")
                return

            raid_id = input('Введите ID рейда: ')

            tasks = []
            for i, token in enumerate(tokens, start=1):
                tasks.append(process_token(session, token, i, raid_id))

            await asyncio.gather(*tasks)
        except FileNotFoundError:
            print("Файл tokens.txt не найден.")


if __name__ == '__main__':
    asyncio.run(main())
