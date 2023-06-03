import asyncio
import aiohttp

from api import submit_raid


async def process_token(session: aiohttp.ClientSession, token: str, token_number: int, raid_id: str, proxy: str):
    try:
        response = await submit_raid(session, token, raid_id, proxy)
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

            with open('proxies.txt', 'r') as file:
                proxies = [proxy.strip() for proxy in file if proxy.strip()]

            tasks = []
            for i, (token, proxy) in enumerate(zip(tokens, proxies), start=1):
                tasks.append(process_token(session, token, i, raid_id, proxy))

            await asyncio.gather(*tasks)
        except FileNotFoundError:
            print("Файл tokens.txt не найден.")

        await main()

if __name__ == '__main__':
    asyncio.run(main())
