# vue2 和 vue3 区别

## 1、生命周期函数

| VUE2            |          | VUE3              |
| --------------- | -------- | ----------------- |
| beforeCreate()  | 创建之前 | setup()           |
| created()       | 创建完成 | setup()           |
| beforeMount()   | 挂载之前 | onBeforeMount()   |
| mounted()       | 挂载完成 | onMounted()       |
| beforeUpdate()  | 修改之前 | onBeforeUpdate()  |
| updated()       | 修改完成 | onUpdated()       |
| beforeDestroy() | 销毁之前 | onBeforeUnmount() |
| destroyed()     | 销毁完成 | onUnmounted()     |
| errorCaptured() | 错误捕获 | onErrorCaptured() |

## 2、v-if 与 v-for 的优先级

-   2.x 版本中 v-for > v-if
-   3.x 版本中 v-if > v-for

## 3、v-for 中的 Ref 数组

-   vue2.x 会自动把ref填充内容
-   vue3.x 需要手动添加

```vue
<ul>
    <li v-for='item in 5' :key='item' :ref="setItemRef">
    	{{ item }}
    </li>
</ul>
```

```vue
methods:{ setItemRef(el){ this.arr.push( el ); } }
```

## 4、$children

-   vue2.x : 访问当前实例的子组件

-   vue3.x : 在 3.x 中，$children 已被移除，且不再支持

    ```vue
    <child ref="hw" />

    this.$refs.hw
    ```

## 5、setup

### 5.1、 是什么

​ 组合式 API

### 5.2、 来解决什么问题

​ 使用 (data、computed、methods、watch) 组件选项来组织逻辑通常都很有效。然而，当我们的组件开始变得更大时，逻辑关注点的列表也会增长。尤其对于那些一开始没有编写这些组件的人来说，这会导致组件难以阅读和理解。

### 5.3、 响应区别

-   vue2.x : Object.defineProperty()
    -   Object.defineProperty 存在的问题
        -   不能监听数组的变化
        -   必须遍历对象的每一个属性
-   vue3.x : Proxy
    -   Proxy 不需要遍历

### 5.4、 使用渲染函数

-   ref : 定义数据 简单类型

-   reactive : 定义数据 复杂类型

### 5.5 、setup语法糖插件

​ 解决场景 ： 在组件中开发无需每次都引入 import { ref, ...} from ...

1. 下载安装

    ```
    npm i unplugin-auto-import -d
    ```

2. 配置：vite.config.js

    ```js
    import { defineConfig } from "vite";
    import vue from "@vitejs/plugin-vue";
    import AutoImport from "unplugin-auto-import/vite";

    import { resolve } from "path"; // 使用ES模块导入path模块

    export default defineConfig({
        plugins: [
            vue(),
            //配置插件
            AutoImport({ imports: ["vue", "vue-router"] }),
        ],
        resolve: {
            // 配置路径别名
            alias: { "@": resolve(__dirname, "./src") },
        },
    });
    ```

### 5.6、 toRefs

​ toRefs：完成数据的解构

### 5.7 、computed

```js
obj = reactive({
    name: "张三",
    age: 18,
    str: computed(() => {
        return obj.name.slice(1, 2);
    }),
});

let msgChange = computed(() => {
    return msg.value.slice(1, 3);
});

let msgChange = computed({
    get() {
        return msg.value.slice(1, 3);
    },
    set() {
        console.log("设置了");
    },
});
```

### 5.8、 watch

-   vue2.x :

    ```vue
    watch:{ obj:{ handler(newVal , oldVal){ console.log( newVal , oldVal ) }, immediate:true, deep:true } }
    ```

-   vue3.x :

    ```js
    #监听数据「初始化监听」
    watch( msg, (newVal, oldVal)=>{
        	console.log(  newVal,oldVal )
        },{
        immediate:true
    })

    #监听多个数据「一起监听」
    watch([msg,str],(newVal,oldVal)=>{
        	console.log( newVal,oldVal )
        },{
        immediate:true
    })

    #监听“对象”中某个对象
    watch( ()=>obj.arr , (newVal,oldVal)=>{
    	console.log( newVal,oldVal )
    })

    #立即执行监听函数
    watchEffect(()=>{
    	console.log( msg.value )
    })
    ```

