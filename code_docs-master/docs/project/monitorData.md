## jsError

```json
{
  "title": "前端监控系统", // 页面标题
  "url": "http://localhost:8080/", // 页面URL
  "timestamp": "1590815288710", // 访问时间戳
  "userAgent": "Chrome", // 用户浏览器类型
  "kind": "stability", // 大类
  "type": "error", // 小类
  "errorType": "jsError", // 错误类型
  "message": "Uncaught TypeError: Cannot set property 'error' of undefined", // 类型详情
  "filename": "http://localhost:8080/", // 访问的文件名
  "position": "0:0", // 行列信息
  "stack": "btnClick (http://localhost:8080/:20:39)^HTMLInputElement.onclick (http://localhost:8080/:14:72)", // 堆栈信息
  "selector": "HTML BODY #container .content INPUT" // 选择器
}
```

## promiseError

```json
{
    ...
    "errorType": "promiseError",//错误类型
    "message": "someVar is not defined",//类型详情
    "stack": "http://localhost:8080/:24:29^new Promise (<anonymous>)^btnPromiseClick (http://localhost:8080/:23:13)^HTMLInputElement.onclick (http://localhost:8080/:15:86)",//堆栈信息
    "selector": "HTML BODY #container .content INPUT"//选择器
}
```

## resourceError

```json
    ...
    "errorType": "resourceError",//错误类型
    "filename": "http://localhost:8080/error.js",//访问的文件名
    "tagName": "SCRIPT",//标签名
    "timeStamp": "76",//时间
```

## xhr

```json
{
  "title": "前端监控系统", //标题
  "url": "http://localhost:8080/", //url
  "timestamp": "1590817024490", //timestamp
  "userAgent": "Chrome", //浏览器版本
  "kind": "stability", //大类
  "type": "xhr", //小类
  "eventType": "load", //事件类型
  "pathname": "/success", //路径
  "status": "200-OK", //状态码
  "duration": "7", //持续时间
  "response": "{\"id\":1}", //响应内容
  "params": "" //参数
}
```

## 白屏blank

```js
{
  "title": "前端监控系统",
  "url": "http://localhost:8080/",
  "timestamp": "1590822618759",
  "userAgent": "chrome",
  "kind": "stability", //大类
  "type": "blank", //小类
  "emptyPoints": "0", //空白点
  "screen": "2049x1152", //分辨率
  "viewPoint": "2048x994", //视口
  "selector": "HTML BODY #container" //选择器
}
```

## 加载时间timing

```json
{
  "title": "前端监控系统",
  "url": "http://localhost:8080/",
  "timestamp": "1590828364183",
  "userAgent": "chrome",
  "kind": "experience",
  "type": "timing",
  "connectTime": "0", //TCP连接耗时
  "ttfbTime": "1",  //ttfb
  "responseTime": "1", //Response响应耗时
  "parseDOMTime": "80",  //DOM解析渲染耗时
  "domContentLoadedTime": "0", //DOMContentLoaded事件回调耗时
  "timeToInteractive": "88", //首次可交互时间
  "loadTime": "89" //完整的加载时间
}
```

## 首屏paint

```json
{
  "title": "前端监控系统",
  "url": "http://localhost:8080/",
  "timestamp": "1590828364186",
  "userAgent": "chrome",
  "kind": "experience",
  "type": "paint",
  "firstPaint": "102",
  "firstContentPaint": "2130",
  "firstMeaningfulPaint": "2130",
  "largestContentfulPaint": "2130"
}
```

## 第一次交互 firstInputDelay

```json
{
  "title": "前端监控系统",
  "url": "http://localhost:8080/",
  "timestamp": "1590828477284",
  "userAgent": "chrome",
  "kind": "experience",
  "type": "firstInputDelay",  //首次输入延迟
  "inputDelay": "3", // 延迟的时间
  "duration": "8",
  "startTime": "4812.344999983907", // 开始处理的时间
  "selector": "HTML BODY #container .content H1"
}
```

## 卡顿 longTask

```json
{
  "title": "前端监控系统",
  "url": "http://localhost:8080/",
  "timestamp": "1590828656781",
  "userAgent": "chrome",
  "kind": "experience",
  "type": "longTask",
  "eventType": "mouseover",
  "startTime": "9331",
  "duration": "200",
  "selector": "HTML BODY #container .content"
}
```

## PV(page view) 
- 是页面浏览量，UV(Unique visitor)用户访问量。PV 只要访问一次页面就算一次，UV 同一天内多次访问只算一次。

```json
{
  "title": "前端监控系统",
  "url": "http://localhost:8080/",
  "timestamp": "1590829304423",
  "userAgent": "chrome",
  "kind": "business",
  "type": "pv",
  "effectiveType": "4g",
  "rtt": "50",
  "screen": "2049x1152"
}
```
