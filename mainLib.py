from PyQt5 import QtCore

def getcanshu(tree_wangye,className,name):
    outList=[]
    Datas=tree_wangye.xpath(f'//div[@class="{className}"]/div/div')
    for data in Datas:
        date=data.xpath('./div[1]/div/p[2]/text()')
        Main=data.xpath('./div[2]/p[1]/text()')
        Tip=data.xpath('./div[2]/p[2]/text()')
        if len(date)>0 and len(Main)>0 and len(Tip)>0:
            todaydic={'date':date[0],name:[Main[0],Tip[0]]}
            outList.append(todaydic)
    return outList
def getMainTemperature(tree_wangye):
    import time
    mainWord=tree_wangye.xpath('//p[@class="weather30d-calendar__abstract text-center"]/text()')[0]
    dates=tree_wangye.xpath('//div[@class="calendar__date--bg"]')
    month=str(time.localtime().tm_mon)
    outList=[]
    for date in dates:
        day=date.xpath('./a/div/span/text()')
        temperature=date.xpath('./a/p/text()')
        picUrl=date.xpath('./a/div/img/@src')
        if len(day)>0 and len(temperature)>0 and len(picUrl)>0:
            todaydic={"day":month+'-'+day[0],"temperature":temperature[0].replace(' ','').replace('\n',''),'picUrl':picUrl[0]}
            if "月"in day[0]:
                month=day[0][0]
                todaydic={"day":month+'-'+"1","temperature":temperature[0].replace(' ','').replace('\n',''),'picUrl':picUrl[0]}
            outList.append(todaydic)
    outdic={'mainWord':mainWord,'outList':outList}
    return outdic
getPicName=lambda zi:zi[zi.rfind('/')+1:]



if __name__=="__main__":
    from lxml import etree
    import requests,time
    tree=etree.HTML(requests.get('https://www.qweather.com/indices/changsha-county-101250106.html').text)
    print(getcanshu(tree,"indices-detail__forecast--bg jsIndicesDetail jsIndicesDetailUv",'UV'))