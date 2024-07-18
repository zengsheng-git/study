<!--
 * @Author: sheng.zeng 1218128305@qq.com
 * @Date: 2024-01-22 17:59:43
 * @LastEditors: sheng.zeng 1218128305@qq.com
 * @LastEditTime: 2024-07-18 18:52:48
 * @FilePath: \almfirst-psa\frontend\psa-vite\README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
## 项目路径
D:\w\psa\almfirst-psa\frontend\psa-vite

# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## yarn create vite psa --template react 创建模板命令

## 命令：
- 安装依赖 `yarn install`
- 开发环境
  - 启动生产环境api `yarn start:pro`
  - 启动开发环境api(尹哥) `yarn start:dev`
- 生产环境打包
  - 打包使用生产环境api（不和Java一起跑） `yarn build:pro`
  - 打包使用开发环境api(和Java一起跑) `yarn build:dev`
- git 
https://dev.azure.com/dnetlab/Fintech/_git/almfirst-psa
zejun.zhang
udpu6is5m4xooo7r3nythnw4vbfyoprlnra37t7zvcb3ax6uxakq
## yarn create vite psa --template react 创建模板命令

## 使用 azure 的登录 
- window.crypto.randomUUID 仅在 HTTPS 上下文或 localhost 下可用。
- http会报错 window.crypto.randomUUID 仅在 HTTPS 上下文或 localhost 下可用。

## React18 严格模式 React.StrictMode
- 导致dispatch 有误 
- React18的useEffect会执行两次

        1. 这是 React18 才新增的特性。
        2. 仅在开发模式("development")下，且使用了严格模式("Strict Mode")下会触发。
        生产环境("production")模式下和原来一样，仅执行一次。
        3. 之所以执行两次，是为了模拟立即卸载组件和重新挂载组件。
        为了帮助开发者提前发现重复挂载造成的 Bug 的代码。 
        同时，也是为了以后 React的新功能做铺垫。 
        未来会给 React 增加一个特性，允许 React 在保留状态的同时，能够做到仅仅对UI部分的添加和删除。
        让开发者能够提前习惯和适应，做到组件的卸载和重新挂载之后， 重复执行 useEffect的时候不会影响应用正常运行。
## 命令格式化代码

## 添加 `tailwindcss` ,`postcss-pxtorem`

## `react-resize-detector` 监听某个div 的宽高
- 已使用在echarts div，Luckysheet div
- 因为侧边导航的收缩不会触发 `window.resize` 事件，所以需要监听div的宽高

## 多个reducer
## vite 打包正式环境 报错require is not defined
https://blog.csdn.net/zhongqw_00/article/details/134375704

## 执行 yarn install 抛出 unable to verify the first certificate 错误
https://www.hxstrive.com/article/897.htm


## select 选择相同的不会触发 onchange react
重新赋值下拉选择项(Products) ` dispatch({ type: "Products", newState: JSON.parse(JSON.stringify(Products)) });`
``` javascript

onChange={(e) => {
              console.log(e);
              dispatch({ type: "Products", newState: JSON.parse(JSON.stringify(Products)) });
            }}
```

## postCssPxToRem 会影响 @carbon/react 样式

## TreeView api太少 , 数据格式写死的


## 使用@carbon/react
- 引入组件`import { Button, Tabs, TabList, TabPanels, TabPanel, Tab } from '@carbon/react';`
- 在scss中引入
``` scss
@use '@carbon/react';
```
- 文档：https://react.carbondesignsystem.com/?path=/story/components-tabs--playground


## Luckysheet的使用

- [文档][Luckysheet文档]
- 在html中引入
``` html
    <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/luckysheet/dist/plugins/css/pluginsCss.css' />
    <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/luckysheet/dist/plugins/plugins.css' />
    <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/luckysheet/dist/css/luckysheet.css' />
    <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/luckysheet/dist/assets/iconfont/iconfont.css' />
    <script src="https://cdn.jsdelivr.net/npm/luckysheet/dist/plugins/js/plugin.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/luckysheet/dist/luckysheet.umd.js"></script>
```
- 使用
``` javascript
  useEffect(() => {
     const luckysheet = window.luckysheet;
     luckysheet.create({
       container: "luckysheet",
       plugins: ['chart'],
       title: 'filename', // 设定表格名称
       data: [], // 设定表格数据
    })
  }, [])
```


## [文件路径转children数组][文件路径转children数组]



## useNavigate 只能在 React Router v6 中使用，如果你的项目中使用的是 React Router v5 或更早的版本，你需要继续使用 useHistory

``` javascript
import { useNavigate } from 'react-router-dom';

function MyComponent() {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate('/new-route');
  };

  return (
    <div>
      <button onClick={handleClick}>Go to new route</button>
    </div>
  );
}

```

## ts项目中允许使用js
- 在tsconfig.json中配置`allowJs:true`


## 集成 univerjs
- 安装依赖
``` json
{
    "@univerjs/core": "^0.1.0-beta.4",
    "@univerjs/design": "^0.1.0-beta.4",
    "@univerjs/docs": "^0.1.0-beta.4",
    "@univerjs/docs-ui": "^0.1.0-beta.4",
    "@univerjs/engine-formula": "^0.1.0-beta.4",
    "@univerjs/engine-numfmt": "^0.1.0-beta.4",
    "@univerjs/engine-render": "^0.1.0-beta.4",
    "@univerjs/facade": "^0.1.0-beta.4",
    "@univerjs/network": "^0.1.0-beta.4",
    "@univerjs/rpc": "^0.1.0-beta.4",
    "@univerjs/sheets": "^0.1.0-beta.4",
    "@univerjs/sheets-formula": "^0.1.0-beta.4",
    "@univerjs/sheets-numfmt": "^0.1.0-beta.4",
    "@univerjs/sheets-ui": "^0.1.0-beta.4",
    "@univerjs/ui": "^0.1.0-beta.4",
    "@univerjs/uniscript": "^0.1.0-beta.4",
    "@wendellhu/redi": "^0.12.13",

    "monaco-editor": "^0.45.0",
    "rxjs": "^7.8.1",
}
```
- [参考项目][univerjs项目示例]




### 待处理
- ~~antd 去掉~~

----------------------
[文件路径转children数组]: https://www.cnblogs.com/liaozhenting/p/8343827.html
[Luckysheet文档]: https://mengshukeji.gitee.io/LuckysheetDocs/zh/guide/config.html#%E9%85%8D%E7%BD%AE%E9%A1%B9
[univerjs项目示例]: https://univer.ai/playground/?title=Uniscript
