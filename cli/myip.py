#!/usr/bin/env python3

import urllib.request, json
import requests
def retrive_ip():
    """ Retrieve the external ip adress using api.myip.com
        Json gets converted to python dict and string containg ip is returned.
    """
    url = "https://api.myip.com"
    my_socket = urllib.request.urlopen(url)
    json_data = my_socket.read().decode()
    my_socket.close()
    dict_data = json.loads(json_data)
    #return dict_data["ip"]
    print(dict_data["ip"])

def retrive_ip2():
    import requests
    r = requests.get(r'http://jsonip.com')
    # r = requests.get(r'https://ifconfig.co/json')
    ip= r.json()['ip']
    print('Your IP is {}'.format(ip))

def retrive_ip3():
    import requests
    r = requests.get(r'https://api.myip.com')
    print(r.json())
    ip= r.json()['ip']
    print('Your IP is {}'.format(ip))



#print(retrive_ip())
#retrive_ip()
#retrive_ip2()
retrive_ip3()
