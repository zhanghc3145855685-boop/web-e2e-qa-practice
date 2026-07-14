# Web 端到端软件测试练手项目（web-e2e-qa-practice）

> 独立完成的 **软件测试全流程练习**：手工功能测试 → 缺陷记录 → API 接口测试 → UI 冒烟自动化。  
> 基于公开演示站点，用于测试方法与工具链演练，**非商业生产项目**。
---

## 1. 项目简介

本仓库练习一名测试工程师从 0 到交付的常见工作流：

1. **手工端到端测试（UI）**：针对电商演示站编写测试计划、用例，执行并记录缺陷  
2. **接口测试（API）**：用 Postman + Excel 数据驱动验证酒店预订 CRUD 接口  
3. **冒烟自动化（UI）**：用 Playwright + pytest 覆盖登录/购物/结账主路径  

**练手目标：** 能讲清测试计划、用例设计、缺陷生命周期、API 断言与冒烟自动化门禁。

---

## 2. 被测系统

| 类型 | 系统 | 链接 |
|------|------|------|
| 主测（UI） | Sauce Demo（Swag Labs） | https://www.saucedemo.com/ |
| 辅测（API） | Restful-Booker | https://restful-booker.herokuapp.com/ |
| API 文档 | Restful-Booker API Doc | https://restful-booker.herokuapp.com/apidoc/index.html |

演示账号（Sauce Demo，官网公开）：

| 用户名 | 密码 | 用途 |
|--------|------|------|
| `standard_user` | `secret_sauce` | 主路径 |
| `locked_out_user` | `secret_sauce` | 锁定用户异常 |
| `problem_user` / `error_user` | `secret_sauce` | 缺陷复现 |

Restful-Booker Auth（文档公开）：`admin` / `password123`

---

## 3. 目录说明

```text
web-e2e-qa-practice/
├── README.md                          # 本文件
├── docs/
│   └── 端到端测试练手项目_Checklist.md # 总进度 Checklist（唯一）
├── sauce-demo/                        # UI：手工测试 + 自动化
│   ├── docs/                          # 测试计划 / 用例 / 缺陷 / 报告草稿
│   ├── evidence/                      # 手工测试缺陷截图
│   └── automation/                    # Playwright 冒烟（Day 3–4）
├── restful-booker-api/                # API：Postman + Excel（Day 2）
│   ├── postman/                       # Collection 与导入说明
│   ├── data/                          # 用例表 & 执行结果 Excel
│   ├── scripts/                       # 生成 Excel / 跑接口回写结果
│   └── docs/                          # 接口速览
└── LICENSE
```

| 模块 | 路径 | 阶段 |
|------|------|------|
| 手工 UI | `sauce-demo/docs/`、`sauce-demo/evidence/` | Day 1 |
| API | `restful-booker-api/` | Day 2 |
| UI 自动化 | `sauce-demo/automation/` | Day 3–4 |
| 总清单 | `docs/端到端测试练手项目_Checklist.md` | 全程 |

---

## 4. 使用的工具

| 类别 | 工具 |
|------|------|
| 文档与用例 | Markdown、Excel（openpyxl） |
| 手工测试 | Chrome / Chromium |
| 缺陷与证据 | Markdown + 截图 |
| 接口测试 | Postman、Python `requests` |
| UI 自动化 | Playwright、pytest、pytest-playwright、pytest-html |
| 版本管理 | Git / GitHub |

Windows 下 Python 请使用启动器：`py`（见 `.cursor/rules/python-py-command.mdc`）。

---

## 5. 成果数据

| 指标 | 结果 |
|------|------|
| UI 手工用例 | **26** 条，全部执行，通过率 **100%**（主账号 `standard_user`） |
| 缺陷记录 | **5** 条（多与 `problem_user` / `error_user` 演示异常相关） |
| API Postman 请求 | **11** 条（均含 Tests 断言）；脚本复跑通过率 **100%** |
| UI 冒烟自动化 | **5** 条；本地 `py -m pytest` → **5 passed** |
| 交付物 | 测试计划、用例、缺陷、API Collection、Excel、自动化脚本与 HTML 报告 |

详细数据见：

- UI：`sauce-demo/docs/test-report.md`、`test-cases.md`、`bug-list.md`  
- API：`restful-booker-api/data/api-execution-results.xlsx`  
- 自动化报告：运行后生成 `sauce-demo/automation/reports/report.html`

---

## 6. 快速开始

### 6.1 查看手工测试文档

直接打开 `sauce-demo/docs/` 下 Markdown 文件即可。

### 6.2 导入并运行 API Collection

1. Postman → Import → `restful-booker-api/postman/restful-booker.postman_collection.json`  
2. 按请求 **01 → 11** 顺序 Run Collection  
3. 说明：`restful-booker-api/postman/README.md`

刷新 Excel 用例 / 执行结果：

```bash
cd restful-booker-api/scripts
py -m pip install -r requirements.txt
py generate_excel.py
py run_api_tests.py
```

### 6.3 运行 UI 冒烟自动化

```bash
cd sauce-demo/automation
py -m pip install -r requirements.txt
py -m playwright install chromium
py -m pytest
```

一条命令跑完全部冒烟；报告：`sauce-demo/automation/reports/report.html`。

---

## 7. 简历可写一行（可按实际删减）

> 独立完成 Web 端到端软件测试练手项目：基于 Sauce Demo 编写测试计划与用例并执行缺陷记录；使用 Postman / Excel 完成 Restful-Booker API 验证；使用 Playwright + pytest 实现冒烟自动化，通过 GitHub 管理文档与报告。

---

## 8. 声明

- 本项目基于 **公开演示站点**（Sauce Demo、Restful-Booker），仅用于测试流程与工具练习。  
- 不虚构商业背景；演示站行为可能变更，遇失败请重试并对照最新页面/接口。  
- 仓库中仅为演示公开账号，无个人隐私与无关生产密钥。

进度总表见：[docs/端到端测试练手项目_Checklist.md](docs/端到端测试练手项目_Checklist.md)
