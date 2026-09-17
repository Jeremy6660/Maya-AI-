# API Provider 配置参考

## 配置预设

界面最上方有「配置预设」下拉，可直接套用下表：

| 预设 | 接口类型 | Base URL | Model |
|---|---|---|---|
| 自定义 | 不改动 | 不改动 | 不改动 |
| `rightcode` | `RightCode Responses` | `https://www.rightapi.ai/codex/v1` | `gpt-5.2` |
| `DeepSeek` | `OpenAI-compatible Chat Completions` | `https://api.deepseek.com` | 清空，需自己填 |
| `OpenAI` | `OpenAI Responses` | `https://api.openai.com/v1` | 保持当前值 |

**预设只填充「接口类型 / Base URL / Model」三项，永远不改动 API Key 与「显示 Key」勾选。**

套用后仍可手动修改任意字段，包括 Model。

## DeepSeek / OpenAI-compatible

插件接口类型选择：

```text
OpenAI-compatible Chat Completions
```

然后填写服务商提供的：

```text
Base URL: 服务商 API 根地址
Model: 服务商模型 ID
API Key: 服务商 API Key
```

插件最终请求：

```text
<Base URL>/chat/completions
```

如果 Base URL 本身已经带 `/v1`，保留即可。

## OpenAI Responses

接口类型选择：

```text
OpenAI Responses
```

Base URL 通常填写 API 根地址，例如：

```text
https://api.openai.com/v1
```

插件最终请求：

```text
<Base URL>/responses
```

## RightCode

接口类型选择：

```text
RightCode Responses
```

Base URL 填：

```text
https://www.rightapi.ai/codex/v1
```

插件最终请求：

```text
<Base URL>/responses
```

RightCode 的 `/responses` 与 OpenAI 原生 Responses API **有两处不同**，所以插件为它单独走一条请求路径，不与上面两个 provider 共用：

- `input` 数组项必须带 `"type": "message"`
- 请求带 `"stream": true`，端点按 SSE（`text/event-stream`）返回，不是完整 JSON

插件两种返回都能解析：真流式时按 `output_text.delta` 逐块拼接；若服务端忽略 `stream` 返回完整 JSON，则按普通 JSON 解析。

鉴权头与其它 provider 一致：

```text
Authorization: Bearer <API Key>
```

## 本地 OpenAI-compatible 服务

允许：

```text
http://localhost:端口
http://127.0.0.1:端口
```

远程地址要求 HTTPS。

## 环境变量

插件会读取：

```text
DEEPSEEK_API_KEY
OPENAI_API_KEY
```

界面中手动填写的 Key 优先级最高。

## 安全

不要把真实 API Key 写入：

- README
- GitHub 仓库
- 示例配置文件
- 截图
- Maya 场景备注
