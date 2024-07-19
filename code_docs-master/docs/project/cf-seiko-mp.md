---
title: cf-seiko-mp
order: 8
toc: content
nav:
  title: 项目记录
  order: 7
group: 
  title: 项目记录
  order: 3
---


## 业务功能
* 发送验证码的状态码有误
* http是否要换https
* cf.juyunfuwu 上的图片全部要换过来
* taro 微信登录
* e70917ef700a8c3c58975c9d2e4c1363
* 接口http，图片https
* 体验版发送不了http接口，开启调试模式可以；只要接口支持https模式就行；
* 小程序发送订阅消息，模版ID
* wxca56d2ed52e8ed16 自己appid
* 标签属性动态写法   
  ```Javascript
    <View className="info_item">
        <Text className='name'>手机</Text>
        <Text data-tel='0769-82926753' className='content' onClick={this.ringUp.bind(this)}>18926031086</Text>
    </View>
  ```
  ```Javascript
    // 打电话
  ringUp(e) {
    const { dataset } = e.target
    Taro.makePhoneCall({
      phoneNumber: dataset.tel
    })
  }
  ```
* > 作用
  ``` Javascript
    "ignoreUploadUnusedFiles": false,
    "ignoreDevUnusedFiles ": false
  ```
* > 打开PDF
  ``` Javascript
    Taro.downloadFile({
          // 示例 url，并非真实存在
          url: 'http://183.63.138.50:8877/main/third/weixin/downloadFile/091ff275967b171a04293335aa0870fa',
          filePath: wx.env.USER_DATA_PATH +'/1.pdf',//自定义文件地址
          success: function (res) {
            console.info(res);
            const filePath = res.tempFilePath;
            Taro.openDocument({
              // filePath: filePath,
              filePath: wx.env.USER_DATA_PATH +'/1.pdf',//自定义文件地址
              fileType:'pdf',
              showMenu: true,// 右上角显示三个点，微信自带的api，可以保存、转发文件
              success: function (res) {
                console.log('打开文档成功')
                Taro.hideLoading() // 关闭loading
              },
              fail:res=>{
                console.info(res);
                Taro.hideLoading() // 关闭loading
              }
            })
          }
        })
  ``` 
* 两种下载的回顾
  * 下载到微信，并分享给朋友（3d模块的下载）
  * 打开PDF文件（产品目录的下载）
  * 发送下载链接到qq邮箱
* 值是上一次的，可使用定时器解决
* 回顾下载的两个过程，3d模块的下载到微信，产品目录的下载并打开
* 文件的下载和打开pdf，webview需要加入小程序的安全域名

----------------
## 开发
* 预览和发布上传时压缩代码的勾选
* 命令的区别
    * `"dev:weapp": "SET NODE_OPTIONS=--openssl-legacy-provider && npm run build:weapp --watch --env production"`,
    * `"dev:weapp": "SET NODE_OPTIONS=--openssl-legacy-provider && npm run build:weapp -- --watch"`,
    * `"build:weapp": "SET NODE_OPTIONS=--openssl-legacy-provider && taro build --type weapp"`,


---------------------
## 临时记录

* https://qiniu.juyunfuwu.cn/cf/3d/CFX14M-C1-1040L.STEP?e=1692277268&token=L0My403x2tKerLom6Pc0Rh9LzTPlAE0xrdagiUfY:s9Om2G3gs3OvIspFJJZMR1Gm0Q0=

* url:'http://'+this.state.url,  singleSelect/download.tsx  282

* 13923367220

本机型号 model
皮带形式 D
导程  lead
移动行程 stroke_value
马达位置  connect_value
厂牌 BrandVal + 电机容量功率 capacity_value
原点感应器 origin_value
极限感应器 limit_value

ZCH5B-BL-100W-50L.STEP

BrandVal: ["Y"]
brand_value: ""
capacity_value: "100W"
category_name: "内嵌皮带滑台系列"
category_type: ""
connect_url: "http://qiniu.juyunfuwu.cn/zch202308/connect/ZCH5B-BL.png?e=1692694429&token=L0My403x2tKerLom6Pc0Rh9LzTPlAE0xrdagiUfY:w0VNpX54D92LbqvUcmeXjr6rtW4="
connect_value: "BL"
control_value: ""
delivery_time: "5个工作日"
encoder_value: ""
id: "481776677551086114"
lead: 30
limit_value: "4"
model: "ZCH5B"
origin_value: "C"
sensor_model: "EE-SX674(NPN)"
sensor_model_in: ""
stroke_value: 50

型号详情-3D名称需根据产品参数组装，组装规则：产品名称-导程-行程-马达位置-厂牌功率-原点感应器-端点极限感应器（曾工）
型号详情-公称型号需根据产品参数组装，目前是创锋的公称型号，组装规则：产品名称-导程-行程-马达位置-厂牌功率-原点感应器-端点极限感应器（曾工）



--------
/cf/seiko/products/list/single
sensor_model



