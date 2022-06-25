from netmiko import ConnectHandler

myserver = {
        'device_type': 'linux',
        'host': '192.168.56.105',
        'username': 'meow',
        'password': 'meowmeow',
        'port': 22,
        'secret': '',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('apt update')

print(output)

