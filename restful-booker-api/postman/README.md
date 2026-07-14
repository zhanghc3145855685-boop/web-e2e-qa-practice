# Postman Collection 使用说明

## 导入

1. 打开 Postman（桌面版或网页版）。
2. **Import** → 选择本目录下的 `restful-booker.postman_collection.json`。
3. 导入后可见集合 **Restful-Booker API Tests**（共 11 个请求）。

## 环境 / 集合变量

变量定义在 Collection Variables（无需单独 Environment 也可跑）：

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `baseUrl` | `https://restful-booker.herokuapp.com` | API 根地址 |
| `username` | `admin` | CreateToken 用户名 |
| `password` | `password123` | CreateToken 密码 |
| `token` | （空，运行时写入） | `02 Auth` 成功后自动保存 |
| `bookingId` | （空，运行时写入） | `03/05` 运行后自动保存 |

如需切换环境，在 Collection Variables 中修改 `baseUrl` 即可。

## 建议执行顺序

在集合上点击 **Run**，保持默认顺序（01 → 11）：

| # | 请求 | 断言要点 |
|---|------|----------|
| 01 | `GET /ping` | 201，body 含 `Created` |
| 02 | `POST /auth` | 200，存在非空 `token` |
| 03 | `GET /booking` | 200，非空数组，元素含 `bookingid` |
| 04 | `GET /booking/{id}` | 200，核心字段与日期格式 |
| 05 | `POST /booking` | 200，`bookingid` + 字段值匹配 |
| 06 | `PUT /booking/{id}` | 200，全量字段更新（需 token） |
| 07 | `PATCH /booking/{id}` | 200，部分字段更新（需 token） |
| 08 | `DELETE /booking/{id}` | 201，body 含 `Created`（该站删除成功约定） |
| 09 | `GET` 不存在 id | 404 |
| 10 | `DELETE` 错误 token | 403 |
| 11 | `POST /auth` 错误密码 | 200 且 `reason=Bad credentials` |

> 正向 CRUD（05→08）依赖 02 写入的 `token` 与 05 写入的 `bookingId`，请勿打乱顺序单独跳跑写操作。

### 04 失败时怎么处理

常见原因：集合变量 `bookingId` 仍是**上一次** `08 DELETE` 删掉的 id，再次跑到 `04` 会得到 **404**，`Status code is 200` 失败。

处理：

1. **重新导入**更新后的 `restful-booker.postman_collection.json`（`03` 已改为每次刷新 `bookingId`）。
2. 或在集合 **Variables** 里把 `bookingId` 清空后再从 `01` 顺序 Run。
3. 不要只单独 Send `04`；至少先跑通 `03`，让 `bookingId` 写成当前仍存在的 id。

## 与 Excel 的对应关系

| Postman 请求名 | Excel CaseID |
|----------------|--------------|
| 01 GET Ping Health Check | API-001 |
| 02 POST Auth Create Token | API-002 |
| 03 GET All Bookings | API-003 |
| 04 GET Booking By Id | API-004 |
| 05 POST Create Booking | API-005 |
| 06 PUT Update Booking | API-006 |
| 07 PATCH Partial Update Booking | API-007 |
| 08 DELETE Booking | API-008 |
| 09 NEG GET Nonexistent Booking Id | API-009 |
| 10 NEG DELETE With Invalid Token | API-010 |
| 11 NEG POST Auth Bad Credentials | API-011 |

用例明细与请求体数据见 `../data/api-test-cases.xlsx`。
