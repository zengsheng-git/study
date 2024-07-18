<!--
 * @Author: sheng.zeng 1218128305@qq.com
 * @Date: 2024-02-21 16:31:15
 * @LastEditors: sheng.zeng 1218128305@qq.com
 * @LastEditTime: 2024-07-18 18:52:24
 * @FilePath: \LMM-Frontend\project.md
-->
## 项目路径
D:\w\lmm\lmm-onliy-new\LMM-Frontend
## file 上传相同文件没反应， onchnage 不触发，解决办法

```html
<input class="file-ipt" type="file" multiple @change="changeFile" />
```

```js
const changeFile = (e) => {
    let inputDom = e.target;
    let files = inputDom.files;

    console.log(files);
    e.preventDefault();
    handleFileName(files);

    // 给 inputDom 重新设置值，这样 inputDom 里的 files 就为空了，
    // 再选择同一个文件的时候就会触发 onchange 事件了
    inputDom.value = "";
};
```

## 监听路由变化

```js
import { useRouter } from "vue-router";
const router = useRouter();
watch(
    () => router.currentRoute.value.path,
    (toPath) => {
        //要执行的方法
        const query = router.currentRoute.value.query;
    },
    { immediate: true, deep: true },
);
```

## 合并分支

-   git pull
-   git merge origin/dev
-   git add .
-   git commit -m "xxx"
-   git push

## change事件与input事件的区别在于

-   change事件在输入框失去焦点后才会触发
-   而input事件在用户输入时即可触发。

## 手写Vue3中的表单验证

-   https://blog.csdn.net/aahwj/article/details/135257788#:~:text=%E5%9C%A8Vue3%E4%B8%AD%EF%BC%8C,%E8%A1%A8%E5%8D%95%E9%AA%8C%E8%AF%81%20%E5%8F%AF%E4%BB%A5%E4%BD%BF%E7%94%A8Vue%E7%9A%84%E5%86%85%E7%BD%AE%E6%8C%87%E4%BB%A4v-model%E5%92%8C%E8%87%AA%E5%AE%9A%E4%B9%89%E6%8C%87%E4%BB%A4%E6%9D%A5%E5%AE%9E%E7%8E%B0%E3%80%82

## 路由重定向

```js
        {
            path: "/",
            name: "home",
            redirect:'/lmm/forecast-setup/institutions'
        }

```

## 监听一下路由的变动

```js
onBeforeRouteUpdate(async (to, from) => {
    if (to.params.institutionId !== from.params.institutionId) {
    }
});
```

## 文件流下载需要token

-   https://zhuanlan.zhihu.com/p/350069246
-   responseType: 'blob' 在导出的接口加上声明接收参数 最后一个参数就是指定类型为 blob 或者 arraybuffer

## 【axios 使用】下载文件流 以及 获取响应头header content-disposition 中的文件名

-   [参考链接][参考链接2]
-   [参考链接][参考链接3]

## vue3 文件上传支持点击/粘贴/拖拽

-   https://blog.csdn.net/Jie0817/article/details/133312171

## axios timeout: 50000,

-   设置了在5000毫秒内请求数据 如果没有请求成功就执行错误函数

## 项目需求，鼠标悬浮在div上时出现弹框信息，on关联mouseover事件时，出现悬浮框一直不停闪烁，是因为频繁触发了mouseover和mouseout事件，

-   [参考链接][参考链接1]

## setup 语法，模版语法

-   父传值给子
-   子调用父函数
-   阻止事件冒泡

```js
e.preventDefault();
e.stopPropagation();
```

-   计算属性
-   路由跳转
-   插槽类似react的 props.children
-   [在路由文件中使用 pinia] [在路由文件中使用 pinia]

-   `!z-0`

```css
z-index: 0 !important;
```

## 指定容器div滚动到指定位置 (overflow-y-auto h-[540px])

```html
<div ref="scrollDiv" class="flex  flex-col items-center gap-5 overflow-y-auto h-[540px]"></div
```

```js
const scrollDiv = ref(null);

const scrollToBottom = () => {
    setTimeout(() => {
        let scrollElem = scrollDiv.value;
        scrollElem.scrollTop = scrollElem.scrollHeight;
    }, 100);
};
```

## 待办事项

-   文件上传请求的统一
-   3个ID 的统一，和记录

---

[在路由文件中使用 pinia]: https://blog.csdn.net/zlting_/article/details/127495583
[参考链接1]: https://blog.csdn.net/qq_42627162/article/details/111941690#:~:text=%E9%A1%B9%E7%9B%AE%E9%9C%80%E6%B1%82%EF%BC%8C%E9%BC%A0%E6%A0%87%E6%82%AC%E6%B5%AE%E5%9C%A8div%E4%B8%8A%E6%97%B6%E5%87%BA%E7%8E%B0%E5%BC%B9%E6%A1%86%E4%BF%A1%E6%81%AF%EF%BC%8Con%E5%85%B3%E8%81%94mouseover%E4%BA%8B%E4%BB%B6%E6%97%B6%EF%BC%8C%E5%87%BA%E7%8E%B0%E6%82%AC%E6%B5%AE%E6%A1%86%E4%B8%80%E7%9B%B4%E4%B8%8D%E5%81%9C%E9%97%AA%E7%83%81%EF%BC%8C%E6%98%AF%E5%9B%A0%E4%B8%BA%E9%A2%91%E7%B9%81%E8%A7%A6%E5%8F%91%E4%BA%86mouseover%E5%92%8Cmouseout%E4%BA%8B%E4%BB%B6%EF%BC%8C%E8%A7%A3%E5%86%B3%E5%8A%9E%E6%B3%95%EF%BC%9A%E5%9C%A8%E6%82%AC%E6%B5%AE%E6%A1%86%E5%85%83%E7%B4%A0%E4%B8%AD%E5%8A%A0%E5%85%A5css%E6%A0%B7%E5%BC%8F%EF%BC%9Apointer-events%3A,none%3B%E8%AF%A5%E6%A0%B7%E5%BC%8F%E9%98%BB%E6%AD%A2%E6%82%AC%E6%B5%AE%E5%B1%82%E6%88%90%E4%B8%BA%E9%BC%A0%E6%A0%87%E4%BA%8B%E4%BB%B6%E7%9A%84target%EF%BC%8C%E7%A9%BF%E9%80%8F%E6%82%AC%E6%B5%AE%E7%AA%97%E6%9D%A5%E6%8C%87%E5%AE%9A%E5%8E%9F%E5%A7%8B%E7%BB%91%E5%AE%9Amouseout%E5%92%8Cmouseover%E7%9A%84div%E3%80%82
[参考链接2]: https://blog.csdn.net/m0_53584457/article/details/130527033
[参考链接3]: https://blog.csdn.net/GYB4979/article/details/127424021
