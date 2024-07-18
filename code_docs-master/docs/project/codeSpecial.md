---
title: codeSpecial
order: 11
toc: content
nav:
 title: 项目记录
 order: 6
group:
 title: 项目记录
 order: 1
---

# [代码规范 & 详细解释 husky、prettier、eslint、lint-staged 的作用和使用][1]

参考：

- [前端工程化:配置 React+ts 企业级代码规范及样式格式和 git 提交规范][2]
- [开启高效前端规范开发之旅！ESLint + Prettier + husky +Commitizen][3]

---

```sh
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"
# 注释
# npm run prettier:check && git add -A .
# 注释
# npm run eslint:check
# 注释
# npx lint-staged
# npx --no-install lint-staged   用于在不安装 lint-staged 的情况下运行该工具
```

---

## .editorconfig

- 安装插件`EditorConfig for VS Code`

```sh
    # http://editorconfig.org
    root = true

    [*]
    indent_style = space
    indent_size = 2
    end_of_line = lf
    charset = utf-8
    trim_trailing_whitespace = true
    insert_final_newline = true

    [*.md]
    trim_trailing_whitespace = false
    indent_size = 1

    [*.{scss,less,css}]
    indent_size = 2

    [*.{js,jsx,ts,tsx}]
    indent_size = 4

    [Makefile]
    indent_style = tab

```

## husky

- 安装 npm 包
- 提示：所有钩子默认情况下是禁用的
- pre-commit 钩子会在 commit 前触发
- pre-push 会在 push 前触发。
- 利用 pre-commit 钩子在 commit 时对代码先进行 eslint 检查，如果不合格就不给 commit，不过使用 git 钩子稍微麻烦，于是就有了 husky 。

## prettier

- 安装 vscode 插件`Prettier - Code formatter`
- 检查和修复
- **在代码保存时进行格式化与检查,保存自动格式化代码**
- 来检查代码格式是否合格
- 添加.vscode/settings.json 来支持保存后触发格式化
  ```json
  {
   "editor.formatOnSave": true
  }
  ```

## eslint

- 安装 vscode 插件`ESLint`
- 安装 npm 包
- 检查和修复
- 可以对代码进行约束规范，如果代码不符合规范则会在下面呈现一条 ~~~~ 红色的波浪线，
- 代码规范检查

## lint-staged

- 安装 npm 包
- 上面的插件都需要指定文件才能进行检查，比如 eslint 命令需要指定 src/\*.js ，但这样会产生新的问题，如果 src 目录存在着大量的 .js 文件，那么每次执行 eslint 时都会对所有文件检查&修复，很明显除了对性能有影响外，还会影响同事以前写过的代码格式。
- 只检查&修复我们修改过的文件，能让这些插件只扫描暂存区的文件而不是全盘扫描

## Stylelint

- 安装 vscode 插件`Stylelint`
- 安装 npm 包

---

[1]: https://blog.csdn.net/cookcyq__/article/details/125457031 '代码规范 & 详细解释 husky、prettier、eslint、lint-staged 的作用和使用'
[2]: https://juejin.cn/post/7101596844181962788#heading-38 '前端工程化:配置React+ts企业级代码规范及样式格式和git提交规范'
[3]: https://mp.weixin.qq.com/s/0q13PZ6vNxrbrpuxQxxt-g '开启高效前端规范开发之旅！ESLint + Prettier + husky +Commitizen'
