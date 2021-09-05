#staplish connect to the target maschine
import socket
from IPy import IP
                                                                                                  
print("                                                                                                     ")
print("                                                                                                     ")
print("              /+.      `/+o+/:       /+      -+++//.                            -+o+-                ")
print("              /Nhd     +No---:+      smmy     oM/::+mm`                         ym/-:hd`             ")
print("             -N/`ms    dN.          /M--M/    oM`   :M+ oh+oso -yyssy/         +M-   `Ny             ")
print("            `my  -M/   `ohddhs:    .N+  +N.   oM+++omh` yM-   :M/   -No        yM     dm             ")
print("            yMsooomN.       `/Ms  `mNooooNm`  oM/::-`   ym    yN     hm  yhhh: sM`    mh             ")
print("           +M:-----hd` -`    .Ny  yN------my  oM`       ym    :M/   -No        .Ns   /M:             ")
print("          .d+      `d+ +hhyyhh+` :d:      -d: /d`       oy     -yyssy/          .shyhy-              ")
print("                                                                                                     ")
print("                                                                                                     ")
 
def scan (target):
    converted_ip = check_ip(target)
    print ("\n"+"[-_0 Scanning the target " + st(target))
    for port in range(1, 100):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return  s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.1)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] port ' + str(port) + ":" + str(banner.decode().strip('\n')))
        except:
            print("[+] open port :" + str(port) + " !" )
    except:
        #print('[-] port ' + str(port) + ' is closed !')
        pass

targets = input('[+] Enter your Targets to scan: ')

if "," in targets:
    for ip_add in targets.split(","):
        scan(ip_add.strip(" "))
else:
    scan(targets)

