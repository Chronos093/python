import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('HOST', port=22, username='USERNAME', password='PASSWORD')

channel = client.get_transport().open_session()
channel.invoke_shell()

while channel.recv_ready():
    channel.recv(1024)

channel.sendall("pwd\n")
print channel.recv(1024)

channel.sendall("cd..\n")

channel.sendall("pwd\n")
print channel.recv(1024)
