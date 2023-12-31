import config

# 判断是否是管理员
def Authorization(func):
    async def wrapper(*args, **kwargs):
        if config.whitelist == None:
            return await func(*args, **kwargs)
        if (args[0].effective_chat.id not in config.whitelist):
            message = (
                f"`Hi, {args[0].effective_user.username}!`\n\n"
                f"id: `{args[0].effective_user.id}`\n\n"
                f"无权访问！\n\n"
            )
            await args[1].bot.send_message(chat_id=args[0].effective_chat.id, text=message, parse_mode='MarkdownV2')
            return
        return await func(*args, **kwargs)
    return wrapper