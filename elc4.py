import requests#请求
import urllib.request, urllib.parse, urllib.error#urllib
from bs4 import BeautifulSoup
import re#正则
import schedule#周期性执行任务
import time#获取当前时间
import xlwt#表格
import json#jsondata解码
from win11toast import toast#windows提醒
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
def job():
    print("check it!")
    #判断用户电量是否充足
    if float(elc[0]) > dick :
       toast('电量完全OK',image=r'C:\Users\xiang\OneDrive\图片\微信图片_20241030221137.png')
    else:
        toast('你电没了,赶快发电',duration='long',
        image=r'C:\Users\xiang\OneDrive\图片\微信图片_20241030221137.png')
        #邮件提醒
        if ass ==1:
            msg = MIMEText("没电了赶快发电", 'html', 'utf-8')  # 设置内容，和内容的格式编码
            msg["From"] = formataddr(["爱发电", "xiangjunxiaonb@163.com"])  # 编辑发送人和发送的邮箱
            msg['to'] = str("\""+mail+"\"") # 发送的目标地址
            msg['Subject'] = '速速发电'  # 发送邮件的主题名
            server = smtplib.SMTP_SSL("smtp.163.com")  # 创建与邮件服务器连接
            server.login("xiangjunxiaonb@163.com", "NEgS836VsPa5Jtn3")  # 账户和授权码
            server.sendmail("xiangjunxiaonb@163.com",str("\""+mail+"\""), msg.as_string())
            print("邮件发送成功")# 发送邮件， msg.as_string()为我们构建的邮件内容
        else:
            print("邮箱提醒未开启")
    print(elc[0])
#查询用url（fiddler抓包获得）
url="http://10.100.1.24:8988/web/Common/Tsm.html"
#请求头
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; RMX1931 Build/PQ3A.190605.09201023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
     }
