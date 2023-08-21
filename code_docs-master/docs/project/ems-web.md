---
title: ems-web
order: 1
toc: content
nav:
  title: 项目记录
  order: 6
group: 
  title: 项目记录
  order: 1
---

# 项目记录
-----

## 架构升级如下:
* react升级 15>17         使用hooks
* react-router升级 2>4    hash路由改为/路由，因为特定的部署原因又改回hash路由；
* webpack  升级 3>4       antd,icon/part多个按需加载，自定义主题，配置样式
* babel       升级 6>7    可链式语法等等es10支持
* antdesign  升级 3>4     from表单大改
* 添加css modules(less)         与antd样式冲突
* nodejs运行版本 升级12.18>16.15.1
* 删除不要的引入css,scss,js,jq,bootstrap,img

-----

## 升级的改动 为什么要改？
* 子表单的ref获取;赋值;
* valuePropName="checked" 的改写
* 验证方法;
* getFieldDecorator的替换，name,rules,initialValue；只会对它的直接子元素绑定表单功能
* Form.create()直接去掉；
* 连接redux的{ withRef: true } 直接改为{ forwardRef: true }
* antd图标的替换
* initialValue为变量时候要重新赋值
* 赋值的延迟 定时器解决
* 调用子组件的方法getWrappedInstance()直接去掉
* 路由跳转使用withRouter，去掉contextTypes的定义
* ref="dialogRef" ref值不能为字符串了
* 引入lessmodelus
* 注释了所有的登录失效跳转到登录页面的判断 location.href = '/login';
* 代理了3个类型接口；mapUrl，serviceAddress--》/rest   serviceUrl--》/bods.svc/
* import React3 from 'react-three-renderer'; 不能使用了；
* propTypes 的定义，组件的接受值的类型写法
* _basicForm的使用问题
* 路由懒加载的改动
* 路由结构的参数改动
* 哈希路由改为/路由
* 添加别名安装不同版本的react
* 分开环境的目录url
* 添加别名配置和vscode的别名识别跳转
* WebSocket的NGINX代理配置
* **`使用的不常用的技术：比如WebSocket，文件上传，下载`**


-----

## 部署
* 配合后端打包部署，部署在一起不使用Nginx
* 使用hash路由
* 部署不使用Nginx代理，URL路径写全
* 整和部署方式：和后端一起部署（不使用Nginx），自己单独部署（使用Nginx）---->见diffEvn文件

-----

## 部署调试的步骤：
1. `cd /home/weadmin3.1.2/`
2. `./service.sh stop`
3. `cd /home/weadmin3.1.2/bundle-cache/org.eclipse.osgi/151/0`
> * `rm -rf page ` 
> * `rm -rf page.tar`  
> * `/home/weadmin3.1.2/bundle-cache/org.eclipse.osgi/151/0`  
> * `上传page.tar压缩文件`
4. `tar -xf page.tar`
5. `zip -r bundleFile com/ ico/ META-INF/ OSGI-INF/ page/ plugin.xml`
6. `mv bundleFile.zip bundleFile`
7. `cd /home/weadmin3.1.2/`
8. `./service.sh start`

-----

# 学习

 ## 新技术：
* 项目作为微前端的子应用配置复习,
* 桌面端tauri发布的https问题，安装打包过程；
* 小程序的发布流程:，VR打开外部链接需要配置，地图导航打开第三方app配置，点击打电话，修改uview组件默认样式，小程序（移动端）单位使用？？；
点击图片的指定区域，路由传参参数丢失；微信appid和项目appid需要填（运行》开发预览版》发行》微信开发者工具上传》小程序体验版》提交审核）
* markdown语法
* grafana安装过程
* 部署goview过程，主要是安装mysql，navicat破解版，导入sql文件，连接数据库，修改数据库名称和密码
* web_blog ssr安装与实践
* vue3-egg-test 安装与实践
* taro小程序的使用，下载PDF
* dumi文档静态网站， ~~[代码示例][3]~~
* ~~调试技巧~~
* ~~Windows shell命令~~
* ~~代码规范，检查eslint,格式化~~
* ~~老项目webpack太慢了，升级vite~~
* 前端监控报错，~~监控文档理解~~
* 升级react到17并兼容3d库 react-three-renderer
* 搭建goview开源项目，帮助产品运营的快速实现大屏
* 大屏一键换主题，并使用hooks
* 修改console样式
* 手撸自定义原子css，并去掉没有用的css
* [如果是你前端leader，你会做哪些前端基础建设？][1]
* [centos+jenkins+nginx+gitlab前端自动化部署全记录-cicd][2]
* [怎么制定前端协作规范?][4]

