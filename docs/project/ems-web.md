---
title: ems-web
order: 1
toc: content
nav:
  title: 项目记录
  order: 6
group: 
  title: 项目记录
  order: 3
---

# 项目记录
-----
## 项目路径
D:\w\ems-web\ems\README.md

## 架构升级如下:   sdsd
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



 -----

## nodejs版本从16升级到18问题
`Error: error:0308010C:digital envelope routines::unsupported`

解决添加命令 **`SET NODE_OPTIONS=--openssl-legacy-provider && `**
已经修改了项目有emsh5；qiankun；vue-echarts-master大屏；emsweb

 -----


 
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
  




 