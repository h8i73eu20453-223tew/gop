from time import strftime
import os
import sys
import requests
from time import sleep
from datetime import datetime, timedelta
import requests
import os
try:
  from faker import Faker
  import requests
  from colorama import Fore, Style
  import re
  import pystyle
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  print('__Vui Lòng Chạy Lại Tool__')
# màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = '\033[1;39m'
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
os.system("cls" if os.name == "nt" else "clear")

# đánh dấu bản quyền
ndp_tool = "\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

ip = requests.get("https://api.ipgeolocation.io/getip").json()
def banner():
    banner = f"""


\033[1;34m ╭╮╱╭┳━━┳━━━┳╮╱╭╮╱╭━━━━┳━━━┳━━━┳╮
\033[1;37m ┃┃╱┃┣┫┣┫╭━━┫┃╱┃┃╱┃╭╮╭╮┃╭━╮┃╭━╮┃┃
\033[1;34m ┃╰━╯┃┃┃┃╰━━┫┃╱┃┃╱╰╯┃┃╰┫┃╱┃┃┃╱┃┃┃
\033[1;37m ┃╭━╮┃┃┃┃╭━━┫┃╱┃┣━━╮┃┃╱┃┃╱┃┃┃╱┃┃┃╱╭╮
\033[1;34m ┃┃╱┃┣┫┣┫╰━━┫╰━╯┣━━╯┃┃╱┃╰━╯┃╰━╯┃╰━╯┃
\033[1;37m ╰╯╱╰┻━━┻━━━┻━━━╯╱╱╱╰╯╱╰━━━┻━━━┻━━━╯
\033[1;34m 𝐀𝐃𝐌𝐈𝐍_𝐇𝐈𝐄𝐔_𝐓𝐎𝐎𝐋
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m────────────────────────────────────────────────────────────
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;39m┌────────────────────────💚 HIẾU TOOL💚────────────────────────┐
\033[1;32m║   \033[1;39mPYTHON VERSION\033[1;32m     :  4.2                                  \033[1;32m║
\033[1;32m║   \033[1;39mZALO               :  84939271874                          \033[1;32m║
\033[1;32m║   \033[1;39mGROP_zalo          :  https://zalo.me/g/wfakde942          \033[1;32m║
\033[1;32m║   \033[1;39mYOUTUBER           :  HIẾU TOOL                            \033[1;32m║
\033[1;32m║   \033[1;39mYOTUBE_LINK        :  https://www.youtube.com/@hieutool248 \033[1;32m║
\033[1;39m└──────────────────────────────────────────────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;31m────────────────────────────────────────────────────────────
"""

    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)
banner()


