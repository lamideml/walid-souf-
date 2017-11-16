
BLUE = '\033[94m'
RED = '\033[91m'
GREEN = '\033[32m'
Magenta = '\033[95m'
Yellow = '\033[93m'
import os
import time
import webbrowser
import platform
print(BLUE+"""
#####################################################################
                .__  .__    .___            __           .__  .__ 
__  _  _______  |  | |__| __| _/           |  | _______  |  | |__|
\ \/ \/ /\__  \ |  | |  |/ __ |    ______  |  |/ /\__  \ |  | |  |
 \     /  / __ \|  |_|  / /_/ |   /_____/  |    <  / __ \|  |_|  |
  \/\_/  (____  /____/__\____ |            |__|_ \(____  /____/__|
              \/             \/                 \/     \/ 
              **WALID SOUF**        
######################################################################
""")
print(Yellow+"start time:",time.asctime())
print(Magenta+"""
**************************************
1: install vm tools in kali linux
**************************************
2:install carte wifi 
**************************************
3:install vpn in kali linux
**************************************
4:my facebook
**************************************





""")

while 1:
   try:
     user=int(input(GREEN+"CHOICE NUMBER:   "))
     if user>4:
      print(RED+"error choice")
     if user==1:
       a = open("/etc/apt/sources.list", "w")
       a.write("""deb http://http.kali.org/kali kali-rolling main contrib non-free
       # For source package access, uncomment the following line
       # deb-src http://http.kali.org/kali kali-rolling main contrib non-free """)
       a.close()
       print(GREEN+"Dane")
       print(GREEN+"Please Wait.........")
       os.system("sudo apt-get update")
       os.system("sudo apt-get install open-vm-tools-desktop -y")
       print(GREEN+"Successfully installed ")
       time.sleep(1)
       print(GREEN+"Dane")
       print("Now will be reboot Driver")
       os.system("reboot")


     if user==2:
       os.system("git clone https://github.com/mehedishakeel/BroadcomInstaller2017.git")
       os.system("cd BroadcomInstaller2017/")
       os.system("cd  /root/Desktop/untitled/BroadcomInstaller2017")
       os.system("chmod +x /root/Desktop/untitled/BroadcomInstaller2017/Broadcom.sh")
       print("dane")
       os.system("sudo /root/Desktop/untitled/BroadcomInstaller2017/./Broadcom.sh")
     if user==3:
       os.system("apt-get install network-manager-openvpn-gnome ")
       os.system("apt-get install network-manager-pptp")
       os.system("apt-get install network-manager-pptp-gnome")
       os.system("apt-get install network-manager-strongswan")
       os.system("apt-get install network-manager-vpnc")
       os.system("apt-get install network-manager-vpnc-gnome")
       #os.system("/etc/init.d/network-manager restart")
       print("Successfully installed")
       
       

     if user==4:
       c=webbrowser.open("https://web.facebook.com/profile.php?id=100010519515586")
       print("ok will be open browser")


   except:
       print(RED+" error....use number")

       