参考链接：https://v3.cn.vuejs.org/api/computed-watch-api.html#watcheffect

### 5.9、 组件\_父传子

1. 父

    ```vue
    <child :msg="msg"></child>

    import child from './child.vue' let msg = ref('这是父传过去的数据');
    ```

2. 子

    ```vue
    <div>{{ msg }}</div>

    <script setup>
    defineProps({
        msg: {
            type: String,
            default: "1111",
        },
    });
    </script>
    ```

### 5.10 、组件\_子传父

-   子

    ```vue
    <div> 
        {{ num }}
        <button @click='changeNum'>按钮</button>
    </div>

    <script setup lang="ts">
    let num = ref(200);
    const emit = defineEmits<{
        (e: "fn", id: number): void;
    }>();

    const changeNum = () => {
        emit("fn", num);
    };
    </script>
    ```

-   父

    ```vue
    <div>
    	<List @fn='changeHome'></List>
    </div>

    <script setup>
    import List from "../components/List.vue";
    const changeHome = (n) => {
        console.log(n.value);
    };
    </script>
    ```

### 5.11、 v-model传值

-   父

    ```vue
    <List v-model:num="num"></List>

    <script setup>
    import List from "../components/List.vue";
    let num = ref(1);
    </script>
    ```

-   子

    ```js
    const props = defineProps({
        num: {
            type: Number,
            default: 100,
        },
    });
    const emit = defineEmits(["update:num"]);

    const btn = () => {
        emit("update:num", 200);
    };
    ```

### 5.12 、兄弟组件传值

-   下载安装

    ```
    npm install mitt -S
    ```

-   plugins/Bus.js

    ```
    import mitt from 'mitt'
    const emitter = mitt()
    export default emitter
    ```

-   A组件

    ```
    emitter.emit('fn',str)
    ```

-   B组件

    ```
    emitter.on('fn',e=>{
    	s.value = e.value
    })
    ```

## 6、生命周期

-   选项式 API

​ beforeCreate ...

-   setup 组合式API

​ 注意：没有beforeCreate和created

​ 其他生命周期要使用前面加"on" 例如：onMounted

参考链接：https://v3.cn.vuejs.org/guide/composition-api-lifecycle-hooks.html

## 7、路由

​ useRoute ==> this.$route

​ useRouter ==> this.$router

## 8、插槽

### 8.1、匿名插槽

-   父

    ```
    <A>传递的数据</A>
    ```

-   子

    ```vue
    <header>
        <div>头部</div>
        <slot></slot>
    </header>

    <footer>
        <div>底部</div>
        <slot></slot>
    </footer>
    ```

### 8.2、具名插槽

-   父

    ```vue
    <Son>
        <template v-slot:xxx>数据</template>
    
        <template v-slot:yyy>数据</template>
    </Son>

    简写：
    <template #xxx></template>
    ```

-   子

    ```vue
    <header>
        <slot name='xxx'></slot>
        <slot name='yyy'></slot>
    </header>

    <footer>
        <slot name='xxx'></slot>
    </footer>
    ```

### 8.3、作用域插槽

-   父

    ```vue
    <template v-slot="{ data }">{{ data.name }} --> {{ data.age }}</template>

    简写：
    <template #default="{ data }"></template>
    ```

-   子

    ```vue
    <div v-for="item in list" :key="item.id">
    	<slot :data='item'></slot>
    </div>
    ```

### 8.4、动态插槽

​ 通过数据进行切换

-   父

    ```vue
    <template #[xxx]>数据</template>

    <script setup>
    let xxx = ref("xxx");
    </script>
    ```

## 9、传送 Teleport

```vue
<teleport to="#container"></teleport>
<teleport to=".main"></teleport>
<teleport to="body"></teleport>

***必须传送到有这个dom的内容【顺序】
```

## 10、动态组件

```vue
<component :is="动态去切换组件"></component>
```

## 11、异步组件

**提升性能**

vueuse ： https://vueuse.org/core/useintersectionobserver/

### 11.1、使用场景1

组件按需引入：当用户访问到了组件再去加载该组件

