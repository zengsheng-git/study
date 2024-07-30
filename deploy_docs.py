
# 参考链接 https://blog.csdn.net/zengliguang/article/details/136616982
# 需要安装的库
# pip install paramiko

# from deploy_azure import upload_to_azure
import os
import paramiko

def upload_folder_to_remotes(local_folder, remote_paths, hostname='10.0.8.18', port=22, username='root', password='siteview'):
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
local_folder = 'D:/w/dumi-study/dist'
remote_paths = [
    '/www/wwwroot/dumi-study.com/study/',
    # '/www/wwwroot/casey.cgnewout.com.yin/',
    # '/www/wwwroot/casey.cgnewout.com.yinGe/',
    # '/www/wwwroot/casey.cgnewout.com.pro/',
    ]
upload_folder_to_remotes(local_folder, remote_paths)

# upload_to_azure()
