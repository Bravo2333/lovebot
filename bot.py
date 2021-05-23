import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot


nonebot.init()
nonebot.load_plugins("lovebot\\plugins")
nonebot.load_plugins()
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
nonebot.load_builtin_plugins()

if __name__ == "__main__":
    nonebot.run()
