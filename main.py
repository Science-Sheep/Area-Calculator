#声明
print("声明")
print("作者:科学羊")
print(" 版本:1.0")
#获取图形
PICTAUE = input("请输入图形")
if PICTAUE == "长方形":
    #获取数据类型
    CLASS_AND_CLASS = input("请输入数据类型")
    if CLASS_AND_CLASS == "小数":
        #获取长
        LONG = float(input("请输入长"))
        #获取宽
        FAT = float(input("请输入宽"))
        #计算 
        YES = LONG * FAT
        #输出
        print(YES)    
    elif CLASS_AND_CLASS == "整数":
        #获取长
        LONG = int(input("请输入长"))
        #获取宽
        FAT = int(input("请输入宽"))
        #计算
        YES = LONG * FAT
        #输出
        print(YES)
    else:
        print("您输入的输据类型我们不支持")
        print("请重新输入")
        bool = False
        while bool == False:
            #获取数据类型
            CLASS_AND_CLASS = input("请输入数据类型")
            if CLASS_AND_CLASS == "整数":
                break
            elif CLASS_AND_CLASS == "小数":
                break
        if CLASS_AND_CLASS == "小数":
            #获取长
            LONG = float(input("请输入长"))
            #获取宽
            FAT = float(input("请输入宽"))
            #计算
            YES = LONG * FAT
            #输出
            print(YES)
        elif CLASS_AND_CLASS == "整数":
            #获取长
            LONG = int(input("请输入长"))
            #获取宽
            FAT = int(input("请输入宽"))
            #计算
            YES = LONG * FAT
            #输出
            print(YES)
elif PICTAUE == "正方形":
    #获取数据类型
    CLASS_AND_CLASS = input("请输入数据类型")
    if CLASS_AND_CLASS == "小数":
        #获取边长
        LONG = float(input("请输入边长"))
        #计算
        YES = LONG * LONG
        #输出
        print(YES)
    elif CLASS_AND_CLASS == "整数":
        #获取边长
        LONG = int(input("请输入边长"))
        #计算
        YES = LONG * LONG
        #输出
        print(YES)
    else:
        print("您输入的输据类型我们不支持")
        print("请重新输入")
        bool = False
        while bool == False:
            #获取数据类型
            CLASS_AND_CLASS = input("请输入数据类型")
            if CLASS_AND_CLASS == "整数":
                break
            elif CLASS_AND_CLASS == "小数":
                break
        if CLASS_AND_CLASS == "小数":
            #获取边长
            LONG = float(input("请输入边长"))
            #计算
            YES = LONG * LONG
            #输出
            print(YES)
        elif CLASS_AND_CLASS == "整数":
            #获取边长
            LONG = int(input("请输入边长"))
            #计算
            YES = LONG * LONG
            #输出
            print(YES)
#退出
input("点击关闭按钮或按Enter来退出")