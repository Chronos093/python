import paramiko

host = "ip_client"
user = "test"
password = "123456"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port=22, username=user, password=password)

channel = ssh.get_transport().open_session()
channel.invoke_shell()

while channel.recv_ready():
    channel.recv(1024)

channel.sendall("pwd\n")
print channel.recv(1024)

channel.sendall("cd..\n")

channel.sendall("pwd\n")
print channel.recv(1024)
