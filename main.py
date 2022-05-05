from PyQt5 import QtCore,QtGui,QtWidgets
from lxml import etree
from UI import Ui_Form
import sys,time,os,requests,json,mainLib,plyer



def killprograme():
    ui.close()
    # ui.deleteLater()
    os.system("taskkill /pid {} /f".format(os.getpid()))
    # sys.exit()

tree=etree.HTML(requests.get('https://www.qweather.com/weather30d/changsha-county-101250106.html').text)
mainTemperature=mainLib.getMainTemperature(tree)



tree=etree.HTML(requests.get('https://www.qweather.com/indices/changsha-county-101250106.html').text)
comfortDic=mainLib.getcanshu(tree,"indices-detail__forecast--bg jsIndicesDetail jsIndicesDetailComfort active","comfort")


dressDic=mainLib.getcanshu(tree,"indices-detail__forecast--bg jsIndicesDetail jsIndicesDetailDress","dress")


UvDic=mainLib.getcanshu(tree,"indices-detail__forecast--bg jsIndicesDetail jsIndicesDetailUv","Uv")


weizhiList=[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6]]
todaytime=time.strftime('%m月%d日'.encode('unicode_escape').decode('utf8'),time.localtime()).encode('utf-8').decode('unicode_escape')

if not os.path.exists('./pic'):
    os.mkdir('./pic')

if '-noGUI' in sys.argv:
    with open('weather.json', 'w', encoding='utf-8') as f:
        json.dump(mainTemperature, f, indent=4)
    with open('comfort.json', 'w', encoding='utf-8') as f:
        json.dump(comfortDic, f, indent=4)
    with open('dress.json', 'w', encoding='utf-8') as f:
        json.dump(dressDic, f, indent=4)
    with open('Uv.json', 'w', encoding='utf-8') as f:
        json.dump(UvDic, f, indent=4)
    # mainWord="{}\nComfort:{}\n{}.\nDress:{}\n{}.\nUv:{}\n{}.".format(mainTemperature['mainWord'],comfortDic[0]['comfort'][0],comfortDic[0]['comfort'][1],dressDic[0]['dress'][0],dressDic[0]['dress'][1],UvDic[0]['Uv'][0],UvDic[0]['Uv'][1])
    mainWord=mainTemperature['mainWord']
    plyer.notification.notify(title="天气", message=mainWord, app_name='通知',app_icon='100.ico', timeout=6000)
    time.sleep(2)
    # toast.show_toast("天气", mainWord, '100.ico', 6000, True)
    mainWord = "Comfort:{}\n{}".format(comfortDic[0]['comfort'][0],comfortDic[0]['comfort'][1])
    # plyer.notification.notify(title="天气", message=mainWord, app_name='通知',app_icon='100.ico', timeout=6000)
    # mainWord = "Comfort:{}\n{}.".format(comfortDic[0]['comfort'][0],comfortDic[0]['comfort'][1])
    plyer.notification.notify(title="天气", message=mainWord, app_name='通知',app_icon='100.ico', timeout=6000)
    time.sleep(2)
    # mainWord="{}\nComfort:{}\n{}.\n".format(mainTemperature['mainWord'],comfortDic[0]['comfort'][0],comfortDic[0]['comfort'][1])
    if '清凉夏季服装'in dressDic[0]['dress'][1]:
        mainWord="Dress:{}\n{}".format("清凉夏季服装",dressDic[0]['dress'][1])
    elif '等夏季服装' in dressDic[0]['dress'][1]:
        mainWord="Dress:{}\n{}".format("短袖",dressDic[0]['dress'][1])
    elif '长袖' in dressDic[0]['dress'][1]:
        mainWord="Dress:{}\n{}".format("长袖",dressDic[0]['dress'][1])
    elif '羽绒服' in dressDic[0]['dress'][1]:
        mainWord="Dress:{}\n{}".format("羽绒服",dressDic[0]['dress'][1])
    elif '毛衣' in dressDic[0]['dress'][1]:
        mainWord="Dress:{}\n{}".format("毛衣",dressDic[0]['dress'][1])
    else:
        mainWord=mainWord+"Dress:{}\n{}".format(dressDic[0]['dress'][0],dressDic[0]['dress'][1])
    plyer.notification.notify(title="天气", message=mainWord, app_name='通知', app_icon='100.ico', timeout=6000)
    time.sleep(2)
    mainWord="Uv:{}\n{}".format(UvDic[0]['Uv'][0],UvDic[0]['Uv'][1])
    plyer.notification.notify(title="天气", message=mainWord, app_name='通知', app_icon='100.ico', timeout=6000)
    # os.system("taskkill /pid {} /f".format(os.getpid()))
    sys.exit()

app=QtWidgets.QApplication(sys.argv)
QtGui.QFontDatabase.addApplicationFont("./MI_LanTing_Regular.ttf")
ui=Ui_Form()
ui.pushButton_4.clicked.connect(killprograme)
plyer.notification.notify(title="天气", message=mainTemperature['mainWord'], app_name='通知',app_icon='100.ico', timeout=6000)
#toast.show_toast("天气",mainTemperature['mainWord'],'100.ico',600,True)
ui.label.setText(mainTemperature['mainWord'])
for item in mainTemperature['outList']:
    if not os.path.exists('./pic/{}'.format(mainLib.getPicName(item['picUrl']))):
        try:
            pic=requests.get(item['picUrl'],timeout=10).content
            with open('./pic/{}'.format(mainLib.getPicName(item['picUrl'])),'wb') as f:
                f.write(pic)
                time.sleep(1)
        except:
            try:
                pic = requests.get(item['picUrl'], timeout=10).content
                with open('./pic/{}'.format(mainLib.getPicName(item['picUrl'])), 'wb') as f:
                    f.write(pic)
                    time.sleep(1)
            except:
                try:
                    pic = requests.get(item['picUrl'], timeout=10).content
                    with open('./pic/{}'.format(mainLib.getPicName(item['picUrl'])), 'wb') as f:
                        f.write(pic)
                        time.sleep(1)
                except:
                    try:
                        pic = requests.get(item['picUrl'], timeout=10).content
                        with open('./pic/{}'.format(mainLib.getPicName(item['picUrl'])), 'wb') as f:
                            f.write(pic)
                            time.sleep(1)
                    except:
                        pass
    cishu=mainTemperature['outList'].index(item)
    t=time.localtime().tm_wday
    weizhi=weizhiList[cishu+t]
    i=QtWidgets.QTableWidgetItem()
    i.setIcon(QtGui.QIcon('./pic/{}'.format(mainLib.getPicName(item['picUrl']))))
    if cishu<4:
        # print(cishu)
        i.setText(item['temperature']+'\n'+comfortDic[cishu]['comfort'][0]+' '+dressDic[cishu]['dress'][0]+' '+UvDic[cishu]['Uv'][0])
        i.setToolTip(comfortDic[cishu]['date']+'\n'+comfortDic[cishu]['comfort'][1]+'\n'+dressDic[cishu]['dress'][1]+'\n'+UvDic[cishu]['Uv'][1])
        i.setFont(QtGui.QFont('小米兰亭'))
    else:
        i.setText(item['temperature'])
        i.setFont(QtGui.QFont('小米兰亭'))
        i.setToolTip(mainTemperature["outList"][cishu]['day'])
    ui.tableWidget.setItem(weizhi[0],weizhi[1],i)
ui.tableWidget.update()
ui.show()
app.exec_()
# print('finish')
