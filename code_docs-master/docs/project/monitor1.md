---
title: monitor1
order: 4
toc: content
nav:
  title: 项目记录
  order: 6
group: 
  title: 进阶项目
  order: 2
---

## 待完成
* 打包构建自动上传source-map 参考 vue3项目
* 数据的展示在后台管理
* 封装成SDK接入，参考 “资料-前端监控SDK实战项目”

## 注意事项
* 只有js错误和promise错误才能捕捉到某行
* 资源加载错误捕获不了到某行
* 后台接口启动命令 `nodemon app.js`
* 前台启动命令 `yarn start`
* 前台构建打包命令 `yarn build`
* 开发环境自带source-map,上传的日志都是nodemodules中的
* 生产环境带上source-map,上传的日志都是nodemodules中的
* 生产环境不带source-map,把source-map上传到 /server/source/ 文件夹下，可捕获到具体错误行号
