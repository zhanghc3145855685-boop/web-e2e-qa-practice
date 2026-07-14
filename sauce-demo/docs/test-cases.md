# Sauce Demo 测试用例与执行结果

| 项 | 内容 |
|----|------|
| 文档版本 | v0.1（Day 1） |
| 执行日期 | 2026-07-14 |
| 环境 | Windows 10/11 + Chrome/Chromium；https://www.saucedemo.com/ |
| 主账号 | `standard_user` / `secret_sauce` |

**状态取值：** 通过 / 失败 / 阻塞  
**优先级：** P0 主路径必测；P1 重要；P2 一般

---

## A. 登录

| 编号 | 模块 | 标题 | 前置条件 | 步骤 | 预期结果 | 优先级 | 实际结果 | 状态 |
|------|------|------|----------|------|----------|--------|----------|------|
| TC-LOGIN-001 | 登录 | 正确账号密码登录成功 | 打开登录页 | 1. 输入 `standard_user` 2. 输入 `secret_sauce` 3. 点击 Login | 进入 `/inventory.html`，标题 Products | P0 | 跳转商品列表，标题为 Products | 通过 |
| TC-LOGIN-002 | 登录 | 错误密码登录失败 | 打开登录页 | 1. 输入 `standard_user` 2. 输入错误密码 3. 点击 Login | 停留登录页，显示用户名/密码不匹配错误 | P0 | 提示：`Username and password do not match any user in this service` | 通过 |
| TC-LOGIN-003 | 登录 | 空用户名登录失败 | 打开登录页 | 1. 用户名为空 2. 输入密码 3. 点击 Login | 提示 Username is required | P0 | 提示：`Username is required` | 通过 |
| TC-LOGIN-004 | 登录 | 空密码登录失败 | 打开登录页 | 1. 输入用户名 2. 密码为空 3. 点击 Login | 提示 Password is required | P0 | 提示：`Password is required` | 通过 |
| TC-LOGIN-005 | 登录 | locked_out_user 无法登录并有提示 | 打开登录页 | 1. 输入 `locked_out_user` 2. 输入 `secret_sauce` 3. 点击 Login | 无法进入商品页，提示账号被锁定 | P0 | 提示：`Sorry, this user has been locked out.` | 通过 |
| TC-LOGIN-006 | 登录 | 非法用户名登录失败 | 打开登录页 | 1. 输入不存在的用户名 2. 输入 `secret_sauce` 3. 点击 Login | 登录失败并有错误提示 | P1 | 提示：`Username and password do not match any user in this service` | 通过 |
| TC-LOGIN-007 | 登录 | 用户名和密码均为空 | 打开登录页 | 1. 不填任何字段 2. 点击 Login | 提示 Username is required | P1 | 提示：`Username is required` | 通过 |

---

## B. 商品列表

| 编号 | 模块 | 标题 | 前置条件 | 步骤 | 预期结果 | 优先级 | 实际结果 | 状态 |
|------|------|------|----------|------|----------|--------|----------|------|
| TC-INV-001 | 商品列表 | 商品列表正常展示 | `standard_user` 已登录 | 1. 查看 Inventory 页 | 展示多个商品，含名称与价格 | P0 | 展示 6 个商品，名称与 `$` 价格均正常 | 通过 |
| TC-INV-002 | 商品列表 | 排序名称 A-Z | 已登录商品页 | 1. 排序选择 Name (A to Z) | 商品名按字母升序 | P1 | 顺序正确（A→Z） | 通过 |
| TC-INV-003 | 商品列表 | 排序名称 Z-A | 已登录商品页 | 1. 排序选择 Name (Z to A) | 商品名按字母降序 | P1 | 顺序正确（Z→A） | 通过 |
| TC-INV-004 | 商品列表 | 排序价格低到高 | 已登录商品页 | 1. 排序选择 Price (low to high) | 价格升序 | P1 | 价格升序正确 | 通过 |
| TC-INV-005 | 商品列表 | 排序价格高到低 | 已登录商品页 | 1. 排序选择 Price (high to low) | 价格降序 | P1 | 价格降序正确 | 通过 |
| TC-INV-006 | 商品列表 | 点击商品进入详情 | 已登录商品页 | 1. 点击任一商品名称 2. 查看详情 3. Back to products | 进入详情页，信息一致，可返回列表 | P1 | 进入详情，名称一致，可返回 | 通过 |

