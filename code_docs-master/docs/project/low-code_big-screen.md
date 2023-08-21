---
title: low-code_big-screen
order: 5
toc: content
nav:
  title: 项目记录
  order: 7
group: 
  title: 项目记录
  order: 1
---


# 安装流程

## 前端

   #### 代码修改
   * .env文件修改 VITE_PRO_PATH
   * proxy修改（开发环境才修改）
   * 登录密码修改为 123123

   ### 环境配置
   * vue3 , vite , node>=16

----

## 后端

   ### 代码修改
   * config/default.js 修改 数据库地址，数据库名称，数据库密码

   #### 环境配置
   * express,mysql,node>16
   * 搭建数据库 mysql >=5.7 
   * `安装navicat破解版,导入sql`  
   * 搭建pm2(生产环境)  **`npm run pm2` 命令牛逼**
   * 切换mysql版本，node版本
   * pm2常见命令

----