print(f"\033[1;37m\033[1;33mip của bạn là: {ip['ip']}  \033[1;37m")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Trao Đổi Sub  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool TDS FB FULL JOD\033[1;31m[\033[1;33mlive\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTool TDS FB VIP\033[1;31m[\033[1;33mlive\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mTool TDS Pro5 {1 page}\033[1;31m[\033[1;33mlive\033[1;31m]")

print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4\033[1;31m] \033[1;32mTool TDS IG \033[1;31m[\033[1;33mV1\033[1;31m] \033[1;31m[\033[1;33mlive\033[1;31m]")

print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m5\033[1;31m] \033[1;32mTool TDS TikTok & TDS TIKTOK NOW \033[1;31m[\033[1;33mlive\033[1;31m] ")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═══════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Tương Tác Chéo  \033[1;37m║")
print("\033[1;37m╚═══════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m6\033[1;31m] \033[1;32mTool TTC TikTok [chưa fix] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m7\033[1;31m] \033[1;32mTool TTC Pro5 \033[1;31m[\033[1;33mlive\033[1;31m]  ")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Tiện Ích      \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m8\033[1;31m] \033[1;32mTool Đào Mail ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m9\033[1;31m] \033[1;32mTool Tạo Thẻ Thanh Toán ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m10\033[1;31m] \033[1;32mTool Check Valid")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m11\033[1;31m] \033[1;32mTool LOC PROXY \033[1;31m[\033[1;33mlive\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m12\033[1;31m] \033[1;32mtool buff view,tym,.. tiktok\033[1;31m『\033[1;33mNEW\033[1;31m』 ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m13\033[1;31m] \033[1;32mTool Get Cookie Pro5 Facebook\033[1;31m『\033[1;33mNEW\033[1;31m』")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool PROFILE       \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
# print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m14\033[1;31m] \033[1;32mTool Reg Page Pro5")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m15\033[1;31m] \033[1;32mTool SHARE Facebook")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m16\033[1;31m] \033[1;32mTool Reg Page Pro5 \033[1;31m[\033[1;33mV2\033[1;31m]")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m17\033[1;31m] \033[1;32mTOOL TĂNG SHARE AO BẰNG TOKEN")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m18\033[1;31m] \033[1;32mTool Buff View Story Max Speed Pro5 ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool SPAM SMS      \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m19\033[1;31m] \033[1;32mtool spam sms\033[1;31m[\033[1;33mV5\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m20\033[1;31m] \033[1;32mTool SPAM SMS \033[1;31m[\033[1;33mV6\033[1;31m] ")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔══════════════╗")
print("\033[1;37m║ \033[1;33mTool Golike  \033[1;37m║")
print("\033[1;37m╚══════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m21\033[1;31m] \033[1;32mTool Golike Tiktok ")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m00\033[1;31m] \033[1;32mThoát Tool")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═══════════╗")
print("\033[1;37m║\033[1;33mhỗ trợ Tool\033[1;37m║")
print("\033[1;37m╚═══════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m101\033[1;31m] \033[1;32mĐể support qua zalo ngay")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m102\033[1;31m] \033[1;32mĐể vào nhóm zalo cập nhật tool")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m103\033[1;31m] \033[1;32mĐể vào kênh yotube")

print("\033[1;31m────────────────────────────────────────────────────────────")

chon = int(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;37m: \033[1;33m'))
#tool tds
try:
	if chon == 1 :
		response = requests.get('https://run.mocky.io/v3/6f026b34-572d-4fdb-b6a2-76492bb73a32')
		exec(response.text)
	elif chon == 2:
		response = requests.get('https://run.mocky.io/v3/b452f892-505d-4481-b043-e320b0217053')
		exec(response.text)
	elif chon == 3 :
		response = requests.get('https://run.mocky.io/v3/956f97cd-10d8-4b85-8cf9-42ec97d4674b')
		exec(response.text) 
	elif chon == 4 :
		response = requests.get('https://run.mocky.io/v3/ed772142-2a09-42fb-a67b-7183e7c78145')
		exec(response.text)
	elif chon == 5 : 
		response = requests.get('https://run.mocky.io/v3/30e697ca-46ff-4516-b99f-2fba9ad55670')
		exec(response.text)
	#tool ttc
	elif chon == 6 :
		response = requests.get('')
		exec(response.text)
	elif chon == 7 :
		response = requests.get('https://run.mocky.io/v3/5b26d318-842a-410d-9459-b9ba0cc446f6')
		exec(response.text)
	#tool công cụ 
	elif chon == 8 :
		response = requests.get('https://run.mocky.io/v3/4a04c1b4-e556-42fa-ab56-627cc1f46cea')
		exec(response.text)
	elif chon == 9 :
		response = requests.get('https://run.mocky.io/v3/e1cb6200-5193-424f-9b60-a663e761d861')
		exec(response.text)
	elif chon == 10 :
		response = requests.get('https://run.mocky.io/v3/a8b7d110-4b72-4b36-a1f3-203d47125ff1')
		exec(response.text)
	elif chon == 11 :
		response = requests.get('https://run.mocky.io/v3/a51afbc0-ad47-418b-adee-4d629ae8296c')
		exec(response.text)
	elif chon == 12 :
		response = requests.get('https://run.mocky.io/v3/9311a738-f03d-4dfd-8ef3-42833ee9af70')
		exec(response.text)
	elif chon == 13 :
		response = requests.get('https://run.mocky.io/v3/3c324b5b-db85-4560-9f52-417a546b9e2e')
		exec(response.text)
	elif chon == 14:
		response = requests.get('')
		exec(response.text)
	elif chon == 15 :
		response = requests.get('https://run.mocky.io/v3/13a2a17b-521d-4470-9ea2-70b53bdea2b0')
		exec(response.text)
	elif chon == 16 :
		response = requests.get('https://run.mocky.io/v3/7ac4aa31-751d-46b0-bea7-fffe315f6219')
		exec(response.text)
	elif chon == 17 :
		response = requests.get('https://run.mocky.io/v3/11b0b7ed-e305-443a-9e08-e95c7e074933')
		exec(response.text)
	elif chon == 18 :
		response = requests.get('https://run.mocky.io/v3/f03a1dea-6c77-4609-9aab-26cfb79255e8')
		exec(response.text)
	elif chon == 19 :
		response = requests.get('https://run.mocky.io/v3/d04b932d-a0d5-4a42-b10c-aba744c6a88d')
		exec(response.text)
	elif chon == 20 :
		response = requests.get('https://run.mocky.io/v3/ca359ed8-e6ec-4b21-95ad-9c0e54f2cfb3')
		exec(response.text)
	elif chon == 21 :
		response = requests.get('https://run.mocky.io/v3/1803836a-81b1-44f1-8975-11d8c913eca8')
		exec(response.text)
	elif chon == 22 :
		response = requests.get('')
		exec(response.text)
	elif chon == 00 :
		response = requests.get('https://run.mocky.io/v3/e3c7f69b-0036-4daf-8543-3ce627c477ff')
		exec(response.text)
	elif chon == 101:
		os.system("termux-open-url https://zalo.me/84939271874")
	elif chon == 102:
		os.system("termux-open-url https://zalo.me/g/wfakde942")
	elif chon == 103:
		os.system("termux-open-url https://www.youtube.com/@hieutool248")
	else :
		exit()
except:
	print("\033[1;31m"'''Kiểm Tra kết nối mạng
hoặc sever chứa tool đang có lỗi
hay admin muốn gửi tới Mấy thằng tính bug thì có cái cc''') 
