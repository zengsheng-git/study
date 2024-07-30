---
title: deploy-upload
order: 4
toc: content
nav:
  title: 项目记录
  order: 6
group: 
  title: 进阶项目
  order: 2
---

## 配置运行脚本
```
"deploy": "python deploy.py",
"deploy_azure": "python deploy_azure.py",
```

## 上传到Linux服务器
- 新建deploy.py文件
``` py

# 参考链接 https://blog.csdn.net/zengliguang/article/details/136616982
# 需要安装的库
# pip install paramiko

from deploy_azure import upload_to_azure
from send_dingding_message import send_message
import os
import paramiko

def upload_folder_to_remotes(local_folder, remote_paths, hostname='******', port=22, username='******', password='******'):
    """
    循环上传本地文件夹及其内容到多个远程服务器指定路径。
    
    :param local_folder: 本地文件夹路径
    :param remote_paths: 远程服务器基础路径的列表
    :param hostname: 远程主机IP或域名
    :param port: SSH端口，默认22
    :param username: 登录用户名
    :param password: 登录密码
    """
    # 创建SSH客户端对象
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # 连接到远程服务器
    ssh.connect(hostname=hostname, port=port, username=username, password=password)
    
    try:
        # 使用SFTP打开一个通道
        with ssh.open_sftp() as sftp:
            # 对于每个远程基础路径
            for remote_base_path in remote_paths:
                # 遍历本地文件夹并将文件及子文件夹上传到远程服务器
                for root, dirs, files in os.walk(local_folder):
                    relative_path = os.path.relpath(root, local_folder)
                    remote_path = remote_base_path + relative_path.replace("\\", "/")
                    
                    # 尝试列出远程目录，如果失败则创建目录
                    try:
                        sftp.listdir(remote_path)
                    except IOError:
                        sftp.mkdir(remote_path)
                        print(f"创建目录: {remote_path}")
                    
                    for file in files:
                        local_file_path = os.path.join(root, file)
                        remote_file_path = os.path.join(remote_path, file).replace("\\", "/")
                        
                        try:
                            sftp.put(local_file_path, remote_file_path)
                            print(f"文件 {local_file_path} 成功上传到 {hostname}:{remote_file_path}")
                        except Exception as e:
                            print(f"文件 {local_file_path} 上传过程中发生错误: {str(e)}")
    finally:
        # 确保SSH连接被关闭
        ssh.close()

# 使用
local_folder = 'D:/w/lmm/LMM-Frontend/dist'
remote_paths = [
    '/www/wwwroot/casey.cgnewout.com/', 
    '/www/wwwroot/casey.cgnewout.com.yin/',
    '/www/wwwroot/casey.cgnewout.com.yinGe/',
    '/www/wwwroot/casey.cgnewout.com.pro/',
    ]
upload_folder_to_remotes(local_folder, remote_paths)

upload_to_azure()

send_message('******')

```


## 上传到Azure
- 新建deploy_azure.py文件
``` py
# 需要安装的库
#pip install azure-storage-blob

import os
from azure.storage.blob import BlobServiceClient, ContentSettings
from mimetypes import guess_type

# Azure Storage Account信息
account_name = "lmmwebapp"
account_key = "******"
container_name = "$web"

# 初始化Blob Service Client
connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"
service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = service_client.get_container_client(container_name)

def upload_recursive(local_dir, blob_prefix=""):
    for root, dirs, files in os.walk(local_dir):
        relative_path = os.path.relpath(root, local_dir)
        if relative_path != '.':
            current_blob_prefix = os.path.join(blob_prefix, relative_path).replace("\\", "/")
        else:
            current_blob_prefix = blob_prefix

        for file in files:
            local_file_path = os.path.join(root, file)
            blob_name = os.path.join(current_blob_prefix, file).replace("\\", "/")
            blob_client = container_client.get_blob_client(blob_name)

            # 获取文件的MIME类型
            mime_type, _ = guess_type(local_file_path)
            content_settings = ContentSettings(content_type=mime_type or 'application/octet-stream')

            with open(local_file_path, "rb") as data:
                blob_client.upload_blob(data, content_settings=content_settings, overwrite=True)
                print(f"File uploaded: {blob_name} with MIME type: {mime_type}")

def upload_to_azure():
    print("\n 开始部署 Azure...")
    try:
        upload_recursive("./dist")
        print("\n 恭喜您，Azure 部署成功了^_^")
    except Exception as e:
        print(f"\n Azure 部署失败 {e}")

if __name__ == "__main__":
    upload_to_azure()

```


## 发送钉钉消息
``` py

import requests
import json
from datetime import datetime

def send_message(webhook_url):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    title = f"LMM 更新提醒"
    content= "\n ## LMM web端页面更新啦！ \n 1. [符哥测试环境](http://10.0.8.18:10091) \n 2. [尹哥测试环境](http://10.0.8.18:10092) \n 3. [本地线上测试环境](http://10.0.8.18:10090) \n 4. [线上测试环境](https://lmm.dnet.us) \n 4. [本地prod环境](http://10.0.8.18:10093)  \n![alt ALMFIRST](https://www.almfirst.com/wp-content/uploads/2019/02/logo-288x150.png)"
   
    markdown_text = f"""
    {current_time}
    {content}
    """
    
    headers = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    data = {
        # "msgtype": "text",
        # "text": {
        #     "content": message
        # },


        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": markdown_text
        },
        # 可选参数，如果机器人需要@某人
        "at": {
            "isAtAll": False  # 是否@所有人，默认为False
        }
    }
    response = requests.post(
        url=webhook_url,
        data=json.dumps(data),
        headers=headers
    )
    print('消息发送成功')
    return response.json()

# 使用示例  测试用的webhook_url
webhook_url = '******'

# response = send_message(webhook_url)
# print(response)

```
