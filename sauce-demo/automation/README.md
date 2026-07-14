# Sauce Demo Playwright 冒烟自动化（Day 3–4）

被测站点：[Sauce Demo](https://www.saucedemo.com/)  
本目录挂在 `sauce-demo/` 下，与 Day 1 手工测试同轨，并与 `restful-booker-api/`（Day 2）隔离。

## 目录

```text
automation/
├── pages/           # Page Object
├── tests/           # 冒烟用例
├── reports/         # pytest-html 报告（运行后生成 report.html）
├── screenshots/     # 失败时额外截图
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## 安装

在仓库根目录或本目录执行（Windows 使用 `py`）：

```bash
cd sauce-demo/automation
py -m pip install -r requirements.txt
py -m playwright install chromium
```

## 一条命令跑全部冒烟

```bash
cd sauce-demo/automation
py -m pytest
```

默认：Chromium、失败截图、HTML 报告写入 `reports/report.html`。

### 常用变体

```bash
# 有界面
py -m pytest --headed

# 只跑登录相关
py -m pytest tests/test_smoke_login.py
```

## 冒烟用例对照（Checklist §4.2）

| 用例 | 文件 | 说明 |
|------|------|------|
| 4.2.1 正确登录 | `test_smoke_valid_login_enters_inventory` | standard_user → Products |
| 4.2.2 错误密码 | `test_smoke_wrong_password_shows_error` | 错误提示可见 |
| 4.2.3 locked 用户 | `test_smoke_locked_out_user_cannot_login` | locked out 提示 |
| 4.2.4 加购进车 | `test_smoke_add_item_and_open_cart` | 角标 1 + 购物车页 |
| 4.2.5 结账完成 | `test_smoke_checkout_to_complete` | 到达 Thank you 页 |

## 工程化（§4.3）

- **Page Object：** `pages/`
- **失败截图：** `pytest-playwright --screenshot only-on-failure` + `conftest` 写入 `screenshots/`
- **HTML 报告：** `reports/report.html`（`--self-contained-html`）

## 演示账号

| 用户名 | 密码 |
|--------|------|
| `standard_user` | `secret_sauce` |
| `locked_out_user` | `secret_sauce` |

## 报告查看

跑完后用浏览器打开：

`sauce-demo/automation/reports/report.html`
