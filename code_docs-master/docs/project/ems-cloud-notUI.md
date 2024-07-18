---
title: ems-cloud
order: 3
toc: content
nav:
 title: 项目记录
 order: 6
group:
 title: 项目记录
 order: 1
---

# 项目
## 项目路径
D:\w\ems-cloud-notUI\ems-cloud\project.md

### hover 加上 border 之后页面会抖动

1. 使用 outline 代替 border： outline 不会在元素的盒模型内增加额外的空间，因此不会导致布局变化

```css
.element:hover {
 outline: 1px solid black;
}
```

2. 使用 box-shadow 代替 border： box-shadow 同样不会增加额外的空间，并且可以在不影响布局的情况下实现类似于 border 的效果。

```css
.element:hover {
 box-shadow: 0 0 0 1px black;
}
```

3. 预先定义 border 属性： 如果你在 hover 状态下使用的边框颜色和元素默认的边框颜色相同，你可以在元素的默认样式中定义边框，以避免在 hover 时出现布局变化。

```css
.element {
 border: 1px solid transparent; /* 或者与 hover 状态下相同的颜色 */
}
.element:hover {
 border-color: black; /* 或者你想要的颜色 */
}
```

4. 使用 transition 属性： 通过在边框属性上添加 transition，你可以使边框的出现和消失更加平滑，从而减少抖动。

```css
.element {
 transition: border 0.3s ease;
}
.element:hover {
 border: 1px solid black;
}
```

### 点击变色封装 `activeDiv === item.key`

### tailwind vscode 样式提示

1. 安装*Tailwind CSS IntelliSense*插件；
2. 类名前面添加一个空格，就会有提示了

- 视口高度 `h-screen/80`
  ```javascript
  extend: {
      // 使用 h-screen/80
      height: {
        'screen/80': '80vh',
        'screen/85': '85vh',
      },
    }
  ```

### git 忽略 eslint 监测,配置自动化

- `git commit --no-verify -m "信息"`
- 配置`.eslintrc.js`
  ```javasript
      rules: {
        // XXX is defined but never used
        'no-unused-vars': 'off',
        // was used before it was defined
        '@typescript-eslint/no-use-before-define': 'off',
        '@typescript-eslint/no-shadow': 'off',
      }
  ```

### transform 缓慢放大,过渡

- ```css
  .pic {
   cursor: pointer;
   transition: all 0.6s;
   &:hover {
    transform: scale(1.2);
   }
  }
  ```

### 非组件调用全局 redux

- `getDvaApp()._store.dispatch()` `getDvaApp()._store.getState()`

### 配置数据持久化,三种共享数据的区别

1. initialState
2. redux 数据持久化
   - 安装依赖`redux-persist`
   - 在 src 下添加 models/globalModel.ts
   - 在 app.tsx 配置
   - 使用 `useSelector`,`useDispatch`,`getDvaApp()._store.dispatch()`,`getDvaApp()._store.getState()`
3. 简易 dva

### `symbol: 'image://' + imgRect`

### 自动添加 头部注释和 函数注释的插件 `koroFileHeader`

1. 头部注释 `Ctrl+Windows+I`
2. 函数注释 `Ctrl+Windows+T`
3. 趣味 `Ctrl+Windows+J`
4. .vscode/settings.json 配置
   ```json
   "fileheader.configObj": {
      "autoAdd": true, // 检测文件没有头部注释，自动添加文件头部注释
      "prohibitAutoAdd": ["json", "md"] ,// 禁止.json .md文件，自动添加头部注释
      "createHeader": true, // 新建文件自动添加注释
    },
   "fileheader.customMade": {
       "FilePath": "Do not edit", // 设置后，默认生成文件相对于项目的路径
       "Author": "sheng.zeng",
       "Date": "Do not edit", // 设置后默认设置文件生成时间
       "LastEditTime": "Do not edit", // 设置后，保存文件更改默认更新最后编辑时间
       "LastEditors": "sheng.zeng", // 设置后，保存文件更改默认更新最后编辑人
       "Description": ""
     }
   ```

### 翻译插件`Comment Translate`

- .vscode/settings.json 配置使用 bing 翻译源
  ```json
    "commentTranslate.source": "Bing"
  ```

### bat 文件命令式源码一键部署

- 自定义更新内容推送到钉钉消息
- 新建文件 deploy.bat
  ```shell
  npm run todeploy
  pause
  ```
- 使用源码的方式，使用 npm 包的方式参考 ems-pro
- ~~熟悉插件的作用~~

```
json
 "archiver": "^3.1.1",
 "dingtalk-robot-sender": "^1.2.0",
 "node-ssh": "^7.0.0",
 "ora": "^4.0.3",
```

### 部署信息推送到钉钉信息

- 推送到钉钉信息 [`npm install dingtalk-robot-sender`][2]
- 使用签名的安全方式
- ~~熟悉插件的作用~~

### [使用钉钉接收 gitlab 仓库的推送消息][1]

### 使用命令一键提交代码到 git 并部署

- git`post-receive`（push 完成之后触发）服务端钩子 ，客户端没有用
- `"shelljs": "^0.8.5",`
- `npm run topush "fix: 提交信息" todeploy`

### flex order 排序

