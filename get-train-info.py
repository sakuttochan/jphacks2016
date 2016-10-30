# coding: utf-8
import urllib2


#url = 'http://transit.yahoo.co.jp/search/result?flatlon=&from=小牛田&tlatlon=&to=石巻&via=&via=&via=&y=2016&m=10&d=30&hh=17&m1=0&m2=0&type=4&ticket=ic&al=1&shin=1&ex=1&hb=1&lb=1&sr=1&s=0&expkind=1&ws=2&kw=石巻'
#url = 'http://transit.yahoo.co.jp/search/result?flatlon=&from=杉田&tlatlon=&to=恵比寿&via=&via=&via=&y=2016&m=10&d=30&hh=17&m1=0&m2=0&type=4&ticket=ic&al=1&shin=1&ex=1&hb=1&lb=1&sr=1&s=0&expkind=1&ws=2&kw=恵比寿'
url = 'http://transit.yahoo.co.jp/search/result?flatlon=&from=水戸&tlatlon=&to=常陸大子&via=&via=&via=&y=2016&m=10&d=30&hh=17&m1=0&m2=0&type=4&ticket=ic&al=1&shin=1&ex=1&hb=1&lb=1&sr=1&s=0&expkind=1&ws=2&kw=常陸大子'
def getInfo(url):

    #lineName = raw_input()


    #運行情報ページのHTMLデータ取得して1行ずつリストに格納
    response = urllib2.urlopen(url)
    htmlData = response.read()
    railwayInfo = htmlData.split('\n')
    #正常ならtrue, 遅延ならfalseを返す関数
    #引数には路線名
    # 情報取得する路線名文字列が含まれているかチェック

    for i in range(0, len(railwayInfo)):
        pos = railwayInfo[i].find('routeDetail')
        if pos >= 0:
            n = 0
            while n < 300:
                n = n + 1
                pos = railwayInfo[i + n].find('icnAlert')
                if pos >= 0:
                    pos = railwayInfo[i+n+1].find('遅延')
                    if pos >= 0:
                        print 1
                        return 1
                        break
                    else:
                        pos = railwayInfo[i+n+1].find('運休')
                        if pos >= 0:
                            print 2
                            return 2
                            break
                        else:
                            # 平常運転、遅延でもなければ運休の可能性
                            print "平常"
                            return 0
                            break
                            #else:
                        #print "はい"

getInfo(url)
