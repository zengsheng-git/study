---
title: study
order: 1
toc: content
nav:
 title: 项目记录
 order: 6
group:
 title: 项目指引
 order: 1
---

# 学习

## 新技术：

- 项目作为微前端的子应用配置复习,~~记录 md 文件~~
- 桌面端 tauri 发布的 https 问题，安装打包过程；
- 小程序的发布流程:，VR 打开外部链接需要配置，地图导航打开第三方 app 配置，点击打电话，修改 uview 组件默认样式，小程序（移动端）单位使用？？；点击图片的指定区域，路由传参参数丢失；微信 appid 和项目 appid 需要填（运行》开发预览版》发行》微信开发者工具上传》小程序体验版》提交审核）
- markdown 语法
- grafana 安装过程
- 部署 goview 过程，主要是安装 mysql，navicat 破解版，导入 sql 文件，连接数据库，修改数据库名称和密码
- web_blog ssr 安装与实践
- vue3-egg-test 安装与实践
- taro 小程序的使用，下载 PDF 等等，~~关键代码的记录到 md~~
- dumi 文档静态网站， ~~[代码示例][3]~~
- ~~调试技巧~~
- ~~Windows shell 命令~~
- ~~代码规范，检查 eslint,格式化~~
- ~~老项目 webpack 太慢了，升级 vite~~
- 前端监控报错，~~监控文档理解~~
- 升级 react 到 17 并兼容 3d 库 react-three-renderer
- 搭建 goview 开源项目，帮助产品运营的快速实现大屏
- ~~大屏一键换主题，并使用 hooks~~
- 修改 console 样式
- [使用钉钉接收 gitlab 仓库的推送消息][10]
- 使用命令一键提交代码到 git `npm run topush "fix: 提交信息" todeploy`
- 命令式一键部署,自定义更新内容并自动推送到钉钉信息 ~~每次删除原有的文件，对比 Jenkins,~~
  1. `npm i fe-deploy-cli -g`
  2. `deploy -V`
  3. `deploy init` 生成 `deploy/deploy.config.js`
  4. `deploy --help`
  5. `deploy test`
- 手撸自定义原子 css，并去掉没有用的 css，
- [如果是你前端 leader，你会做哪些前端基础建设？][1]
- [centos+jenkins+nginx+gitlab 前端自动化部署全记录-cicd][2]
- [怎么制定前端协作规范?][4]
- [就是一个基于 Axios 的完美的双 token 无感刷新][5]
- [基于 Axios 二次封装请求库,带你重构面试亮点][7]
- [css 新特性][6]
- [前端最能打的本地存储方案][8]
- [【前端工程化】使用 verdaccio 搭建公司 npm 私有库完整流程和踩坑记录][9]
- 自定义约定路由配置
- 代码规范 & 详细解释 husky、prettier、eslint、lint-staged 的作用和使用
- ~~canvas 库 fabricJs,svg~~
- ~~安装的 vscode 插件集合~~

---

## 重要而不常用

- `node-saas`和`node`的对应关系--->见 4 个 package.json 文件
  ```
   yarn add [package] --dev
   yarn add [package] --peer
   yarn add [package] --optional
  ```

## 项目合集

- `ems-web`
- `tauri-antdpro`
- `ems-cloud`
- `ballcat-ui-react-main`
- `carbon-example/carbon-max`
- `web_blog`
- `vue3-egg-test`
- `dumi-study`
- `fe-deploy-cli-master`
- `ems-web-mobile`
- `uni_ems`
- `tauri-any-exe`
- `qiankun`
- `monitor`
- `vue-echarts-master`
- `front-end-data-visualization-master`
- ~~`grafana-8.2.7`~~
- `low-code_big-screen`
- `VRnavigation` ~~小程序二维码~~
- `cf-seiko-mp` ~~小程序二维码~~
- `uni-vue3` ~~小程序二维码~~
- `1.md,ems-web/README.md`

## 文件资料统计

- **w 文件夹**
- **谷歌下载**
- **edge 下载**
- **电脑管家下载**
- **百度网盘下载**
- **qq 下载**
- **迅雷下载**
- **微信下载**

---

[1]: https://mp.weixin.qq.com/s?__biz=Mzk0NTI2NDgxNQ==&mid=2247489116&idx=1&sn=27b32cab7912fe837dc4d6502dcc6a10&chksm=c319579cf46ede8a362bce85189c5f58525385c28bfe1ffe9bb4fc433f13ca754b4e93b85eab#rd '基础建设'
[2]: https://mp.weixin.qq.com/s?__biz=Mzk0NTI2NDgxNQ==&mid=2247483730&idx=1&sn=5298f4841241767ca427bef4137b1680&chksm=c3194092f46ec9841051f2c5ea52688db07a50def205e997a6a6b0c1cf1b3c8517267857a156#rd '自动化部署'
[3]: https://juejin.cn/post/7222804347830206525#heading-32 'dumi 代码示例'
[4]: https://mp.weixin.qq.com/s?__biz=Mzk0NTI2NDgxNQ==&mid=2247485514&idx=1&sn=3d2237f19081576b4b36da7df29d47e6&chksm=c319498af46ec09c5c28eb60c914c1167e362e4f4fd5e55d4f64e7eb5b8c4fca5ff56a6952b2#rd '协作规范'
[5]: https://mp.weixin.qq.com/s?__biz=Mzg5ODA5NTM1Mw==&mid=2247501075&idx=1&sn=f7a81ef54e9a75b52a310b2e54043712&chksm=c0654485f712cd932e9cd949d1e37bd44672ed17b7d70f68cad74d35913c6969e8797886bd44&mpshare=1&scene=24&srcid=082685uAmWg5qCboKPD1qfzh&sharer_sharetime=1693050648436&sharer_shareid=d0b6f47fad4bd7c2e575b22646a6eb1a#rd '基于Axios的完美的双token无感刷新'
[6]: https://mp.weixin.qq.com/s?__biz=MzA5MjQwMzQyNw==&mid=2650767684&idx=1&sn=4c08a97c082e15e6ae59ed9e2a5d6df0&chksm=886682c8bf110bde0997454a59115e7454133aeda8ee2af023f27afa587ad2ee1bf8ecd8642d&mpshare=1&scene=24&srcid=0827lLuOtNKbcLqXK3mP2RVl&sharer_sharetime=1693151494348&sharer_shareid=d0b6f47fad4bd7c2e575b22646a6eb1a#rd 'css新特性'
[7]: https://juejin.cn/post/7266308603938062391?searchId=20230920103646EAE35E6F327D2A799574#heading-9 '基于Axios二次封装请求库'
[8]: https://mp.weixin.qq.com/s/FVpa-8izlbwha063ZeN3TA '前端最能打的本地存储方案'
[9]: https://juejin.cn/post/7096701542408912933 '【前端工程化】使用verdaccio搭建公司npm私有库完整流程和踩坑记录'
[10]: https://www.codenong.com/cs109489923/ '使用钉钉接收gitlab仓库的推送消息'
