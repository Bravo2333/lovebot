from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

weather = on_command("p", rule=to_me(), priority=5, block=True)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    strings = ""
    with open("students.txt", 'r', encoding='utf-8') as f:
        strs = f.readline()
        while strs:
            strings += strs
            strs = f.readline()
    await weather.reject(strings)