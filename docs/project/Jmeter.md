
## 点击 .jmx文件直接 打开Jemter客户端 
- 管理员权限打开cmd
> 输入命令 `Assoc .jmx=jmeter`
> `FType jmeter="c:\apps\jmeter\bin\jmeter-t.cmd" %1`


## 生成测试报告
D:\w\lmm\lmm-frontend-test\Jmeter/.test.txt  可以不存在，如果存在必须为空文件
D:\w\lmm\lmm-frontend-test\Jmeter/report     可以不存在，如果存在必须为空文件夹

- 设置jmeter 环境变量前，需要在安装目录下执行
jmeter -n -t D:\w\lmm\lmm-frontend-test\Jmeter/test.jmx -l D:\w\lmm\lmm-frontend-test\Jmeter/.test.txt -e -o D:\w\lmm\lmm-frontend-test\Jmeter/report

- 设置jmeter 环境变量后，任意目录下执行
jmeter -n -t ./test.jmx -l ./test.txt -e -o ./report




