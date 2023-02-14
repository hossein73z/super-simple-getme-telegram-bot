import telegram
import asyncio
import os


async def main():
    token = 'BOT_TOKEN'
    token = os.environ.get('BOT_TOKEN', token)
    print(token)
    bot = telegram.Bot(token)
    async with bot:
        print(await bot.getMe())


if __name__ == '__main__':
    asyncio.run(main())
    input('\n------------------------------\nInput anything to exit!')

