import sys
import os
import socket
import ctypes

def check_admin_rights():
    return ctypes.windll.shell32.IsUserAnAdmin()
    
    
def your_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return ip
    
    
if __name__ == "__main__":
    isAdmin = check_admin_rights()
    print("admin rights: {}".format(isAdmin))
    
    # do something here with admin privilages