#判断用户是否需要表格
fuck=int(input("是否需要楼栋编号对照表(是请输入1，否则输入2)："))
if fuck == 1 :
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('building&id', cell_overwrite_ok=True)
    #fiddler抓包获得楼栋信息
    json_data={"query_elec_building":{"retcode":"0", "errmsg":"请选择相应的楼栋：",  "aid":"0030000000002505", "account":"823872", "area":{"area":"青岛校区","areaname":"青岛校区"},  "buildingtab":[ { "buildingid":"1503975980", "building":"凤凰居6号楼" },{ "buildingid":"1661835273", "building":"B5号楼" },{ "buildingid":"1661835256", "building":"B2" },{ "buildingid":"1574231830", "building":"T1" },{ "buildingid":"1503975832", "building":"凤凰居1号楼" },{ "buildingid":"1503975832", "building":"S1一多书院" },{ "buildingid":"1599193777", "building":"S11" },{ "buildingid":"1693031698", "building":"B9" },{ "buildingid":"1503976004", "building":"凤凰居9号楼" },{ "buildingid":"1503975890", "building":"凤凰居2号楼" },{ "buildingid":"1503975967", "building":"S5凤凰居5号楼" },{ "buildingid":"1503976037", "building":"凤凰居10号楼" },{ "buildingid":"1503975890", "building":"S2从文书院" },{ "buildingid":"1693031710", "building":"阅海居B10楼" },{ "buildingid":"1693031698", "building":"阅海居B9楼" },{ "buildingid":"1574231835", "building":"T3" },{ "buildingid":"1503976004", "building":"S9凤凰居9号楼" },{ "buildingid":"1503975988", "building":"S7凤凰居7号楼" },{ "buildingid":"1503976037", "building":"S10凤凰居10号楼" },{ "buildingid":"1503975995", "building":"S8凤凰居8号楼" },{ "buildingid":"1599193777", "building":"凤凰居11/13号楼" },{ "buildingid":"1574231833", "building":"专家公寓2号楼" },{ "buildingid":"1503975902", "building":"凤凰居3号楼" },{ "buildingid":"1693031710", "building":"B10" },{ "buildingid":"1661835249", "building":"B1" },{ "buildingid":"1503975950", "building":"凤凰居4号楼" },{ "buildingid":"1503975980", "building":"S6凤凰居6号楼" }]}}
    #json解码
    data=f"jsondata={urllib.parse.quote(json.dumps(json_data,ensure_ascii=False))}&funname=synjones.onecard.query.elec.building&json=true"

    request = urllib.request.Request("http://10.100.1.24:8988/web/Common/Tsm.html",data=data.encode('utf-8'),headers=headers, method="POST")
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    a=re.compile(r'"building":"(.*?)"')#正则提取
    b=re.compile(r'"buildingid":"(.*?)"')
    building=re.findall(a,html)
    buildingid=re.findall(b,html)
    #写入信息和保存表格
    for i in range(0,len(building)):
        worksheet.write(i,0,building[i])
    for i in range(0, len(buildingid)):
        worksheet.write(i, 1, buildingid[i])
    workbook.save("山大电力.xls")
    print("表格已生成")
    #开启电费查询模块
    print("电费查询系统已启动")
    #id与楼栋对照字典
    building_id={"凤凰居6号":"1503975980","B5号楼":"1661835273","B2":"1661835256","T1":"1574231830","凤凰居1号楼":"1503975832","S1一多书院":"1503975832","S11":"1599193777","B9":"1693031698","凤凰居9号楼":"1503976004","凤凰居2号楼":"1503975890","S5凤凰居5号楼":"1503975967","凤凰居10号楼":"1503976037","S2从文书院":"1503975890","阅海居B10楼":"1693031710","阅海居B9楼":"1693031698","T3":"1574231835","S9凤凰居9号楼":"1503976004","S7凤凰居7号楼":"1503975988","S10凤凰居10号楼":"1503976037","S8凤凰居8号楼":"1503975995","凤凰居11/13号楼":"1599193777","专家公寓2号楼":"1574231833","凤凰居3号楼":"1503975902","B10":"1693031710","B1":"1661835249","凤凰居4号楼":"1503975950","S6凤凰居6号楼":"1503975980"}
    print("凤凰居6号，B5号楼，B2，T1，凤凰居1号楼，S1一多书院，S11,B9,凤凰居9号楼,凤凰居2号楼,S5凤凰居5号楼,凤凰居10号楼,S2从文书院,阅海居B10楼,阅海居B9楼,T3,S9凤凰居9号楼,S7凤凰居7号楼,S10凤凰居10号楼,S8凤凰居8号楼,凤凰居11/13号楼,专家公寓2号楼,凤凰居3号楼,B10,B1,凤凰居4号楼,S6凤凰居6号楼")
    building=str(input("请输入你的楼栋："))
    room=str(input("请输入房间号:"))
    #可变data
    json_data = {"query_elec_roominfo": {"retcode": "0", "errmsg": "房间当前剩余电量358.01", "aid": "0030000000002505",
                                         "account": "823872", "meterflag": "amt", "bal": "", "price": "0",
                                         "pkgflag": "none", "area": {"area": "青岛校区", "areaname": "青岛校区"},
                                         "building": {"buildingid": building_id[building], "building": ""},
                                         "floor": {"floorid": "", "floor": ""},
                                         "room": {"roomid": room, "room": room}, "pkgtab": []}}
    #解码并发送请求
    data1 = f"jsondata={urllib.parse.quote(json.dumps(json_data, ensure_ascii=False))}&funname=synjones.onecard.query.elec.roominfo&json=true"
    request1 = urllib.request.Request(url=url, headers=headers, data=data1.encode("utf-8"), method='POST')
    response1 = urllib.request.urlopen(request1, timeout=6000)
    html1 = response1.read().decode("utf-8")
    a1 = re.compile(r'"errmsg":"房间当前剩余电量(.*?)",')#正则提取
    elc = re.findall(a1, html1)
    print(elc[0])
    #询问用户预期最低电量
    dick=float(input("你希望电量不低于多少："))
    print(''' 
              模式1:按每？分钟执行一次爬取
              模式2：按每？小时执行一次爬取
              模式3：按每天的？点？分执行一次爬取
              模式4：每？小时运行，？点后停止
              ''')
    cock = int(input("是否需要邮箱提醒（是请输入1，否则输入2）："))
    if cock == 1:
        mail = str(input("请输入您的邮箱："))
        ass = 1
    #定时系统
    moudule = input("请输入你需要模式几")
    if moudule == "1":
        schedule.every(float(input("请输入分钟数"))).minutes.do(job)
    if moudule == "2":
        schedule.every(float(input("请输入小时数"))).hour.do(job)
    if moudule == "3":
        schedule.every().day.at("11:25").do(job)
    if moudule == "4":
        schedule.every(float(input("请输入小时数"))).hours.until(
            "input('请输入：小时：分钟，如13：15代表13点15分，需要输入冒号')").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
