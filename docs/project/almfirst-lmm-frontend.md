---
title: almfirst-lmm-frontend-1.0
order: 1
toc: content
nav:
  title: 项目记录
  order: 6
group: 
  title: 项目记录
  order: 3
---

## 项目路径
D:\w\lmm\almfirst-lmm-frontend

## 线上服务器界面用户密码
<!-- jzhang@almfirst.com
S1tev1ew -->

## 服务器密码
root
siteview
## 面板信息
- 帮助命令
`bt`
- 地址
https://10.0.8.18:39159/cbf96ef1
- 密码
iqhbpsqg
123456

## 命令式上传文件
- 依赖
``` json
    "inquirer": "^8.0.0",
    "ora": "^4.0.3",
    "node-ssh": "^7.0.0",
    "archiver": "^3.1.1",
    "chalk": "^3.0.0",
```
## 发送到钉钉机器人
- 依赖
``` json
    "dingtalk-robot-sender": "^1.2.0",
```

## "type": "module" 会报错  require is not defined in ES module scope, you can use import instead
- 文件名全改为.cjs

## 合并分支
- git pull 
- git merge origin/dev
- git add .
- git commit -m "xxx"
- git push

## change事件与input事件的区别在于
- change事件在输入框失去焦点后才会触发
- 而input事件在用户输入时即可触发。

## 手写Vue3中的表单验证
- https://blog.csdn.net/aahwj/article/details/135257788#:~:text=%E5%9C%A8Vue3%E4%B8%AD%EF%BC%8C,%E8%A1%A8%E5%8D%95%E9%AA%8C%E8%AF%81%20%E5%8F%AF%E4%BB%A5%E4%BD%BF%E7%94%A8Vue%E7%9A%84%E5%86%85%E7%BD%AE%E6%8C%87%E4%BB%A4v-model%E5%92%8C%E8%87%AA%E5%AE%9A%E4%B9%89%E6%8C%87%E4%BB%A4%E6%9D%A5%E5%AE%9E%E7%8E%B0%E3%80%82


## 路由重定向
``` js
        {
            path: "/",
            name: "home",
            redirect:'/lmm/forecast-setup/institutions'
        }

```

## 监听一下路由的变动
``` js
onBeforeRouteUpdate(async (to, from) => {
    if (to.params.institutionId !== from.params.institutionId) {
    }
});

```

## 文件流下载需要token
- https://zhuanlan.zhihu.com/p/350069246
- responseType: 'blob'  在导出的接口加上声明接收参数 最后一个参数就是指定类型为 blob 或者 arraybuffer

## 【axios 使用】下载文件流 以及 获取响应头header content-disposition 中的文件名
- https://blog.csdn.net/m0_53584457/article/details/130527033
- https://blog.csdn.net/GYB4979/article/details/127424021
## vue3 文件上传支持点击/粘贴/拖拽 
- https://blog.csdn.net/Jie0817/article/details/133312171


## axios  timeout: 50000,
- 设置了在5000毫秒内请求数据 如果没有请求成功就执行错误函数