```vue
<template>
    <div ref="target">
        <C v-if="targetIsVisible"></C>
    </div>
</template>

<script setup>
import { useIntersectionObserver } from "@vueuse/core";

const C = defineAsyncComponent(() => import("../components/C.vue"));

const target = ref(null);
const targetIsVisible = ref(false);

const { stop } = useIntersectionObserver(target, ([{ isIntersecting }]) => {
    if (isIntersecting) {
        targetIsVisible.value = isIntersecting;
    }
});
</script>
```

### 11.2、使用场景2

```vue
<Suspense>
    <template #default>
        <A></A>
    </template>
    <template #fallback>
        加载中...
    </template>
</Suspense>

<script setup>
const A = defineAsyncComponent(() => import("../components/A.vue"));
</script>
```

### 11.3、打包分包处理

```
npm run build打包完成后，异步组件有单独的js文件，是从主体js分包出来的

A.c7d21c1a.js
C.91709cb2.js
```

## 12、混入 Mixin

来分发 Vue 组件中的可复用功能

### 12.1、setup写法

```js
@/mixins/mixin.js

import { ref } from 'vue'
export default function(){

    let num = ref(1);
    let fav = ref(false);

    let favBtn = ()=>{
        num.value += 1;
        fav.value = true;
        setTimeout(()=>{
            fav.value = false;
        },2000)
    }

    return {
        num,
        fav,
        favBtn
    }

}
```

```vue
@/组件.vue

<template>
    <div>
        <h1>A组件</h1>
        {{ num }}
        <button @click="favBtn">
            {{ fav ? "收藏中..." : "收藏" }}
        </button>
    </div>
</template>

<script setup>
import mixin from "../mixins/mixin.js";
let { num, fav, favBtn } = mixin();
</script>
```

### 12.2、选项式api写法

```js
mixin.js;

export const fav = {
    data() {
        return {
            num: 10,
        };
    },
    methods: {
        favBtn(params) {
            this.num += params;
        },
    },
};
```

```vue
组件.vue

<template>
    <div>
        <h1>A组件</h1>
        {{ num }}
        <button @click="favBtn(1)">按钮</button>
    </div>
</template>

<script type="text/javascript">
import { fav } from "../mixins/mixin.js";
export default {
    data() {
        return {
            str: "你好",
        };
    },
    mixins: [fav],
};
</script>
```

## 13、依赖注入Provide / Inject

提供：

```vue
<script setup>
provide("changeNum", num);
</script>
```

注入：

```vue
<template>
    <div>
        <h1>B组件</h1>
        {{ bNum }}
    </div>
</template>

<script setup>
const bNum = inject("changeNum");
</script>
```

## 14、Vuex

-   state

    -   let num = computed( ()=> store.state.num );

-   getters

    -   let total = computed( ()=> store.getters.total );

-   mutations

    -   store.commit('xxx')

-   actions

    -   store.dispatch( 'xxx' )

-   modules:

    -   和之前的版本使用一样

-   Vuex持久化存储【插件】

    ```js
    npm i vuex-persistedstate -S

    import persistedState from 'vuex-persistedstate'

    export default createStore({
        modules: {
          	user
        },
        plugins:[persistedState({
          	key:'xiaoluxian',
          	paths:['user']
        })]
    })
    ```

## 15、Pinia

-   Vuex和pinia的区别

    -   参考网址： https://github.com/vuejs/rfcs/pull/271

        ```
        pinia没有mutations，只有：state、getters、actions

        pinia分模块不需要modules（之前vuex分模块需要modules）

        pinia体积更小（性能更好）

        pinia可以直接修改state数据
        ```

-   pinia使用

    -   官方网址：https://pinia.vuejs.org/
    -   具体使用：https://xuexiluxian.cn/blog/detail/242b0ed71feb412991f04d448fc86636

-   pinia持久化存储

    -   参考链接：https://xuexiluxian.cn/blog/detail/acebacd99612447e8c80dcf6354240f6

-   设置代理解决跨域问题

    -   参考文章：https://xuexiluxian.cn/blog/detail/01f62baa85b7431992586b4689a9b07a
    -   API参考链接：https://staging-cn.vuejs.org/api/#onmounted

Vue2-3 学习视频：https://www.bilibili.com/video/BV1Zy4y1K7SH
Vue3 学习视频：https://www.bilibili.com/video/BV1Za4y1r7KE
