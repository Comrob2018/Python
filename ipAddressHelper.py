import ipaddress

def ipv4addr(ip):
    '''
    This Function takes user ip address input and determines what class network the ip address is, 
    and gives the user inforamtion about the network class and private address range for the 
    address provided.
    '''
    classA= ' is a Class A IP v4 address. Class A private address range is 10.0.0.0 to 10.255.255.255.'
    classB= ''' is a Class B IP v4 address. Class B private address range is 172.16.0.0 to 172.31.255.255. 
    Additionally, there is the APIPA address range which is 169.254.0.1 through 169.254.255.254.
    '''
    classC= ' is a Class C IP v4 address. Class C private address range is 192.168.0.0 to 192.168.255.255.'
    classD= ' is a Class D IP v4 address. These addresses are used for multicast traffic and not available for hosts.'
    classE= ' is a Class E IP v4 address. These addresses are reserved for future use and are not available for private or public use.'
    iplst = ip.split('.')
    for x in iplst:
        if int(x) in range(0,255):
            if len(x) < 4:
                if int(x) in range(0, 128):
                    print(ip + classA) 
                elif int(x) in range(128, 192):
                    print(ip +  classB)
                elif int(x) in range(192, 224):
                    print(ip +  classC)
                elif int(x) in range(224, 240):
                    print(ip + classD)
                elif int(x) in range(240, 255):
                    print(ip + classE)
    for x in iplst:
        realip = '.'.join(iplst)
        while True:
            try:
                ipaddress.ip_address(realip)
            except ValueError:
                print('This is not a valid IP v4 address.')
                break
            
def subnetting(subnet):
    #This function determines if the subnet mask is valid.
    subnetcheck = ['0','128','192','224','240','248','252','254','255']
    subnetlist = subnet.split('.')
    num=''
    if subnetlist[0] == '255':
        if subnetlist[1] in subnetcheck:
            if subnetlist[2] in subnetcheck:
                if subnetlist[3] in subnetcheck:
                    for octet in subnetlist:
                        x = bin(int(octet))
                        num +=str(x[2::1])
                    cidr= num.count('1')
                    print('Your CIDR notation is /' + str(cidr) + '.')
                    return cidr
                print('This is not a valid subnet mask.')
                return False
            print('This is not a valid subnet mask.')
            return False
        print('This is not a valid subnet mask.')
        return False
    print('This is not a valid subnet mask.')
    return False


def network_id(ip, cidr):
    # This returns the subnet id when given the ip address and the cidr notation.
    x = ip + '/' + cidr
    global net_id
    net_id = ipaddress.ip_network(x, strict=False)
    return 'Your subnet id is ' + str(net_id) + '.'

def hostrange(ip, net_id):
    # This is to return the host ip address range for the ip address and network id provided.
    # It also outputs all available host addressess to a file. 
    hostrng = []
    iplist = open('iplist.txt', "w")
    for ip in ipaddress.ip_network(net_id):
        hostrng.append(str(ip))
    iplist.write('Here are your available hosts: '+ str(hostrng[1:-1]))
    return '''
    There are {0} host ip addresses available on this subnet.
    The first useable host ip address is {1}. 
    The last useable host ip address is {2}. 
    Your broadcast IP address is {3}.
    '''.format(str(len(hostrng[1:-1])), hostrng[1], hostrng[-2], str(hostrng[-1]))

def main():
    ip=input('What is your IP v4 address? ')
    subnet=input('What is your subnet mask? ')
    print(ipv4addr(ip))
    print(subnetting(subnet))
    if ipv4addr(ip) and subnetting(subnet):
        print(network_id(ip, str(cidr)))
        print(hostrange(ip, net_id))

if __name__=='__main__':
    main()
