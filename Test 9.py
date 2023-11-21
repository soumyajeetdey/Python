###############################################################################

#write a program to display the below IP addresses

#192.168.0.1
#192.168.0.2
#192.168.0.3
#..
#..
#192.168.0.10



###############################################################################

# This is not correct way of printing
for val in range(1,11):
    print("192.168.0.",val)
    
ip = '192.168.0.{}'
for val in range(1,11):
    print(ip.format(val))

ip = '192.168.0.'
for val in range(1,11):
    print(ip + str(val))
