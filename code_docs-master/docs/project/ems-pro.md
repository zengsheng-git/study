---
title: ems-pro
order: 3
toc: content
nav:
  title: 项目记录
  order: 6
group:
  title: 项目记录
  order: 3
---

# 项目

## 项目路径
D:\w\ems-web\ems-web\ems-pro\project.md

- 在 umi3 中使用 sass  
   `Javascript "@umijs/plugin-sass": "^1.1.1", "sass": "^1.63.6", "sass-loader": "^10.4.1", `  
  `sass: { implementation: require('sass') },`

- 设置布局按钮的出来 是由于引入的错误 ,应该使用  
  `"@ant-design/pro-layout": "^6.32.0"`,

- 启动命令  
  `yarn start`

- 打包构建  
  `yarn build`

- 添加前端错误等监控,火狐 pv 有兼容性
- ~~复制的时候也会复制引入 vscode~~
- Store.get('equipmentId') 使用 redux
- 根据项目不同，保存文件自动格式化

  - vscode 根目录下建立文件`.vscode/settings.json`

- 配置 PostCSS 插件;报错`PostCSS plugin tailwindcss requires PostCSS 8` 解决:使用 `"postcss": "^7",`

  - tailwindcss 配置 (umi3 中)

    安装依赖

    ```Javascript
      "postcss": "^7",
      "tailwindcss": "npm:@tailwindcss/postcss7-compat",
      "@tailwindcss/postcss7-compat": "^2.2.17",
    ```

    根目录下新建`tailwind.config.js`

    ```Javascript
        module.exports = {
          corePlugins: {
            preflight: false
          },
          theme: {
            extend: {
              colors: {
                'custom-blue': '#00899B',
                'custom-green': '#67C67C',
                'custom-red': '#FF6347'
              }
            }
          },
          variants: {
            extend: {}
          },
          plugins: []
        };
    ```

    根目录下新建 tailwind.css,并在 globe.less 中引用: `@import '../tailwind.css';`

    ```Javascript
        @tailwind base;
        @tailwind components;
        @tailwind utilities;
        .my-element {
            @apply text-white;
        }
    ```

  - purgecss 配置 (umi3 中)

    ```Javascript
    "postcss": "^7",
    "@fullhuman/postcss-purgecss": "3.0.0",
    ```

  - autoprefixer 配置 (umi3 中)

    ```Javascript
    "postcss": "^7",
    "autoprefixer": "^9",
    ```

  - `config.ts`统一配置如下
    ```Javascript
        extraPostCSSPlugins: [
          require('tailwindcss'),
          require('autoprefixer'),
          purgecss({
            content: ['./src/pages/**/*.{js,jsx,ts,tsx}', './src/components/**/*.{js,jsx,ts,tsx}'],
            // 选择器 .html ，#html, html标签 ， 将保留在最终的 CSS 中。
            safelist: {
              standard: ['html', 'body', 'root'],
              // 如果选择器的任何部分能够匹配 safelist.greedy 参数所设置的正则表达式，则整个选择器将被保留。
              greedy: [/ant.*/, /dv.*/],
            },
            defaultExtractor: (content: any) => content.match(/[\w-/:]+(?<!:)/g) || [],
          }),
        ],
    ```

- PostCSS 7 兼容性版本

  从 v2.0 版本开始，Tailwind CSS 依赖于 PostCSS 8。由于 PostCSS 8 才使用了几个月，因此生态系统中的许多其他工具尚未更新，这意味着在安装 Tailwind，并尝试编译 CSS 时，您可能会在终端中看到这样的错误：

  Error: PostCSS plugin tailwindcss requires PostCSS 8. 为了弥合这个问题，直到每个人都进行了更新，我们还在 npm 的 compat 频道下发布了 PostCSS 7 兼容性版本。

  如果遇到上述错误，请卸载 Tailwind 并使用兼容性版本重新安装：

  `npm uninstall tailwindcss postcss autoprefixer` `npm install tailwindcss@npm:@tailwindcss/postcss7-compat @tailwindcss/postcss7-compat postcss@^7 autoprefixer@^9` 兼容性版本在任何方面都与主版本相同，因此您不会错过任何功能或类似功能。

  一旦您的其余工具添加了对 PostCSS 8 的支持，就可以通过使用 latest 标签重新安装 Tailwind 及其相关依赖项来取代兼容性构建：

  `npm uninstall tailwindcss @tailwindcss/postcss7-compat` `npm install tailwindcss@latest postcss@latest autoprefixer@latest`

- 保存文件自动格式化

  ```Javascript
  // 保存格式化
  "editor.formatOnSave": true
  ```

- npm view [npm 包名称] version
- pro 高级组件的配置要记住，备注一下 `@ant-design/pro` 来源依赖
- ProTable 和 Table 一样的属性
- 使用 umi request
- 阻止事件冒泡  
  `event.stopPropagation();`
  ```Javascript
   <li
       onClick={() => {
          history.push('/selectSystems')
      }}
      >
      <span onClick={(event) => {
              event.stopPropagation();
              fetchInfo(item.imei);
              }}>
          详情
       </span>
  </li>
  ```
- width 计算属性 width: calc(100% + 44px);
- 查看宝塔命令行提示
  - `bt`
- 查看宝塔面板信息（宝塔地址和登录用户名）
  - `/etc/init.d/bt default`
- 二级目录打开新页面
  - `window.open(location.origin + location.pathname + '#/realtimeMemonitor?parameter=' + val + '&equipmentId=' + RecIdVal);`
- echarts 使用本地图片 `symbol: 'image://' + imgGF`
- let now = new Date(); // console.log(now.toLocaleString('zh-CN')); // 输出类似于 '2023/6/21 18:30:00' 的格式
