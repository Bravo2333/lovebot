from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests
import test
weather = on_command("s", rule=to_me(), priority=5, block=True)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="无图言dio")
async def handle_city(bot: Bot, event: Event, state: T_State):
    city: str = state["city"]
    segments = city.split(',')
    url = segments[2][4:]
    url = url.split(']')
    response = requests.get(url[0])
    with open('image.png', 'wb') as f:
        f.write(response.content)
    name = test.record("image.png")
    if "你这什么玩意？" in name:
        strs = "你这什么玩意？"
    else:
        strs = name[0]+name[1]+name[2]+','+name[3]
    with open("result.txt", 'a') as f:
        f.writelines(strs+'\n')
    await weather.reject(strs)
