---
title: ems-cloud
order: 4
toc: content
nav:
 title: 项目记录
 order: 6
group:
 title: 项目记录
 order: 3
---

## 项目路径
D:\w\ems\ems-cloud\readme.md

### 环境变量

- `NODE_ENV` 可 区分是开发环境还是打包环境

### treeDataSimpleMode antd 中 tree 中的属性

### 浏览器自动填充样式修改

```css
// 浏览器自动填充样式修改
input:-webkit-autofill,
textarea:-webkit-autofill,
select:-webkit-autofill {
 // 是使用css3动画将其背景色变化的延迟时间尽可能的延长
 transition: background-color 5000s ease-in-out 0s;
 -webkit-text-fill-color: var(--themeColor);
 caret-color: var(--themeColor); --themeColor); //光标颜色
}
```

### placeholde 样式

```css
.ant-input::-webkit-input-placeholder {
 color: #fff;
 // font-size: 20px;
 text-align: center;
}
```

### 动态电池百分比 svg

- svgDC25 是 js 去计算的
- svg-dc-25 是在 svg 源码中写死的

```css
.svgDC25 {
 .svg-dc-25 {
  fill: '';
 }
 .svg-dc-50 {
  fill: transparent;
 }
 .svg-dc-75 {
  fill: transparent;
 }
 .svg-dc-100 {
  fill: transparent;
 }
}
```

### 解决 echarts 下钻地图，在平移和缩放后，下钻到下一级时生成的地图不在容器中间，会跑到容器外面去。

问题： echart 地图三级下钻地图在平移和缩放后，点击到省，由于中心点的偏移，省跑到容器以外的地方去了，导致新生成的地图看不见。