-----
## 重要而不常用
* `node-saas`和`node`的对应关系--->见4个package.json文件
   ```
    yarn add [package] --dev
    yarn add [package] --peer
    yarn add [package] --optional
  ```
* 自定义约定路由配置


-----

 ## React15.6版本3d效果问题：
3d库 react-three-renderer 不更新导致不支持react高版本的问题（**仅支持react15版本**）
解决方法：
1. 别名安装react和react-dom（见package.json文件）
``` JavaScript
// 安装依赖
"react1554": "npm:react@^15.5.4",
"react-dom1554": "npm:react-dom@^15.5.4",
```
2. 修改react-dom和react-three-renderer源码依赖库
见文件夹react-dom/lib 和 react-three-renderer/lib

-----

## 文件资料统计
 * **w文件夹**
 * **谷歌下载**
 * **edge下载**
 * **电脑管家下载**
 * **百度网盘下载**
 * **qq下载**
 * **迅雷下载**

 -----

## nodejs版本从16升级到18问题
`Error: error:0308010C:digital envelope routines::unsupported`

解决添加命令 **`SET NODE_OPTIONS=--openssl-legacy-provider && `**
已经修改了项目有emsh5；qiankun；vue-echarts-master大屏；emsweb

 -----

 ## 项目合集
 * `ems-web`
 * `tauri-antdpro`
 * `web_blog`
 * `vue3-egg-test`
 * `dumi-study`
 * `ems-web-mobile`
 * `uni_ems`
 * `tauri-any-exe`
 * `qiankun`
 * `monitor`
 * `vue-echarts-master`
 * `grafana-8.2.7`
 * `low-code_big-screen`
 * `VRnavigation` ~~小程序二维码~~
 * `cf-seiko-mp`  ~~小程序二维码~~
 * `1.md,ems-web/README.md`
 
 -----

 ## 问题：
 * 数据流redux的使用？？？？
 * antd 继续升级到v5  >>  cssinjs 修改默认样式会有问题？？？？？？？？？？？？？？
 * 国际化翻译有问题？？？ monitornls 编辑监测器才请求？？？？？？？？？？？？？？
 * odata请求库？？？？？？？？？？？？？？
 * moment的时间格式转换
 * 新的东西以后不常用就要记下来
 * **在系统里面使用redux hooks**
 * 循环组装对象  
   ```
   export const alarm_typeData = Object.entries(alarm_typeObj).map(item => ({ "value": item[0], "label": item[1] }))
   ```
 * antd下拉框属性
 ``` JavaScript
 <Select 
    options={tableData} 
    showSearch 
    allowClear 
    fieldNames={{
              label: 'serial_alias',
              value: 'RecId'
    }}
  >
  ```
  * URLSearchParams
  ``` JavaScript
    const params = new URLSearchParams(location.search);
    const params = new URLSearchParams(location.hash.split('?')[1]);
    const pid = params.get("pid");
  ```

  * 代理的拓展
    `const url =  location.origin;`
    有代理就走代理，没代理直接走location.origin+url地址
  



---

 [1]:https://mp.weixin.qq.com/s?__biz=Mzk0NTI2NDgxNQ==&mid=2247489116&idx=1&sn=27b32cab7912fe837dc4d6502dcc6a10&chksm=c319579cf46ede8a362bce85189c5f58525385c28bfe1ffe9bb4fc433f13ca754b4e93b85eab#rd "基础建设"

 [2]:https://mp.weixin.qq.com/s?__biz=Mzk0NTI2NDgxNQ==&mid=2247483730&idx=1&sn=5298f4841241767ca427bef4137b1680&chksm=c3194092f46ec9841051f2c5ea52688db07a50def205e997a6a6b0c1cf1b3c8517267857a156#rd "自动化部署"

 [3]:https://juejin.cn/post/7222804347830206525#heading-32 "dumi 代码示例"

 [4]:https://mp.weixin.qq.com/s?__biz=Mzk0NTI2NDgxNQ==&mid=2247485514&idx=1&sn=3d2237f19081576b4b36da7df29d47e6&chksm=c319498af46ec09c5c28eb60c914c1167e362e4f4fd5e55d4f64e7eb5b8c4fca5ff56a6952b2#rd "协左规范"
 