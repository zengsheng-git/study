---
title: tauri-antdpro
order: 2
toc: content
nav:
  title: 项目记录
  order: 6
group:
  title: 项目记录
  order: 1
---

---

## 数据处理

- 数据的备份便于调试,
- 数据处理 ：竖型堆叠柱形图，横向堆叠柱形图(/user/bigData4);

```javascript
// 原始数据
[
  {
    name: '教务系统DB服务器',
    data: [
      { disk: '磁盘:/', percent: '0' },
      { disk: '磁盘:/home', percent: '0' },
    ],
  },
  {
    name: '192.168.202.129(教务系统报表服务器)',
    data: [
      { disk: '磁盘:/run', percent: '0' },
      { disk: '磁盘:/run/user/0', percent: '0' },
      { disk: '磁盘:/sys/fs/cgroup', percent: '0' },
      { disk: '磁盘:/boot', percent: '0' },
      { disk: '磁盘:/run/user/42', percent: '0' },
      { disk: '磁盘:/dev/shm', percent: '0' },
      { disk: '磁盘:/', percent: '0' },
    ],
  },
];
```

- 数据处理横向柱形图(/user/bigData5);

```javascript
// 原始数据
[
  { group_name: 'UPS', group_good_percent: 0, group_warn_percent: 0, group_error_percent: 100 },
  { group_name: '温湿度', group_good_percent: 0, group_warn_percent: 0, group_error_percent: 100 },
  {
    group_name: '采集主机',
    group_good_percent: 0,
    group_warn_percent: 0,
    group_error_percent: 100,
  },
  {
    group_name: '精密空调',
    group_good_percent: 0,
    group_warn_percent: 0,
    group_error_percent: 100,
  },
  {
    group_name: '市电配电柜',
    group_good_percent: 0,
    group_warn_percent: 0,
    group_error_percent: 100,
  },
];
```

- 表格数据渲染为 antd 表格和 data-view-react 滚动

---

## 新功能

- `@jiaminghi/data-view-react`;
  > declare module '@jiaminghi/data-view-react';
- 修改 antd5 的默认样式; less, scss 伪类和 hover 的写法;
- echartFontSize 的实现;rem 的引入 `import '@/util/flexible'`;
- 自定义原子 css

  > `import "@/globalStyles/expand.scss";`  
  >  `import "@/globalStyles/generate.scss";`

- PurgeCSS 插件使用

  > `content: ['./src/components/**/*.tsx', './src/pages/**/*.tsx']`, 中的文件和所有的 css 作比较；

  > `"@fullhuman/postcss-purgecss": "^5.0.0",`  
  > `"postcss": "^8.4.25",`

- 用户自定义主题，修改 css 中的属性值
  - localStorage 实现
  - `redux-persist` 数据持久化实现
- 函数的返回值是一个对象 `()=>({})`
- 滚动条样式，文本溢出
- 对象结构时候声明类型
  - `const { name, age }: { name: string; age: number } = body.value`

---

## 自适应

1. % + vh / vw 适配;
2. ~~`autofit.js` 并不是理想中的自适应，而是会缩小高度,但是 echarts 文字不需要再单独设置;~~
3. ~~`import { FullScreenContainer } from '@jiaminghi/data-view-react'` 全屏组件 好在哪？~~
4. **尝试使用 `autofit.js`**

---

## 启动命令

- web 端 `npm run start` `npm run build`
- 桌面端 `yarn tauri dev` `yarn tauri build`
  - (可执行文件) \src-tauri\target\release\tauri-umi-antd.exe
  - (安装包) \src-tauri\target\release\bundle\msi\tauri-umi-antd_0.1.0_x64_en-US.msi

---

## **待处理**

- **eslint**
- **接口文件的集合**
- **gitlint 的用法**
- 添加原子 css 库 tailwindcss, 对 data-view-react 样式有影响;
- bigData6 用到自定义原子 css
- run start 和 run start：dev 的区别 ????
- 色调的选择，
- 自动配色合适的
- ts 的类型补全
- ~~数据请求封装数据备份~~
- 全部图形确定了就一键换主题
- echarts 配置记录
  - echartFontSize 文字大小动态计算函数
  - bar 的最小高度
  - 没有设置 color 文件模糊
  - 是否是反向坐标轴。 可作为正序和倒序
  - axisLabel 旋转换行
- 使用 ahooks 中的 useInterval
- 开发这个应该使用 tauri 命令，方便熟悉
- tauri 的配置记录
  ```JavaScript
    "build": {
      "beforeBuildCommand": "yarn run build",
      "beforeDevCommand": "yarn run start",
      "devPath": "http://localhost:5000",
      "distDir": "../dist",
      "withGlobalTauri": true
    },
  ```

---
