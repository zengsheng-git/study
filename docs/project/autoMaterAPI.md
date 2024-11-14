
## 查看断开占用
- sudo netstat -tuln
## 临时使用ll代替ls
- alias ll='ls -l'

## 安装mysql
- sudo apt install mysql-serve
- 登录到 MySQL 命令行客户端
sudo mysql -u root -p
- 查看 MySQL 版本
SELECT VERSION();
- 停止mysql
sudo systemctl stop mysql
- 卸载 MySQL 服务
	1. sudo apt-get remove mysql-server
	**清除配置文件**
	2. sudo apt-get purge mysql-server
	**清除数据目录**
	3. sudo rm -rf /var/lib/mysql

## 安装Java
sudo apt install openjdk-11-jdk
java -version

## 安装redis
- sudo apt install redis-server
- 运行 Redis 命令行客户端
redis-cli
- 查看 Redis 版本
info server
- 查看是什么系统
lsb_release -a

## 杀死服务
lsof -i :8084
kill pid

## 查看nohup.out日志
rm  nohup.out  -f
tail -f nohup.out



