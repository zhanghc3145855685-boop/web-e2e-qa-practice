# Restful-Booker API 测试（Day 2）

本目录与 Day 1 的 `sauce-demo/` **隔离**，仅包含 Restful-Booker 接口测试相关交付物。

| 项 | 内容 |
|----|------|
| 被测系统 | [Restful-Booker](https://restful-booker.herokuapp.com/) |
| API 文档 | https://restful-booker.herokuapp.com/apidoc/index.html |
| 基础地址 | `https://restful-booker.herokuapp.com` |
| 演示 Auth | `admin` / `password123` |

## 目录结构

```text
restful-booker-api/
├── README.md
├── docs/
│   └── api-overview.md          # 接口速览
├── postman/
│   ├── README.md                # 导入与运行说明
│   └── restful-booker.postman_collection.json
├── data/
│   ├── api-test-cases.xlsx      # 用例 + 测试数据（Excel）
│   └── api-execution-results.xlsx  # 执行结果（Excel）
└── scripts/
    ├── requirements.txt
    ├── generate_excel.py        # 生成用例/数据表
    └── run_api_tests.py         # 调用真实 API 并回写结果表
```

## Excel 数据约定（业界常用拆分）

| Sheet / 文件 | 用途 |
|--------------|------|
| `api-test-cases.xlsx` → **EnvConfig** | 环境变量（baseUrl、账号等），换环境只改此表 |
| `api-test-cases.xlsx` → **TestCases** | 用例步骤、方法、路径、期望状态码、断言要点 |
| `api-test-cases.xlsx` → **TestData** | 请求体字段数据，通过 `DataRef` 与用例关联 |
| `api-test-cases.xlsx` → **FieldDictionary** | 列含义说明 |
| `api-execution-results.xlsx` → **ExecutionResults** | 实际状态码、通过/失败、响应摘要 |
| `api-execution-results.xlsx` → **Summary** | 总数、通过率 |

> 用例（怎么测）与数据（测什么值）分离，便于维护与扩展，也便于和 Postman / CI 对齐。

## 快速开始

### 1）生成 / 刷新 Excel 用例表

```bash
cd restful-booker-api/scripts
py -m pip install -r requirements.txt
py generate_excel.py
```

### 2）执行 API 并写出结果 Excel

```bash
py run_api_tests.py
```

### 3）用 Postman 跑同一套请求

见 [`postman/README.md`](postman/README.md)：导入 Collection → 按 01～11 顺序 Run Collection。

## Day 2 完成对照

| 标准 | 状态 |
|------|------|
| Collection ≥ 8 条请求 | 11 条 |
| 至少一半含 Tests 断言 | 11/11 均含 |
| 集合已归档在本目录 | `postman/restful-booker.postman_collection.json` |
| 用例/结果进 Excel | `data/*.xlsx` |
