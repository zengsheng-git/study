---
title: cypress
order: 8
toc: content
nav:
  title: 项目记录
  order: 7
group: 
  title: 项目记录
  order: 3
---
## 项目路径
D:\w\lmm\lmm-frontend-test

## 查看并调试CI环境中的过去测试结果
https://cloud.cypress.io/organizations/035cef99-9ad9-4d93-96fd-a4a545ad5245/projects
选择qq邮箱登录
1218128305@qq.com
zs199602.123

## cloud.cypress 创建新的项目
- 点击按钮创建
- 会给你一个projectId复制到cypress.config.ts
  `projectId: "9j3d9x"`
- 下一步会给你一个key，添加到package.json脚本
  `"cypress:run": "cypress run  --record --key XXXXXXXXXXXXX"`
- 再运行 `yarn cypress:run` 这时候cloud.cypress 会刷新即可看到新的测试记录在新项目里面

## 分享给他人测试结果
- 把项目设置为公共的，不是私人的
- 直接把一个链接发出去就行了

## 存档之后需要恢复
- https://cloud.cypress.io/projects/{project ID}/runs/{run number}