- 越小越在前

### echarts 配置

     ``` javascript
            {
             symbol: 'rect',
             symbolSize: [4, 20],
             // 换颜色需要换图片，直接使用symbol: 'rect'
             // symbol: 'image://' + imgRect,
             // 默认为 false，只能用于绘制只有两个端点的线段,symbol生效；true 则可以多线段，实现转弯，但是symbol失效
             polyline: false,
            }
     ```

### 不加`valuePropName='checked'` 导致 Switch 不能赋值

```javascript
<Form.Item label="光伏使能" name="photovoltaicEnable" valuePropName="checked">
 <Switch />
</Form.Item>
```

### purgecss 导致计算出来的 class 在生产环境被去除

- css modules 可以加 module 也可以不加，**只是在这个 antdprov5 中**
- styles['compute-imgDesWrip'] 加上 `compute-***` 这样的 class，再添加 compute 到白名单

### umi UI

- `@umijs/preset-ui": "^2.2.9"`
- 关闭:`UMI_UI=none`
- 开启:`UMI_UI=1`

### 使用 import { useSelector } from 'umi';需要打开 dva: {},

### ~~~websocket 的数据 拿去优化 设备信息和事件信息和首页--->使用了 hooks~~~

- websocket 也需要代理
- 参考 setSocketData/useSetSocketData 文件

### 创建长度为 32 位的数组

- `const len = new Array(32);`

### slice:不改变原数组 ,splice:改变原数组

### 重新渲染会闪烁迟钝 首页 lines 路线图 , 侧边栏监测不到屏幕宽度变化

- 不使用 echarts-for-react（可以监测侧边栏变化后的屏幕宽度变化，但是重新渲染闪一下，迟钝）,
- 使用 `myChart1.setOption(option,true);`重新渲染平滑，但是监测不到侧边栏变化后的屏幕宽度变化
- react-resize-detector 插件：监听宽高变化

### 保留小数位

```javascript
// 输出结果为 2.45
var num = 2.446242342;
num = num.toFixed(2);
```

### svg 当做组件使用，而不是 img

- react-inlinesvg (转 svg 为代码和请求)

```javascript
import SVG from 'react-inlinesvg';
// 把 svg 代码 fill属性全部清空 为 fill="" 后可以使用fill属性设置颜色
import notWifiImg from '../assets/notWifi.svg';
<SVG
 className={`${styles['svg-hover']} cursor-pointer`}
 src={notWifiImg}
 width="1.6rem"
 height="1.6rem"
 fill="red"
/>;
```

```css
.svg-hover {
 // fill: #000;
 &:hover {
  fill: #ccc;
 }
}
```

### 表单文件上传的校验

### 为什么重新渲染

### "umi-plugin-keep-alive": "^0.0.1-beta.35"

- [缓存路由组件][3]
- 在 keepAliveLayouts 文件夹
- `layout: false` , 关闭默认的 antd 布局
- 全局包裹组件 wrappers 配置
- ### [antdpro 动态权限 normalRouteFilter][6]

```javascript
{
    canAdmin: currentUser && currentUser.access === 'admin',
    normalRouteFilter: (route) => {
      // console.log(route)
      return permissionsArr.includes(route.accessKey);
      // return true
    },
  };
```

```javascript
  {
    name: 'enventInfo',
    layout: Settings.antdLayout,  // 关闭默认的antd布局
    icon: 'table',
    accessKey: '事件信息',  // 自定义权限唯一值
    access: 'normalRouteFilter',  // 动态权限
    path: '/enventInfo',
    component: './enventInfo',
    // 全局包裹组件
    wrappers:[
      // '@/keepAliveLayouts/BaseLayout',
      '@/layouts/BaseLayout',
    ]
  },
```

### 环境变量

- 业务组件是 `NODE_ENV`
- config.ts 是 `REACT_APP_ENV`（在业务组件中读取不到，但是 undefined）

### 前端重新部署通知用户刷新网页

- `components/UpdateWeb/index.js`

### git 使用 ip 提交而不是域名

### a 标签下载总结

[a 标签下载附件，无法下载、无法重命名？怎么回事][4]

### [省市等数据][5]

- yarn add china-division

### 阻止多重事件，事件冒泡

```javascript
e.preventDefault();
e.stopPropagation();
```

### treeDataSimpleMode

- pid 数据 转 child 函数

### axios 的封装 params

- RevertAPIFormData
- RevertBothAPI ---? xxx/xxx/[id]
- RevertParamsAPI

## 待处理



---

[1]: https://www.codenong.com/cs109489923/ '使用钉钉接收gitlab仓库的推送消息'
[2]: https://github.com/x-cold/dingtalk-robot 'dingtalk-robot库'
[3]: https://blog.csdn.net/wzp6010625/article/details/125662911 'React + Ant Design Pro项目实现keep-alive页签'
[4]: https://blog.csdn.net/weixin_41387351/article/details/129832854 'a标签下载附件，无法下载、无法重命名？怎么回事'
[5]: https://blog.csdn.net/qq_42339350/article/details/115094171 'react 省市区地址级联 china-division、antd、Cascader'
[6]: https://pro.ant.design/zh-CN/docs/authority-management '动态权限normalRouteFilter'

```

```
