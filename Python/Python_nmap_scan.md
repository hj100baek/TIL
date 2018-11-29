#### port scan 

```python

#Requirements 
# install nmap
# file_name: nmap_scan.py
import nmap
import sys
import socket

if len(sys.argv) !=3:
    print("nmap_scan.py <Hostname> <Port_Range>")
    sys.exit(0)

_hostname = sys.argv[1]
_portrange = sys.argv[2]

ipaddress = socket.gethostbyname(_hostname)  # hostname -> ip

print("==========" * 7)
print('     Scanning Hostname: ', _hostname, ',' 'IP: ', ipaddress)
print("==========" * 7)

try:
    nmscan = nmap.PortScanner()
    nmscan.scan(ipaddress, _portrange) # scan host 127.0.0.1, ports from 22 to 44
except:
    print("Unexcepted error")
    sys.exit(0)

 # get all hosts that were scanned    
for host in nmscan.all_hosts():
     print('Host : %s (%s)' % (host, nmscan[host].hostname()))
     print('State : %s' % nmscan[host].state())

     for proto in nmscan[host].all_protocols():
         print('Protocol : %s' % proto)

         lport = nmscan[host][proto].keys()
         sorted(lport) # lport.sort() -> python3 AttributeError: 'dict_keys' object has no attribute 'sort'
         for port in lport:
                print('port : %s\tstate : %s' % (port, nmscan[host][proto][port]['state']))
     print("==========" * 7)

###
#  python nmap_scan.py www.hostname.com 30-9000
###

======================================================================
     Scanning Hostname:  www.hostname.com ,IP:  203.249.161.90
======================================================================
Host : 203.249.161.90 (www.hostname.co.kr)
State : up
Protocol : tcp
port : 80       state : open
port : 443      state : open
======================================================================

```

