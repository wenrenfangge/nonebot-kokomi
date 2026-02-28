# wowsBot

## How to start

1. generate project using `nb create` .
2. create your plugin using `nb plugin create` .
3. writing your plugins under `src/plugins` folder.
4. run your bot using `nb run --reload` .

## Kokomi Bot 配置（不修改 Kokomi_Bot 源码）

配置只通过 **`Kokomi_Bot/config.toml`** 生效（Kokomi_Bot 原生命令读取该文件）。

与官方说明里 `config.yaml` 的对应关系：

| 官方 config.yaml | Kokomi_Bot/config.toml |
|------------------|------------------------|
| API.API_URL `http://127.0.0.1:8080` | `[api]` 里 `host = "127.0.0.1"`、`port = 8080` |
| API.REQUEST_TIMEOUT | `timeout = 10` |
| API.API_USERNAME（接口用户名） | 当前代码无对应项，仅文档中有 |
| API.API_PASSWORD（接口密码） | `token = "..."` |
| BOT.PLATFORM | `platform = "qq_bot"` |
| BOT.LOG_LEVEL | `log_level = "debug"` |
| BOT.USE_MOCK | `use_mock = true` |
| BOT.RETURN_PIC_TYPE | `file_type = "png"` 或 `"jpg"` |
| BOT.SHOW_DOG_TAG / SHOW_CLAN_TAG / SHOW_CUSTOM_TAG | `show_dog_tag` / `show_clan_tag` / `show_costom_tag` |
| BOT.ROOT_USERS `["QQ号1","QQ号2"]` | `root_users = "QQ号1:QQ号2"`（多个用英文冒号分隔） |

接入 QQ 时把管理员 QQ 号填到 `root_users`，例如：`root_users = "123456789"` 或 `root_users = "123456789:987654321"`。

## Documentation

See [Docs](https://nonebot.dev/)
