---
title: psa
order: 8
toc: content
nav:
  title: 项目记录
  order: 7
group: 
  title: 项目记录
  order: 3
---


## 项目路径
D:\w\psa\almfirst-psa-frontend

## 本地开发接口报错Invalid CORS request 403

-   [参考文档][Invalid CORS request 403]
-   使用 `configure` 或者 `headers`

```js
// 代理请求
proxy: {
        "/psa/api": {
         target: env.VITE_API_URL, //目标url
         changeOrigin: true, //支持跨域
         // rewrite: (path) => path.replace(/^\/api/, ""),
          configure: (proxy, options) => {
        proxy.on("proxyReq", function (proxyReq, req, res) {
                            proxyReq.removeHeader("referer"); //移除请求头---最主要是设置这个
                            proxyReq.removeHeader("origin"); //移除请求头---最主要是设置这个
                            //proxyReq.setHeader('host','api.bilibili.com/') //添加请求头
                        });
                    },
                    // headers: {
                    //   host: 'almfirst-psa.greentree-33a1fcd5.centralus.azurecontainerapps.io/', // 和转发url一样 host不带协议头 origin带上
                    //   origin: 'https://almfirst-psa.greentree-33a1fcd5.centralus.azurecontainerapps.io/'
                    // },
                },
            },

```

## a标签禁用

-   a标签没有**disabled** 属性
-   a标签禁止事件**pointer-events: none**去掉鼠标事件，会与去掉 `cursor: not-allowed;` _红色禁用符号_ 样式
-   同时使用 `cursor: not-allowed;` 样式 并且禁用鼠标事件

```vue
<div
    v-for="(item, index) in navList"
    :class="{
        'cursor-not-allowed': item.disabled,
    }"
>
     <RouterLink  :class="{ 
                        'text-white': route.path === item.path , 
                        'pointer-events-none' : item.disabled,
                 }" 
                        :to="item.path" 
                        :key="index"
                         @click="navBtn(item)">
        {{ item.name }}
    </RouterLink>
</div>
```

---

[Invalid CORS request 403]: https://blog.csdn.net/qq_34718221/article/details/135910807