解决方法：后来发现，是重新绘制图表的时候需要： myChart.setOption(option,true），在 setOption()方法中添加 true，表示重新绘制，最后完美解决。

### **echart 图形与 dom 元素之间的相对单位**

- echarts 图形 使用 **百分比或者 vw 宽，rem 高 （重要）** style={{ width: '64%', height: '69rem', }}
- dom 元素 使用 **百分比 left，rem TOP（重要）** .block4 {top: 54rem;left: 20%;}

### 滚动条样式

```css
body {
 &::-webkit-scrollbar {
  width: 4px;
  // width: 0px;
 }

 &::-webkit-scrollbar-thumb {
  background: var(--themeColor);
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
  opacity: 0.2;
 }

 &::-webkit-scrollbar-track {
  background: #080e2d;
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
 }
}
```

### 修改 antd 默认样式

```css
html {
 --ant-primary-color: var(--themeColor);
}
```

### Animate.css 的使用

- yarn add animate.css
- import 'animate.css';
- 添加动画时长

```css
.myAniDuration500ms {
 animation-duration: 500ms;
}
```

- 示例

```html
<div className="animate__animated animate__zoomIn myAniDuration500ms"></div>
```

## websorct 配置

- 代码

```javascript
const wsType={
  dev:'ws', //http
  test:'ws', //http
  pro:'wss', //https
}
  url: `${wsType[REACT_APP_ENV]}:${window.location.host}/websocket/reportData/${randomKey(10)}`,
```

- NGINX 配置

```
<!-- http -->
   location /websocket/ {
      proxy_pass  http://192.168.110.174:10083;
		    proxy_http_version 1.1;
      proxy_set_header Upgrade websocket;
      proxy_set_header Connection Upgrade;
    }

<!-- https-->
    location /websocket/ {
                        proxy_pass  http://127.0.0.1:8080;
                        proxy_http_version 1.1;
                        proxy_set_header Upgrade websocket;
                        proxy_set_header Connection Upgrade;
                        proxy_set_header Host $host;
                        proxy_set_header X-Real-IP $remote_addr;
                        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                        proxy_set_header X-Forwarded-Proto $scheme;
     }
```

## 统一配置环境变量

https://blog.csdn.net/github_35631540/article/details/107463668

```json
//package.json
 "build:pro": "SET NODE_OPTIONS=--openssl-legacy-provider && cross-env REACT_APP_ENV=pro umi build",
 "build:test": "SET NODE_OPTIONS=--openssl-legacy-provider && cross-env REACT_APP_ENV=test umi build",
 "start": "SET NODE_OPTIONS=--openssl-legacy-provider && set PORT=5080 && cross-env REACT_APP_ENV=dev UMI_ENV=dev UMI_UI=none umi dev",
```

```javascript
 // config.js
  define: {
    'process.env': {
      REACT_APP_ENV: process.env.REACT_APP_ENV,
    },
  },
```

```javascript
// 挂载在Window 全局变量上  直接在业务组件中使用
console.log(REACT_APP_ENV);
```

## 统一配置 API_ENV 环境变量（接口）

- 与上方一致，多添加接口环境变量 API_ENV

## 页面显示打包时间

- 设置

```
<!-- config.js -->
  metas: [
    {
      name: 'buildTime',
      content: moment().format("YYYYMMDDHHmmss")
    },
  ],
```

- 获取 `export const getVersion=()=>'v1.0.0-'+document.querySelector('meta[name=buildTime]').content`

## 报错 EPERM: operation not permitted, unlink 'E:\\code\\xxxxxxxxxx

当前 serve 在另一个项目中在使用，把它关闭以后，重新运行 yarn 命令，就可以了. 我的就是因为另外一个控制台中 yarn dev，没有停止。这个问题产生的原因就是在装包的时候，会删除之前的.bin 文件再重新生成，由于文件被占用导致无法删除文件，因此就会报错，只需要关闭相应的占用程序即可

## nodejs 设置环境变量

```json
    "todeploy": "set BUILD_ENV=1 && node ./deploy/index.js",
    "toupload": "set BUILD_ENV=0 && node ./deploy/index.js",
```

`let isBUILD = process.env.BUILD_ENV == 1;`

## 查询父容器中有多少个子元素

```javascript
// 标记
<div data-divtype="shebei"> </div>;

// 获取
const findDivnum = () => {
 let arr = [];
 for (const it of imgDesWripRef.current.children) {
  if (it.dataset.divtype === 'shebei') {
   arr.push(it);
  }
 }
 return arr.length;
};
```

## 全局配置 antd 属性

```javascript
<ConfigProvider
// renderEmpty={() => <img src={imgE} />}
>
 {/* <BaseLayout> */}
 {children}
 {/* </BaseLayout> */}
</ConfigProvider>
```

## BasicLayoutWrip 样式丢失

因为写在 layouts 里面, 需要 purgecss 添加'./src/layouts/\*_/_.{js,jsx,ts,tsx}'

```javascript
purgecss({
 content: [
  './src/pages/**/*.{js,jsx,ts,tsx}',
  './src/components/**/*.{js,jsx,ts,tsx}',
  './src/layouts/**/*.{js,jsx,ts,tsx}',
 ],
});
```

## echarts 残影

```avascript
/**
           注意： 所有带有尾迹特效的图表需要单独放在一个层，
           也就是需要单独设置 zlevel，同时建议关闭该层的动画（animation: false）。
           不然位于同个层的其它系列的图形，和动画的标签也会产生不必要的残影。
           */
          zlevel: 25,
          animation: false,
```

## redux-persist 添加黑白名单

```javascript
// 这个是redux-persist 的配置
const persistConfig = {
 key: 'root', // 自动框架生产的根目录id 是root。不变
 storage, // 这个是选择用什么存储，session 还是 storage
 // 是/src/models 文件夹下面的文件名
 // whitelist: ["globalModel"], //需要缓存的数据
 blacklist: ['stateModel'], //不需要缓存的数据
};
```

## splice() 会改变原数组，返回的是改变的内容；slice() 不会改变原数组，返回一个新的数组。

## 下拉框失去焦点

```javascript
<Select showSearch ref={SelectRef} />;
SelectRef.current.blur();
```

## Umi 项目集成模式 （在 antdpro 中使用 dumi 框架编写 markdown 文档）

- 打包命令,默认不会打包到生产环境，需要单独打包：`"build:dumi": "SET NODE_OPTIONS=--openssl-legacy-provider && umi build --dumi"`
- 默认 dev 也会跑 dumi 文档，单独跑 dumi 文档命令：`"start:dumi": "SET NODE_OPTIONS=--openssl-legacy-provider && set PORT=5082 && umi dev --dumi",` 除了独立的组件库以外，我们大多数的项目还会有自己的内部组件，这些内部的组件库管理通常是一个很头疼的问题，既不需要发布单独的 npm 包，又需要进行迭代、更新、说明、交接；为了让项目内部组件库管理这件事变得更加轻松，dumi 推出了 Umi 项目集成模式：

- 自动探测：当 dependencies 或 devDependencies 中包含 umi 和 @umijs/preset-dumi 时，进入集成模式（不再需要单独安装 dumi 这个包）
- 相互隔离：所有 dumi 文档都会集中在 /~docs 路由下，与原项目相互隔离、互不干扰，可以理解为标准 dumi 文档都加了一个特定路由前缀，也包括用户的导航和菜单路由配置
- 不影响生产：仅在 NODE_ENV 是 development 时集成，不影响项目的生产构建
- 可单独构建：如果需要单独构建文档做部署，可执行 umi build --dumi，即可得到一份非集成模式的 dumi 站点产物，--dumi 在 umi dev 命令下也是可用的
- 使用方式很简单：在已有 Umi 项目中安装 @umijs/preset-dumi 到 devDependencies 中，再根据需要配置 resolve.includes 即可（比如约定 src/components 目录下为业务组件库和组件库对应的文档）。

## 使用 echarts 属性 graphic 无数据展示

```javascript
import notDataimg from '../../public/1.png';
export const chartNotData = (invisible, mes) => {
 return {
  graphic: [
   {
    type: 'group',
    left: 'center',
    top: '40%',
    // left: '45%',
    // top: '42.5%',
    children: [
     {
      // z:4,
      type: 'image',
      invisible,
      id: 'noData',
      top: -44,
      left: -24,
      rotation: 0, //旋转
      // origin: [64.5, 32.5],//中心点
      // scale: [1.0, 1.0],//缩放
      style: {
       image: notDataimg,
       // width: 129,
       // height: 65,
       opacity: 1,
      },
     },
     {
      type: 'text',
      invisible,
      z: 100,
      // top: -22,
      // left: "center",
      style: {
       fill: '#00D3FF',
       fontWeight: 'normal',
       fontSize: 16,
       textAlign: 'center',
       text: [mes || '暂无数据', ''].join('\n'),
      },
     },
    ],
   },
  ],
 };
};
```

## DOMException: Failed to execute 'send' on 'WebSocket': Still in CONNECTING state.

```javascript
//这样问题的原因就很明显了，之所以数据不能发送出去，是因为 websocket 还处在“CONNECTING”状态下，连接还没有成功
if (ws.current?.readyState == 1) {
 ws.current?.send(str);
}
```

## classnames 的使用

```javascript
const arr = ['b', { c: true, d: false }];
// => 'a b c e'
const class_name = classNames('a', arr, { e: true }, { f: false });

<div className={class_name}></div>;
```

## redux 存储公共函数 在任意组件中调用
``` js
       // 设置
       Dispatch({
          type: 'functionModel/loadMapFnSet',
          payload: loadMap,
        });
       // 获取
       const  {loadMapFn}  = useSelector((state: any) =>state.functionModel);
       // 调用
        <div onClick={()=>loadMapFn(china, 'china')}>
        
        </div>
```

## 升级到 umi/max

- `esbuildMinifyIIFE: true` 由于 Umi 4 默认使用 esbuild 作为压缩器，该压缩器会自动注入全局变量作为 polyfill ，这可能会引发 异步块全局变量冲突、 qiankun 子应用和主应用全局变量冲突 等问题，通过打开该选项或切换 jsMinifier 压缩器可解决此问题
- 不兼容 ie11 了

```json
// targets: {
 //   ie: 11,
 // },
```

- 固定版本 `inquirer@^8.0.0`
- 点击导航会闪一下
- tuobu.tsx 数据需要深度 clone
- 表格 数据不准需要深度 clone
- 首页数据详情不准 ，没找到问题

- 版本跟换： 替换 依赖，config， BaseLayout.tsx 文件

## umi 特性

- 文件系统路由和权限
- 全局状态 usemodel
- 加载 loading，切换页面和未加载时候

## 待处理

- ~~熟练使用 ahooks 库~~
- ~~Commitizen git 提交辅助~~
- ~~Tailwind css 设置 rem~~
- ~~svg 的基础理解动画线条~~
- ~~改成微前端架构~~
- ~~使用 antdesign V5,样式大问题，已修改的和未修改的~~
- ~~升级到 umi4，antdV5~~
- ~~使用 nextjs13 管理系统~~
- ~~通读 react 官方文档~~
- ~~ts 编译不通过时候的报错提示，和 ts 的使用~~
- ~~函数的注释~~
- ~~接口的多个请求，比如获取使能在设置里面要写，在首页里面也要写,redux 没有的时候就请求，有的时候就去取~~
- 通用组件，公共组件
- 导航菜单的动态显示隐藏 access.ts 使用的是 localStorage,登录之后存的数据是否有意义
- 用户，角色，用户组首页一模一样
- 组织机构，资源管理首页一模一样
- 高度自适应
- 表单文件上传的校验
- 背景色，字体颜色的统一(~~css~~ 和 js 中) ， 自定义菜单的权限 ， antd 自定义主题,流线图重写
- 为什么重新渲染
- git 提交和部署 多种自定义命令的使用
- nextjs 客户端渲染
- 项目难点回顾 ： 自己划线动画 rc-tween-one ，和 原生 svg ，svgjs , echarts 的两个案例（流动和拖拽） 插件的使用
- 项目难点回顾 ： **_需要有尾迹动画_**
- 权限的匹配规则 md
- classnames lodash 的 常用方法 使用
- 大屏项目的改变后的数据存储为 json
- 全部使用 dispatch，包含持久化和非持久化
- 验证 useModel 的错误
- happy-birthday-master : card2 , brother , mobile , \happybirthday\yanHuang,likeU
- 分支的东西
- 大屏项目的三个版本
- lmm 项目 : umi4,
- psa(carbon) :umi4,cra,react+vite 的使用
- 该项目的数据复制，便于以后观察学习
