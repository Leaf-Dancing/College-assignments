import re
name=input("请输入您的姓名:")
id=input("请输入您的身份证号码:")
riqi=input("请输入当前日期,例如:2024.3.13:")
riqi2=list(map(int,re.split(r"[.,;、`· ]",riqi)))
b1={"11":"北京市","12":"天津市","13":"河北省","14":"山西省","15":"内蒙古自治区","21":"辽宁省","22":"吉林省","23":"黑龙江省","31":"上海市","32":"江苏省","33":"浙江省","34":"安徽省","35":"福建省","36":"江西省","37":"山东省","41":"河南省","42":"湖北省","43":"湖南省","44":"广东省","45":"广西壮族自治区","46":"海南省","50":"重庆市","51":"四川省","52":"贵州省","53":"云南省","54":"西藏自治区","61":"陕西省","62":"甘肃省","63":"青海省","64":"宁夏回族自治区","65":"新疆维吾尔自治区","81":"香港","82":"澳门","83":"台湾"}
b2={0:1,1:0,2:"X",3:9,4:8,5:7,6:6,7:5,8:4,9:3,10:2}
id2=re.match(r"(?P<地址>\d{6})(?P<年>\d{4})(?P<月>\d{2})(?P<日>\d{2})(?P<顺>\d{3})(?P<校>\S{1})",id)
yue=int(id2.group("月"))
ri=int(id2.group("日"))
if int(id2.group("顺")[-1])%2==0:
    gender="女士"
else:
    gender="先生"
nian=[31,28,31,30,31,30,31,30,31,30,31,30]
nian2=[31,28,31,30,31,30,31,30,31,30,31,30]
if ((riqi2[0])%4==0 and riqi2[0]%100!=0) or riqi2[0]%400==0:
    nian[1]=29
if ((riqi2[0])%4==1 and riqi2[0]%100!=1) or riqi2[0]%400==1:
    nian2[1]=29
days=nian[riqi2[1]-1]-riqi2[2]+ri
if riqi2[1]>yue:
    for i in range(int(riqi2[1]),12):
        days+=nian[i]
    for i in range(0,yue-1):
        days+=nian2[i]
elif riqi2[1]<yue:
    for i in range(int(riqi2[1]),yue-1):
        days+=nian[i]
else:
    days=ri-riqi2[2]-1
a=list(map(int,id[:]))
w=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2,1]
num=0
for i in range(17): 
    num+=a[i]*w[i]
if id2.group("校")==str(b2.get(num%11)):
    if int(riqi2[1])!=yue and int(riqi2[2]!=ri):
        print("校验码正确\n","来自",b1.get((id2.group("地址"))[:2]),"的",name+gender,"您今年",2024-int(id2.group("年")),"岁了,距离您的生日",id2.group("月"),"月",id2.group("日"),"日还有",days,"天.")
    else:
        print("校验码正确\n","来自",b1.get((id2.group("地址"))[:2]),"的",name+gender,"您今年",2024-int(id2.group("年")),"岁了,祝您生日快乐!")
else:
    print("校验码错误,请检查输入")