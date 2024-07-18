<!--
 * @Author: sheng.zeng 1218128305@qq.com
 * @Date: 2024-07-18 18:18:05
 * @LastEditors: sheng.zeng 1218128305@qq.com
 * @LastEditTime: 2024-07-18 18:18:34
 * @FilePath: \dumi-study\code_docs-master\docs\project\react-native-windows.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# 项目路径
D:\w\lmm\rn\kk

# react-native-windows 开发Windows桌面应用

## 开发环境
 - 参考链接 https://blog.csdn.net/MichaelMCFD/article/details/124789768

## 构建打包发布
 - vs 选择 Release 和 X64 （顶部导航下面一栏）
 - 选择项目>发布>创建应用程序包，会打开新的弹窗 （顶部导航栏）
 - 选择旁加载，**不要**勾选自动更新
 - **使用**包签名，并选择创建证书，随便输入信息密码，并信任证书，一路点击下一步
 - 一路点击下一步
 - 等待打包完成会提示包在哪个路劲
 
 ## 安装应用包 （实际的安装包就是.msixbundle文件，其他的都是要信任证书而需要的脚本文件）
 - 进入到应用包文件夹
 ### 需要信任证书
	- 右键点击install.ps1,选择powershell运行，会要求你打开开发者模式，根据向导完成信任证书
 - 安装完成，即可打开程序