else:
    #开启电费查询模块
    print("电费查询系统已启动")
    #id与楼栋对照字典
    building_id={"凤凰居6号":"1503975980","B5号楼":"1661835273","B2":"1661835256","T1":"1574231830","凤凰居1号楼":"1503975832","S1一多书院":"1503975832","S11":"1599193777","B9":"1693031698","凤凰居9号楼":"1503976004","凤凰居2号楼":"1503975890","S5凤凰居5号楼":"1503975967","凤凰居10号楼":"1503976037","S2从文书院":"1503975890","阅海居B10楼":"1693031710","阅海居B9楼":"1693031698","T3":"1574231835","S9凤凰居9号楼":"1503976004","S7凤凰居7号楼":"1503975988","S10凤凰居10号楼":"1503976037","S8凤凰居8号楼":"1503975995","凤凰居11/13号楼":"1599193777","专家公寓2号楼":"1574231833","凤凰居3号楼":"1503975902","B10":"1693031710","B1":"1661835249","凤凰居4号楼":"1503975950","S6凤凰居6号楼":"1503975980"}
    print("凤凰居6号，B5号楼，B2，T1，凤凰居1号楼，S1一多书院，S11,B9,凤凰居9号楼,凤凰居2号楼,S5凤凰居5号楼,凤凰居10号楼,S2从文书院,阅海居B10楼,阅海居B9楼,T3,S9凤凰居9号楼,S7凤凰居7号楼,S10凤凰居10号楼,S8凤凰居8号楼,凤凰居11/13号楼,专家公寓2号楼,凤凰居3号楼,B10,B1,凤凰居4号楼,S6凤凰居6号楼")
    building=str(input("请输入你的楼栋："))
    room=str(input("请输入房间号:"))
    #可变data
    json_data = {"query_elec_roominfo": {"retcode": "0", "errmsg": "房间当前剩余电量358.01", "aid": "0030000000002505",
                                         "account": "823872", "meterflag": "amt", "bal": "", "price": "0",
                                         "pkgflag": "none", "area": {"area": "青岛校区", "areaname": "青岛校区"},
                                         "building": {"buildingid": building_id[building], "building": ""},
                                         "floor": {"floorid": "", "floor": ""},
                                         "room": {"roomid": room, "room": room}, "pkgtab": []}}
    #解码并发送请求
    data1 = f"jsondata={urllib.parse.quote(json.dumps(json_data, ensure_ascii=False))}&funname=synjones.onecard.query.elec.roominfo&json=true"
    request1 = urllib.request.Request(url=url, headers=headers, data=data1.encode("utf-8"), method='POST')
    response1 = urllib.request.urlopen(request1, timeout=6000)
    html1 = response1.read().decode("utf-8")
    a1 = re.compile(r'"errmsg":"房间当前剩余电量(.*?)",')#正则提取
    elc = re.findall(a1, html1)
    print(elc[0])
    #询问用户预期最低电量
    dick=float(input("你希望电量不低于多少："))
    print(''' 
              模式1:按每？分钟执行一次爬取
              模式2：按每？小时执行一次爬取
              模式3：按每天的？点？分执行一次爬取
              模式4：每？小时运行，？点后停止
              ''')
    cock = int(input("是否需要邮箱提醒（是请输入1，否则输入2）："))
    if cock == 1:
        mail = str(input("请输入您的邮箱："))
        ass = 1
    #定时系统
    moudule = input("请输入你需要模式几")
    if moudule == "1":
        schedule.every(float(input("请输入分钟数"))).minutes.do(job)
    if moudule == "2":
        schedule.every(float(input("请输入小时数"))).hour.do(job)
    if moudule == "3":
        schedule.every().day.at("11:25").do(job)
    if moudule == "4":
        schedule.every(float(input("请输入小时数"))).hours.until(
            "input('请输入：小时：分钟，如13：15代表13点15分，需要输入冒号')").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)