## 项目需求，鼠标悬浮在div上时出现弹框信息，on关联mouseover事件时，出现悬浮框一直不停闪烁，是因为频繁触发了mouseover和mouseout事件，
-https://blog.csdn.net/qq_42627162/article/details/111941690#:~:text=%E9%A1%B9%E7%9B%AE%E9%9C%80%E6%B1%82%EF%BC%8C%E9%BC%A0%E6%A0%87%E6%82%AC%E6%B5%AE%E5%9C%A8div%E4%B8%8A%E6%97%B6%E5%87%BA%E7%8E%B0%E5%BC%B9%E6%A1%86%E4%BF%A1%E6%81%AF%EF%BC%8Con%E5%85%B3%E8%81%94mouseover%E4%BA%8B%E4%BB%B6%E6%97%B6%EF%BC%8C%E5%87%BA%E7%8E%B0%E6%82%AC%E6%B5%AE%E6%A1%86%E4%B8%80%E7%9B%B4%E4%B8%8D%E5%81%9C%E9%97%AA%E7%83%81%EF%BC%8C%E6%98%AF%E5%9B%A0%E4%B8%BA%E9%A2%91%E7%B9%81%E8%A7%A6%E5%8F%91%E4%BA%86mouseover%E5%92%8Cmouseout%E4%BA%8B%E4%BB%B6%EF%BC%8C%E8%A7%A3%E5%86%B3%E5%8A%9E%E6%B3%95%EF%BC%9A%E5%9C%A8%E6%82%AC%E6%B5%AE%E6%A1%86%E5%85%83%E7%B4%A0%E4%B8%AD%E5%8A%A0%E5%85%A5css%E6%A0%B7%E5%BC%8F%EF%BC%9Apointer-events%3A,none%3B%E8%AF%A5%E6%A0%B7%E5%BC%8F%E9%98%BB%E6%AD%A2%E6%82%AC%E6%B5%AE%E5%B1%82%E6%88%90%E4%B8%BA%E9%BC%A0%E6%A0%87%E4%BA%8B%E4%BB%B6%E7%9A%84target%EF%BC%8C%E7%A9%BF%E9%80%8F%E6%82%AC%E6%B5%AE%E7%AA%97%E6%9D%A5%E6%8C%87%E5%AE%9A%E5%8E%9F%E5%A7%8B%E7%BB%91%E5%AE%9Amouseout%E5%92%8Cmouseover%E7%9A%84div%E3%80%82
## setup 语法，模版语法
- 父传值给子
- 子调用父函数
- 阻止事件冒泡 
``` js
    e.preventDefault();
    e.stopPropagation();
```
- 计算属性
- 路由跳转
- 插槽类似react的 props.children
- 在路由文件中使用 pinia https://blog.csdn.net/zlting_/article/details/127495583

- `!z-0`
``` css
  z-index: 0 !important;
```

## 测试框架 cypress
- 安装 npm 包就行
``` json
"@cypress/vue": "^6.0.0",
"cypress": "^13.7.0",
"cypress-file-upload": "^5.0.8",
```
- 配置 cypress.config.ts 
- 复制 tsconfig.json 文件
- 配置 .gitignore 忽略
``` file
/cypress/videos/
/cypress/screenshots/
/cypress/report/
```
- 运行 `yarn cypress:open`

## cypress 生成测试报告
- 在以cypress run运行时，如果出现失败，会自动进行截图，并保存至默认目录：cypress\screenshots和cypress\videos。在使用cypress open 不会自动截图。
- 参考链接 https://blog.csdn.net/weixin_39929465/article/details/111852768
- 安装 npm 包就行
```json
  "mocha": "^10.3.0",
  "mochawesome": "^7.1.3",
  "mochawesome-merge": "^4.3.0",
  "mochawesome-report-generator": "^6.2.0",
```
- 配置 cypress.config.ts 
- 命令 `yarn cypress:run`
- 报告在 `cypress/reports` 目录下
- 错误截屏在 `cypress/screenshots` 目录下
- 错误录屏在 `cypress/videos` 目录下



## 提交代码自动格式化
- 添加依赖 和 prettier规则，prettier忽略规则
``` json
"prettier": "^3.2.4",
"husky": "^7.0.4",
"lint-staged": "^15.2.2",
```
- 添加命令
``` json
        "prepare": "husky install",
        "lint-staged": "lint-staged",
```
- 添加lint-staged规则
``` json
 "lint-staged": {
        "**/*.{js,jsx,tsx,ts,less,md,json,scss,vue,css}": [
            "prettier --write",
            "git add"
        ]
    },
```
- 在 `.husky` 文件夹 添加 `pre-commit` 文件
``` sh
#!/bin/sh
. "$(dirname "$0")/_/husky.sh"
npx --no-install lint-staged
```


## 指定容器div滚动到指定位置 (overflow-y-auto h-[540px])
``` html
<div ref="scrollDiv" class="flex  flex-col items-center gap-5 overflow-y-auto h-[540px]"></div
```
``` js
const scrollDiv = ref(null)

const scrollToBottom = () => {
    setTimeout(() => {
        let scrollElem = scrollDiv.value;
        scrollElem.scrollTop = scrollElem.scrollHeight;
    }, 100);
};
```


## 待办事项
- 文件上传请求的统一
- 3个ID 的统一，和记录



7dFhJ9GnM3t8WsRpU2x5e0z4c1v6bQaY
fd8dc99983fe4f5695237e2e3b0418fd
8dd7d2057a794cebadc7d34390d97b12


https://almfirst-lmm.greentree-33a1fcd5.centralus.azurecontainerapps.io/lmm/auth/login/ALMFirst/Admin/admin?redirectUrl=https://lmm.dnet.us&token=xxxxxxx


渠先生的简历

表格主题
编辑框在里面
