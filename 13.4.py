from ipaddress import * 
for mask in range(33):
    net = ip_network(f'215.181.200.27/{mask}', 0)
    print(net, net.netmask)