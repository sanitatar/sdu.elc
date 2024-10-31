import requests#请求
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import schedule
import time
import xlwt
import json
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('building&id', cell_overwrite_ok=True)
worksheet1 = workbook.add_sheet('凤凰居6号楼', cell_overwrite_ok=True)
worksheet2 = workbook.add_sheet('B5号楼', cell_overwrite_ok=True)
worksheet3 = workbook.add_sheet('B2', cell_overwrite_ok=True)
worksheet4 = workbook.add_sheet('T1', cell_overwrite_ok=True)
worksheet5 = workbook.add_sheet('S1一多书院', cell_overwrite_ok=True)
worksheet6 = workbook.add_sheet('S11', cell_overwrite_ok=True)
worksheet7 = workbook.add_sheet('B9', cell_overwrite_ok=True)
worksheet8 = workbook.add_sheet('凤凰居9号楼', cell_overwrite_ok=True)
worksheet9 = workbook.add_sheet('凤凰居2号楼', cell_overwrite_ok=True))
json_data={"query_elec_roominfo":{"retcode":"0", "errmsg":"房间当前剩余电量350.91",  "aid":"0030000000002505", "account":"823744",  "meterflag":"amt", "bal":"",  "price":"0", "pkgflag":"none", "area":{"area":"青岛校区","areaname":"青岛校区"},  "building":{"buildingid":"1503975890","building":"凤凰居2号楼"},  "floor":{"floorid":"","floor":""},  "room":{"roomid":"b228","room":"b228"}, "pkgtab":[ ]}}
data=f"jsondata={urllib.parse.quote(json.dumps(json_data,ensure_ascii=False))}&funname=synjones.onecard.query.elec.building&json=true"
headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; SM-G988N Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
}
request = urllib.request.Request("http://10.100.1.24:8988/web/Common/Tsm.html",data=data.encode('utf-8'),headers=headers, method="POST")
response = urllib.request.urlopen(request)
html = response.read().decode("utf-8")
print(html)
# a=re.compile(r'"building":"(.*?)"')
# b=re.compile(r'"buildingid":"(.*?)"')
# building=re.findall(a,html)
# buildingid=re.findall(b,html)
# for i in range(0,len(building)):
#     worksheet.write(i,0,building[i])
# for i in range(0, len(buildingid)):
#     worksheet.write(i, 1, buildingid[i])
# workbook.save("山大电力.xls")