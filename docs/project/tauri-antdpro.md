---
title: tauri-antdpro
order: 2
toc: content
nav:
  title: 项目记录
  order: 6
group:
  title: 项目记录
  order: 3
---

---
## 项目路径
D:\w\oem_hhsl\web\bigScreeUI\project.md

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
2. `autofit.js` 并不是理想中的自适应，而是会缩小高度;
3. `import { FullScreenContainer } from '@jiaminghi/data-view-react'` 全屏组件 好在哪？

---

## 启动命令

- web 端 `npm run start` `npm run build`
- 桌面端 `yarn tauri dev` `yarn tauri build`
  - (可执行文件) \src-tauri\target\release\tauri-umi-antd.exe
  - (安装包) \src-tauri\target\release\bundle\msi\tauri-umi-antd_0.1.0_x64_en-US.msi

---

## 给 echarts 添加背景图 **适应性不好** ？？？？？？？？ 

- /user/bigData2 设备统计图

```json
     graphic: [
     // 背景图
        {
            type: 'image',
            id: 'logo',
            right: 'center',
            top: '12%',
            z: 0,
            style: {
                image: bg,
                width: 180,
                height:180
            }
        }
    ],
       series: [
        {
          type: 'pie',
          selectedMode: 'single',
          center:['50%', '30%'],
          // 重点这里 radius ， 要设置数值 ，不要百分比 ；图形和背景才会相对不动
          radius: [40, 65],
          color: ['#86D560', '#AF89D6', '#59ADF3', '#FF999A', '#FFCC67'],
          label: {
            show: false,
            formatter: (param: any) => {
              return param.name + ' (' + param.percent + '%)';
            },
            textStyle: {
              color: '#fff',
              fontSize: echartFontSize(1.5),
            },
          },
          labelLine: {
            show: true,
            length: 20,
            length2: 10,
          },
          data: serData,
        },
      ],
```
## echarts 玫瑰图比例太小显示优化
- https://blog.csdn.net/weixin_44101052/article/details/98964284


## 折现图永远铺满
只在数值轴中（type: 'value'）有效。
是否是脱离 0 值比例。设置成 true 后坐标刻度不会强制包含零刻度。在双数值轴的散点图中比较有用。
在设置 min 和 max 之后该配置项无效。
``` javascript
 yAxis: [
        {
          type: 'value',
          scale: true,
        },
      ],

```

## 区分 2560*1440 和 1920*1080 分辨率
``` css
@media screen and (min-width: 1920px) and (max-width: 2559px) and (orientation: landscape),
       screen and (min-height: 1080px) and (max-height: 1439px) and (orientation: portrait) {
    /* 在这里添加针对1920x1080分辨率的样式 */
    .box-wrip{
      padding: 1vh;
     }
}
 /* 这里注意些2300px */
@media screen and (min-width: 2300px) {
  /* 在这里添加针对2560x1440分辨率的样式 */
  .box-wrip{
    padding: 1.8vh;
   }
}
```

## 直接打包web端的build文件，添加开机动画
- 把web端的build文件直接丢进dist文件夹
- tauri.conf.json 去掉"beforeBuildCommand": "yarn build"
- 添加接口跨域处理:后台需要允许跨域；tauri.conf.json添加
``` json
"allowlist": {
      "all": true, 
      "http":{
        "all": true, 
        "request": true, 
        "scope":["http://**", "https://**"]
      }
    },

  
```
- 添加启动窗口页面
  ``` json 
   {
        "title": "3ren",
        "width": 800,
        "height": 600,
        "center": true,
        "url": "splashscreen.html",
        "label": "splashscreen",
        "visible": true
      }
  ```
  - 把public里面的splashscreen.html文件资源丢到dist文件夹
  
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
