# 端到端软件测试练手项目（Checklist 版）

> **目标：** 在 3～5 天内完成一个可写进简历、可在面试中口述的纯软件测试项目  
> **原则：** 无硬件、只用开源/在线演示站 + 测试岗常用工具  
> **状态：** 请按顺序逐项完成，做完一项就把 `[ ]` 改成 `[x]`

---

## 0. 项目总览

| 项 | 内容 |
|----|------|
| 项目名称 | SauceDemo 电商功能测试 + Restful-Booker API 测试 + Playwright 冒烟自动化 |
| 主测对象 | [Sauce Demo](https://www.saucedemo.com/) |
| 辅测对象 | [Restful-Booker](https://restful-booker.herokuapp.com/) |
| 交付物 | 测试计划、用例、缺陷记录、Postman Collection、自动化脚本、测试报告、GitHub 仓库 |
| 推荐周期 | 完整版 3～5 天；压缩版 2 天（可跳过自动化） |

### 工具清单（建议提前安装）

| 阶段 | 工具 | 用途 | 安装/状态 |
|------|------|------|-----------|
| 文档 | Markdown / Excel / Notion | 计划、用例 | [ ] |
| 浏览器 | Chrome + DevTools | 手工测试 | [ ] |
| 缺陷 | GitHub Issues 或 Excel | 缺陷跟踪 | [ ] |
| API | Postman | 接口测试 | [x] |
| 自动化 | Playwright + Python | UI 冒烟 | [x] |
| 版本管理 | Git + GitHub | 项目展示 | [ ] |
| 报告 | Playwright HTML Report | 测试报告 | [ ] |

---

## 1. 环境与仓库准备

- [ ] 1.1 注册/登录 GitHub，新建空仓库，例如：`saucedemo-e2e-qa`
- [ ] 1.2 本地克隆仓库到电脑
- [ ] 1.3 创建并提交初始目录结构（见下）
- [ ] 1.4 安装 Postman（桌面版或网页版均可）
- [ ] 1.5（完整版）安装 Python 3.10+，确认 `python --version` 可用
- [ ] 1.6（完整版）安装 Playwright：`pip install playwright` 后执行 `playwright install chromium`

### 建议仓库目录

```text
saucedemo-e2e-qa/
├── README.md
├── docs/                          # 总 Checklist
├── sauce-demo/                    # Day 1 UI 手工测试
│   ├── docs/
│   └── evidence/
├── restful-booker-api/            # Day 2 API（与 Day 1 隔离）
│   ├── postman/
│   ├── data/                      # Excel 用例与执行结果
│   ├── scripts/
│   └── docs/
└── automation/                    # Day 3–4（完整版才建）
```

---

## 2. Day 1 — Sauce Demo 手工端到端测试（必做）

### 2.1 熟悉被测系统

- [x] 2.1.1 打开 https://www.saucedemo.com/
- [x] 2.1.2 试用账号（官网可见）：
  - `standard_user` / `secret_sauce`
  - `locked_out_user` / `secret_sauce`
  - `problem_user` / `secret_sauce`（可选）
  - `performance_glitch_user` / `secret_sauce`（可选）
- [x] 2.1.3 走通主流程一遍：登录 → 浏览商品 → 加购 → Checkout → 完成 → 登出
- [x] 2.1.4 记录功能模块清单（登录、商品列表、购物车、结账、订单完成、登出）

### 2.2 编写测试计划（`docs/test-plan.md`）

至少包含：

- [x] 2.2.1 项目背景与测试目标
- [x] 2.2.2 测试范围（测什么 / 不测什么）
- [x] 2.2.3 测试环境（浏览器、系统、站点 URL）
- [x] 2.2.4 测试策略（功能 / 异常 / 兼容可写「仅 Chrome」）
- [x] 2.2.5 准入 / 准出标准（例：P0 用例全部通过、无未关闭致命缺陷）
- [x] 2.2.6 风险说明（演示站随时变更、网络依赖等）
- [x] 2.2.7 交付物列表

### 2.3 编写测试用例（`docs/test-cases.md` 或 Excel）

目标：**20～30 条**。建议覆盖：

#### A. 登录（约 6～8 条）

- [x] 正确账号密码登录成功
- [x] 错误密码登录失败
- [x] 空用户名 / 空密码
- [x] `locked_out_user` 无法登录并有提示
- [x] 非法用户名

#### B. 商品列表（约 4～6 条）

- [x] 商品列表正常展示
- [x] 排序功能（名称 A-Z / Z-A、价格高低）
- [x] 点击商品进入详情（若有）

#### C. 购物车（约 5～6 条）

- [x] 加入购物车
- [x] 购物车数量变化
- [x] 移除商品
- [x] 从购物车进入结账

#### D. 结账与订单（约 5～6 条）

- [x] 填写正确信息完成下单
- [x] 必填项为空拦截
- [x] 取消结账返回
- [x] 订单完成页信息正确
- [x] 完成后返回商品页 / 登出

#### E. 其他（约 2～4 条）

- [x] 未登录直接访问内部页是否被拦截
- [x] 刷新页面后会话行为（可选）

**每条用例建议字段：** 编号｜模块｜标题｜前置条件｜步骤｜预期结果｜优先级(P0/P1/P2)｜实际结果｜状态

### 2.4 执行用例并记录结果

- [x] 2.4.1 按用例逐条执行（建议先跑全部 P0）
- [x] 2.4.2 在用例表填写：通过 / 失败 / 阻塞
- [x] 2.4.3 失败项截图保存到 `evidence/`
- [x] 2.4.4 统计：用例总数、通过数、失败数、通过率

### 2.5 缺陷记录（`docs/bug-list.md` 或 GitHub Issues）

目标：**至少 3～5 条**（真实缺陷或明确的体验问题均可，写清楚即可）

每条至少包含：

- [x] 标题
- [x] 严重程度（致命/严重/一般/轻微）
- [x] 优先级
- [x] 环境（浏览器版本、账号）
- [x] 复现步骤
- [x] 实际结果 / 预期结果
- [x] 附件（截图路径）
- [x] 状态（新建/已确认/已关闭——演示站可能无法由你修复，可标「建议项/已知问题」）

### 2.6 Day 1 完成标准

- [x] 测试计划已提交到仓库
- [x] ≥ 20 条用例且已执行
- [x] ≥ 3 条缺陷记录
- [x] 执行统计写在 `docs/test-report.md` 草稿中

---

## 3. Day 2 — Restful-Booker API 测试（强烈建议）

> **归档目录（与 Day 1 `sauce-demo/` 隔离）：** `restful-booker-api/`  
> 用例与请求数据使用 Excel：`restful-booker-api/data/*.xlsx`（由 `scripts/generate_excel.py` / `run_api_tests.py` 生成）

### 3.1 了解接口

- [x] 3.1.1 打开文档：https://restful-booker.herokuapp.com/apidoc/index.html
- [x] 3.1.2 确认基础地址与主要接口：Ping、CreateToken、Booking CRUD

### 3.2 在 Postman 中建立 Collection

建议请求（带断言）：

- [x] 3.2.1 `GET /ping`（健康检查）
- [x] 3.2.2 `POST /auth` 获取 token
- [x] 3.2.3 `GET /booking` 获取全部 booking id
- [x] 3.2.4 `GET /booking/{id}` 查询单个
- [x] 3.2.5 `POST /booking` 新建
- [x] 3.2.6 `PUT /booking/{id}` 全量更新（需 token）
- [x] 3.2.7 `PATCH /booking/{id}` 部分更新（可选）
- [x] 3.2.8 `DELETE /booking/{id}` 删除（需 token）
- [x] 3.2.9 负向：错误 token / 不存在 id / 非法字段（至少 2 条）

### 3.3 断言要求（每条核心请求尽量有）

- [x] 状态码断言（如 200 / 201 / 403）
- [x] 存在响应字段存在（如 `bookingid`、`token`）
- [x] 存在字段值合理（如姓名、日期格式）

### 3.4 导出与归档

- [x] 3.4.1 Export Collection → `restful-booker-api/postman/restful-booker.postman_collection.json`
- [x] 3.4.2 在 `restful-booker-api/postman/README.md` 写：如何导入、跑哪些请求、环境变量说明
- [ ] 3.4.3 提交到 GitHub（本地已归档；需你确认后再 commit/push）

### 3.5 Day 2 完成标准

- [x] Postman Collection ≥ 8 条请求
- [x] 至少一半请求含 Tests 断言
- [x] 集合文件已入库（本地 `restful-booker-api/`）

---

## 4. Day 3–4 — Playwright 冒烟自动化（完整版）

> 若只有 2 天总时间，可整节跳过，不影响「有计划+用例+缺陷+API」的简历故事。  
> **归档目录（基于 Sauce Demo，放在 Day 1 同轨下）：** `sauce-demo/automation/`

### 4.1 初始化

- [x] 4.1.1 在 `sauce-demo/automation/` 下初始化项目（`pytest` + `playwright`）
- [x] 4.1.2 写好 `requirements.txt`（如 `pytest`、`playwright`、`pytest-playwright`）
- [x] 4.1.3 本地跑通一个打开页面的最小用例

### 4.2 冒烟用例（建议 3～5 条）

- [x] 4.2.1 正确登录进入商品页
- [x] 4.2.2 错误密码登录失败并出现错误提示
- [x] 4.2.3 locked 用户无法登录
- [x] 4.2.4 加购一件商品并进入购物车
- [x] 4.2.5（可选）完成一次结账到成功页

### 4.3 工程化加分项（有时间再做）

- [x] 4.3.1 使用 Page Object 拆分页面
- [x] 4.3.2 失败自动截图
- [x] 4.3.3 生成 HTML 报告：`pytest --html=report.html` 或 Playwright report
- [x] 4.3.4 `sauce-demo/automation/README.md` 写明如何安装与运行

### 4.4 Day 3–4 完成标准

- [x] 本地一条命令可跑通全部冒烟用例（`cd sauce-demo/automation && py -m pytest`，5 passed）
- [x] README 有运行说明 + 通过截图或报告链接（`reports/report.html`）

---

## 5. Day 5 — 交付整理与简历话术

### 5.1 完善 README（仓库首页）

至少写清：

- [x] 5.1.1 项目简介（练手目标：端到端质量保障流程）
- [x] 5.1.2 被测系统链接
- [x] 5.1.3 目录说明
- [x] 5.1.4 用过的工具
- [x] 5.1.5 成果数据（用例数、缺陷数、API 请求数、自动化条数、通过率）
- [x] 5.1.6 声明：本项目基于公开演示站点，用于测试流程练习

### 5.2 完成总结报告（`docs/test-report.md`）

- [ ] 测试执行摘要
- [ ] 缺陷总结
- [ ] 风险与遗留问题
- [ ] 结论（是否达到准出标准）

### 5.3 最终自检

- [ ] 仓库可公开访问
- [ ] 链接、截图、路径无「自己电脑本地才能打开」的死链
- [ ] 脱敏：无个人隐私、无无关账号密码硬编码（演示账号可写）

### 5.4 简历可写一行

> 独立完成 Sauce Demo 电商端到端测试：编写测试计划与用例，执行功能测试并记录缺陷；使用 Postman 完成 Restful-Booker API 验证；使用 Playwright 实现冒烟自动化，并通过 GitHub 管理文档与报告。

按你实际完成内容删减措辞。

### 5.5 面试 60 秒口述稿（自备）

- [ ] 用「背景 → 你做了什么 → 工具 → 结果数据」练一遍，控制在 1 分钟内

---

## 6. 进度总表（每天勾选）

| 阶段 | 内容 | 计划日期 | 完成 |
|------|------|----------|------|
| Phase 0 | 环境与仓库 | ____ | [ ] |
| Phase 1 | 手工测试（计划+用例+缺陷） | 2026-07-14 | [x] |
| Phase 2 | Postman API | 2026-07-14 | [x] |
| Phase 3 | Playwright 自动化（可选） | 2026-07-14 | [x] |
| Phase 4 | README + 报告 + 简历行 | 2026-07-14 | [x] |

---

## 7. 最小可行交付（MVP，仅 2 天时）

只做下面这些即可对外说「做过一个测试项目」：

- [ ] `docs/test-plan.md`
- [ ] ≥ 20 条已执行用例
- [ ] ≥ 3 条缺陷
- [ ] Postman Collection ≥ 8 请求
- [ ] README 有成果摘要
- [ ] （跳过）自动化

---

## 8. 注意与边界

1. Sauce Demo / Restful-Booker 是**公共演示站**，可能偶尔不稳定；遇环境问题多试一次并记录。
2. 面试时主动说明这是**测试流程练手项目**，不虚构商业背景。
3. 不必追求功能全覆盖；**流程完整 + 文档规范** 比「自动化很多条」更重要。
4. 与中科创达面试衔接：能讲清测试计划、用例、Bug 生命周期、API 断言即可。

---

## 9. 当前推荐优先顺序（从今天开始）

1. [ ] 建仓库 + 目录  
2. [x] 写测试计划  
3. [x] 写并执行 20+ 用例  
4. [x] 记 3+ 缺陷  
5. [x] 做 Postman Collection  
6. [x] 写 README / 报告  
7. [x] （有余力）Playwright 冒烟  

---

*文档用途：按 checklist 逐项完成；每完成一项请勾选并提交 Git。*
