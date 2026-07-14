# Sauce Demo 缺陷记录

| 项 | 内容 |
|----|------|
| 文档版本 | v0.1（Day 1） |
| 记录日期 | 2026-07-14 |
| 说明 | 公共演示站缺陷/刻意异常账号行为，无法由本项目修复；状态标为「建议项/已知问题」 |

---

## BUG-001 problem_user 商品图片全部展示为 404 占位图

| 字段 | 内容 |
|------|------|
| 标题 | `problem_user` 登录后商品列表图片均为 404 资源 |
| 严重程度 | 严重 |
| 优先级 | P1 |
| 环境 | Windows + Chromium；账号 `problem_user` / `secret_sauce`；URL https://www.saucedemo.com/ |
| 复现步骤 | 1. 使用 `problem_user` 登录 2. 进入 Products 页 3. 查看各商品缩略图 src |
| 实际结果 | 全部商品图片指向 `/assets/sl-404-....jpg`，与正常商品图不符 |
| 预期结果 | 每个商品展示对应正确商品图片 |
| 附件 | `evidence/BUG-001-problem_user-images.png` |
| 状态 | 建议项/已知问题（演示账号刻意异常） |

---

## BUG-002 problem_user 名称 Z-A 排序无效

| 字段 | 内容 |
|------|------|
| 标题 | `problem_user` 选择 Name (Z to A) 后列表顺序仍为 A-Z |
| 严重程度 | 一般 |
| 优先级 | P2 |
| 环境 | 同上；账号 `problem_user` |
| 复现步骤 | 1. `problem_user` 登录 2. 排序下拉选择 Name (Z to A) 3. 读取商品名称顺序 |
| 实际结果 | 顺序仍为 Backpack → … → Red T-Shirt（A-Z），未按 Z-A 排列 |
| 预期结果 | 名称按字母降序排列 |
| 附件 | `evidence/BUG-002-problem_user-sort-za.png` |
| 状态 | 建议项/已知问题 |

---

## BUG-003 error_user 无法从列表移除已加购商品

| 字段 | 内容 |
|------|------|
| 标题 | `error_user` 点击 Remove 后商品仍保留在购物车 |
| 严重程度 | 严重 |
| 优先级 | P1 |
| 环境 | 账号 `error_user` / `secret_sauce` |
| 复现步骤 | 1. `error_user` 登录 2. Add to cart 某商品 3. 再次点击同一按钮（Remove） 4. 观察角标与按钮文案 |
| 实际结果 | 按钮文案仍为 Remove，购物车角标仍为 1，商品未移除 |
| 预期结果 | 成功移除，角标消失或减 1，按钮恢复为 Add to cart |
| 附件 | `evidence/BUG-003-error_user-remove.png` |
| 状态 | 建议项/已知问题 |

---

## BUG-004 error_user 结账 Finish 无法进入完成页

| 字段 | 内容 |
|------|------|
| 标题 | `error_user` 在 Overview 页点击 Finish 无响应 |
| 严重程度 | 致命（对该账号下单完成路径） |
| 优先级 | P0 |
| 环境 | 账号 `error_user` |
| 复现步骤 | 1. `error_user` 加购并 Checkout 2. 填写合法姓名与邮编 3. Continue 进入 Overview 4. 点击 Finish |
| 实际结果 | URL 仍停留在 `/checkout-step-two.html`，未进入完成页 |
| 预期结果 | 进入 `/checkout-complete.html` 并显示感谢信息 |
| 附件 | `evidence/BUG-004-error_user-finish.png` |
| 状态 | 建议项/已知问题 |

---

## BUG-005 problem_user 结账 Last Name 输入串位

| 字段 | 内容 |
|------|------|
| 标题 | `problem_user` 在结账页填写 Last Name 时写入 First Name，Last Name 仍为空 |
| 严重程度 | 严重 |
| 优先级 | P1 |
| 环境 | 账号 `problem_user`；结账 Step One |
| 复现步骤 | 1. `problem_user` 加购并 Checkout 2. First Name 输入 `Prob` 3. Last Name 输入 `Lem` 4. Postal Code 输入任意值 5. 点击 Continue |
| 实际结果 | First Name 变为 `Lem`，Last Name 为空；提示 `Last Name is required`，无法继续 |
| 预期结果 | 各输入框独立保存对应值，可进入 Overview |
| 附件 | `evidence/BUG-005-problem_user-lastname.png`、`evidence/BUG-005b-problem_user-continue.png` |
| 状态 | 建议项/已知问题 |

---

## 汇总

| 编号 | 严重程度 | 状态 |
|------|----------|------|
| BUG-001 | 严重 | 建议项/已知问题 |
| BUG-002 | 一般 | 建议项/已知问题 |
| BUG-003 | 严重 | 建议项/已知问题 |
| BUG-004 | 致命 | 建议项/已知问题 |
| BUG-005 | 严重 | 建议项/已知问题 |

> 以上均可通过改用 `standard_user` 避开；`standard_user` 主路径 P0 用例全部通过，Day 1 准出按「主账号无致命阻塞」判定通过。
