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
  ``` json
    "commentTranslate.source": "Bing"
  ```

## 待处理

- ~~首页图片和文字封装~~
- ~~Commitizen git 提交辅助~~
- ~~Tailwind css 设置 rem~~
- ~~svg 的基础理解动画线条~~
- ~~改成微前端架构~~
- ~~使用 antdesign V5~~
