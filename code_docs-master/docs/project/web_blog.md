---
title: web_blog
order: 10
toc: content
nav:
  title: 项目记录
  order: 6
group: 
  title: 项目记录
  order: 1
---



## 后台管理
* axios接口路径
* 用户名和密码：admin/admin
---
## server端
* 更新了依赖 `"sharp": "^0.32.4"`
* 修改数据库密码
---
## 客户端SSR
* 3316093358@qq.com/admin
* css路径assetPrefix 
* 删掉node-sass依赖 
* axios接口路径
---
## 部署过程
* 修改了ts的类型错误
* 导入sql
* 建表，添加栏目->就是字段
* `yarn install`
* 都是 `npm run dev`
* 部署nextjs(上传所有文件，并安装依赖)
    1. `npm run build`
    2. `pm2 start --name blog-ssr npm -- run start`  
        > 就是执行`npm run start`用pm2管理进程
* **部署server端的生产环境没有成功，依然跑的是 `npm run dev`**  
        > `pm2 start npm -- run dev`

 ---       
 ## pm2 常见命令
 * `npm install -g pm2`
 * `pm2 list`
 * `pm2 start 1`
 * `pm2 restart 1`
 * `pm2 stop 1`
 * `pm2 delete 1`
 * `pm2 log`
 * `pm2 restart dev-server --name newname`
 * `pm2 start npm -- run dev`
 * `pm2 start --name blog-ssr npm -- run start` 