---

## C. 购物车

| 编号 | 模块 | 标题 | 前置条件 | 步骤 | 预期结果 | 优先级 | 实际结果 | 状态 |
|------|------|------|----------|------|----------|--------|----------|------|
| TC-CART-001 | 购物车 | 加入购物车 | 已登录，购物车为空 | 1. 点击某商品 Add to cart | 按钮变为 Remove，角标显示 1 | P0 | 角标为 1 | 通过 |
| TC-CART-002 | 购物车 | 购物车数量变化 | 已有 1 件在车中 | 1. 再添加另一商品 | 角标变为 2 | P0 | 角标变为 2 | 通过 |
| TC-CART-003 | 购物车 | 移除商品 | 车中有 2 件 | 1. 在列表页点击 Remove | 角标减 1，对应商品可再加购 | P0 | 移除后角标为 1 | 通过 |
| TC-CART-004 | 购物车 | 从购物车进入结账 | 车中至少 1 件 | 1. 打开购物车 2. 点击 Checkout | 进入结账 Step One | P0 | 进入 `/checkout-step-one.html` | 通过 |
| TC-CART-005 | 购物车 | Continue Shopping 返回商品页 | 位于购物车页 | 1. 点击 Continue Shopping | 返回 `/inventory.html` | P2 | 返回商品列表 | 通过 |

---

## D. 结账与订单

| 编号 | 模块 | 标题 | 前置条件 | 步骤 | 预期结果 | 优先级 | 实际结果 | 状态 |
|------|------|------|----------|------|----------|--------|----------|------|
| TC-CHK-001 | 结账 | 必填项为空拦截 | 进入结账 Step One | 1. 不填任何信息 2. 点击 Continue | 拦截并提示必填（如 First Name） | P0 | 提示：`First Name is required` | 通过 |
| TC-CHK-002 | 结账 | 取消结账返回购物车 | 位于结账 Step One | 1. 点击 Cancel | 返回购物车页 | P1 | 返回 `/cart.html` | 通过 |
| TC-CHK-003 | 结账 | 填写正确信息完成下单 | 车中有商品 | 1. Checkout 2. 填写姓名与邮编 3. Continue 4. Finish | 到达订单完成页 | P0 | 成功到达 `/checkout-complete.html` | 通过 |
| TC-CHK-004 | 结账 | 订单完成页信息正确 | 刚完成下单 | 1. 查看完成页文案 | 显示感谢信息（Thank you…） | P0 | 显示 `Thank you for your order!` | 通过 |
| TC-CHK-005 | 结账 | 完成后返回商品页 | 位于完成页 | 1. 点击 Back Home | 返回商品列表 | P1 | 返回 `/inventory.html` | 通过 |
| TC-CHK-006 | 结账 | 登出成功 | 已登录 | 1. 打开侧边菜单 2. 点击 Logout | 回到登录页 | P0 | 回到登录页，Login 按钮可见 | 通过 |

---

## E. 其他

| 编号 | 模块 | 标题 | 前置条件 | 步骤 | 预期结果 | 优先级 | 实际结果 | 状态 |
|------|------|------|----------|------|----------|--------|----------|------|
| TC-OTH-001 | 会话 | 未登录直接访问内部页被拦截 | 无有效会话（新隐私窗口/清空存储） | 1. 直接访问 `/inventory.html` | 无法浏览商品，回到登录页 | P0 | 新会话下重定向至登录页（见 `evidence/TC-OTH-001-fresh-context.png`） | 通过 |
| TC-OTH-002 | 会话 | 刷新页面后会话保持 | `standard_user` 已在商品页 | 1. 刷新浏览器 | 仍停留在商品页且无需重新登录 | P2 | 刷新后仍在 `/inventory.html`，Products 可见 | 通过 |
| TC-OTH-003 | 端到端 | 主流程端到端走通 | 可访问演示站 | 登录→加购→Checkout→Finish→登出 | 各步骤成功，最终回到登录页 | P0 | 全流程走通 | 通过 |

---

## 执行说明

- 执行顺序：先全部 P0，再 P1/P2。
- `problem_user` / `error_user` 相关异常表现记入缺陷清单，不单独另开用例编号（避免与演示「刻意坏账号」混淆统计口径）。
- 失败/缺陷截图目录：`evidence/`。
