import sys
from pathlib import Path

KOKOMI_ROOT = Path(__file__).resolve().parent.parent.parent.parent / "Kokomi_Bot"
if str(KOKOMI_ROOT) not in sys.path:
    sys.path.insert(0, str(KOKOMI_ROOT))

from nonebot import get_driver, on_message, logger
from nonebot.rule import Rule
from nonebot.adapters.onebot.v11 import (
    Bot,
    MessageEvent,
    GroupMessageEvent,
    MessageSegment,
)

from app import KokomiBot, Platform, UserBasic

driver = get_driver()
kokomi_bot = KokomiBot()

COMMAND_PREFIXES = ("/", "wws")


@driver.on_startup
async def _():
    await kokomi_bot.init_bot()
    logger.info("Kokomi Bot 初始化完成")


def _is_kokomi_command() -> Rule:
    async def check(event: MessageEvent) -> bool:
        msg = event.get_plaintext().strip()
        if not msg:
            return False
        return any(msg.lower().startswith(p) for p in COMMAND_PREFIXES)

    return Rule(check)


kokomi_matcher = on_message(rule=_is_kokomi_command(), priority=5, block=True)


@kokomi_matcher.handle()
async def handle_kokomi(bot: Bot, event: MessageEvent):
    message = event.get_plaintext().strip()
    user_id = str(event.user_id)
    user = UserBasic(user_id, user_id)

    if isinstance(event, GroupMessageEvent):
        platform = Platform("qq_group", str(event.group_id), str(event.group_id))
    else:
        platform = Platform("qq_private", user_id, user_id)

    try:
        result = await kokomi_bot.main(
            message=message,
            user=user,
            platform=platform,
        )
    except Exception as e:
        logger.opt(exception=True).error("Kokomi Bot 处理指令出错")
        await kokomi_matcher.finish(f"处理指令时出错: {e}")

    if result["type"] == "img":
        img_path = Path(result["data"])
        if img_path.exists():
            await kokomi_matcher.finish(MessageSegment.image(img_path))
        else:
            logger.warning(f"Kokomi Bot 返回的图片路径不存在: {img_path}")
            await kokomi_matcher.finish("图片生成失败，文件不存在")
    elif result["type"] == "msg":
        await kokomi_matcher.finish(result["data"])
