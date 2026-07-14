# Restful-Booker 接口速览（Day 2）

文档入口：https://restful-booker.herokuapp.com/apidoc/index.html  
基础地址：`https://restful-booker.herokuapp.com`

## 主要接口

| 能力 | Method | Path | 鉴权 | 备注 |
|------|--------|------|------|------|
| Ping | GET | `/ping` | 否 | 成功多为 **201** + `Created` |
| CreateToken | POST | `/auth` | 否 | Body: username/password → `token` |
| 列表 | GET | `/booking` | 否 | 返回 `[{bookingid}]` |
| 查询 | GET | `/booking/{id}` | 否 | 单条 booking 详情 |
| 新建 | POST | `/booking` | 否 | 成功多为 **200**（非 201） |
| 全量更新 | PUT | `/booking/{id}` | Cookie `token=` | 需合法 token |
| 部分更新 | PATCH | `/booking/{id}` | Cookie `token=` | 可选字段 |
| 删除 | DELETE | `/booking/{id}` | Cookie `token=` | 成功多为 **201** + `Created` |

## 实测注意点

1. 删除成功、Ping 成功的状态码与文案和常见 REST 习惯不完全一致，断言需按文档/实测写。
2. 错误密码时 `/auth` 仍可能返回 200，body 为 `{"reason":"Bad credentials"}`。
3. 错误 token 删除返回 **403**；不存在的 id 查询返回 **404**。
