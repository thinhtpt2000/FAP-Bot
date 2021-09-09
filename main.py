# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import bot
import asyncio

async def main():
   await bot.on_ready()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   loop = asyncio.get_event_loop()
   loop.run_until_complete(main())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
