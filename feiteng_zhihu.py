import datetime
'''飞腾八法,是以奇经八脉和八脉交会穴为基础,以八卦统八穴,以时干为八穴的代号和开穴的依据,属于道家时间针法的一种。'''


TIAN_GAN = u"甲,乙,丙,丁,戊,己,庚,辛,壬,癸".split(",")

FEITENG_SHIGAN_KAIXUE_DICT={
'甲':'公孙','乙':'申脉','丙':'内关','丁':'照海','戊':'足临泣',
'己':'列缺','庚':'外关','辛':'后溪','壬':'公孙','癸':'申脉'
}

NAJIA_GAN_BAGUA_DICT={
'甲':'乾', '乙':'坤', '丙':'艮', '丁':'兑','戊':'坎',
'己':'离', '庚':'震', '辛':'巽', '壬':'乾','癸':'坤'
}

BAMAIJIAOHUIXUE_BAMAI_DICT={
    '公孙':'冲脉','内关':'阴维脉','足临泣':'带脉','外关':'阳维脉',
    '后溪':'督脉','申脉':'阳跷脉','列缺':'任脉','照海':'阴跷脉'
}

XUEWEI_WEIZHI_DICT={'足临泣':'足临泣穴位于足背外侧，第四趾、小趾跖骨夹缝中，小趾伸肌腱的外侧凹陷处',
                    '外关':'外关穴位于前臂外侧腕横纹上2寸，尺骨与桡骨间隙中点。或内关穴对侧',
                    '申脉':'申脉穴位于外踝尖下1寸',
                    '后溪':'后溪穴位于第5指掌关节后尺侧的远侧掌横纹头赤白肉际',
                    '照海':'照海穴位于内踝尖下1寸',
                    '列缺':'列缺穴位于体前臂桡侧缘，桡骨茎突上方，腕横纹上1.5寸',
                    '公孙':'公孙穴位于第一跖骨基底下的前下缘赤白肉际处',
                    '内关':'内关穴位于前臂掌侧正中，腕横纹上2寸'


}

def getHourGanzhi(dt,num=False):
    #以1901年1月1日凌晨一点为基准点 此刻是乙丑时的开始
    startDT=datetime.datetime(year=1901, month=1, day=1, hour=1)
    #60干支乙丑是第二个，以0为起点，则编号为1
    startGanzhi=1
    if not isinstance(dt, datetime.datetime):
        return ""
    #计算离基准时刻过去了多少时间
    delta = dt - startDT
    if delta.seconds<0:
        return ""
    #计算时刻的干支编号
    flooor = int(delta.seconds/3600)
    hours = delta.days*24 + flooor
    aaa = int(hours /2)
    ganNum  = (startGanzhi + aaa)%10
    
    return (TIAN_GAN[ganNum] )



#yanshi(shi_gan)

def feitengfa(dt=datetime.datetime.now()):
    
    shi_gan=getHourGanzhi(dt)
    #shi_gan就是时柱的天干，时辰的天干

    kaixue=FEITENG_SHIGAN_KAIXUE_DICT[shi_gan]
    #kai_穴就是对应穴位名

    xue_weizhi=XUEWEI_WEIZHI_DICT[kaixue]
    #xue_weizhi就是穴位位置

    print('飞腾八法，时干开穴\n')
    print('当前时干:',shi_gan+'干','对应开穴:',kaixue+'穴')
    print('\n'+xue_weizhi)
    #return shi_gan,kaixue
    #本函数以print为主，可以自己定义return的值


#运行此文件将使用下方的feitengfa函数，自动print当时的时干和穴位名称
    
feitengfa()


