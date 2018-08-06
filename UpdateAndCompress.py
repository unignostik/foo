import os
import zipfile

#create current year folder for each record and populate with folders for each month
for item in os.listdir("/Users/ct/Desktop/CPU"):
    if os.path.exists("/Users/ct/Desktop/CPU/"+item+"/2018"):
       print("Exists!")
    else:
       os.makedirs("/Users/ct/Desktop/CPU/"+item+"/2018")
       os.makedirs("/Users/ct/Desktop/CPU/"+item+"/2018/January")
       os.makedirs("/Users/ct/Desktop/CPU/"+item+"/2018/February")
       os.makedirs("/Users/ct/Desktop/CPU/"+item+"/2018/March")
       os.makedirs("/Users/ct/Desktop/CPU/"+item+"/2018/April")
       os.makedirs("/Users/ct/Desktop/CPU/"+item+"/2018/May")
       os.makedirs("/Users/ct/Desktop/CPU/"+item+"/2018/June")
       os.makedirs("/Users/ct/Desktop/CPU/"+item+"/2018/July")
       os.makedirs("/Users/ct/Desktop/CPU/"+item+"/2018/August")
       os.makedirs("/Users/ct/Desktop/CPU/"+item+"/2018/September")
       os.makedirs("/Users/ct/Desktop/CPU/"+item+"/2018/October")
       os.makedirs("/Users/ct/Desktop/CPU/"+item+"/2018/November")
       os.makedirs("/Users/ct/Desktop/CPU/"+item+"/2018/December")

    #inside the record, determine month of html file and move to corresponding folder
    for subItem in os.listdir("/Users/ct/Desktop/CPU/"+item):
        if ".txt" in subItem:
            if "1801" in subItem:
                os.rename("/Users/ct/Desktop/CPU/"+item+"/"+subItem,"/Users/ct/Desktop/CPU/"+item+"/2018/January/"+subItem)
            if "1802" in subItem:
                os.rename("/Users/ct/Desktop/CPU/"+item+"/"+subItem,"/Users/ct/Desktop/CPU/"+item+"/2018/February/"+subItem)
            if "1803" in subItem:
                os.rename("/Users/ct/Desktop/CPU/"+item+"/"+subItem,"/Users/ct/Desktop/CPU/"+item+"/2018/March/"+subItem)
            if "1804" in subItem:
                os.rename("/Users/ct/Desktop/CPU/"+item+"/"+subItem,"/Users/ct/Desktop/CPU/"+item+"/2018/April/"+subItem)
            if "1805" in subItem:
                os.rename("/Users/ct/Desktop/CPU/"+item+"/"+subItem,"/Users/ct/Desktop/CPU/"+item+"/2018/May/"+subItem)
            if "1806" in subItem:
                os.rename("/Users/ct/Desktop/CPU/"+item+"/"+subItem,"/Users/ct/Desktop/CPU/"+item+"/2018/June/"+subItem)
            if "1807" in subItem:
                os.rename("/Users/ct/Desktop/CPU/"+item+"/"+subItem,"/Users/ct/Desktop/CPU/"+item+"/2018/July/"+subItem)
            if "1808" in subItem:
                os.rename("/Users/ct/Desktop/CPU/"+item+"/"+subItem,"/Users/ct/Desktop/CPU/"+item+"/2018/August/"+subItem)
            if "1809" in subItem:
                os.rename("/Users/ct/Desktop/CPU/"+item+"/"+subItem,"/Users/ct/Desktop/CPU/"+item+"/2018/September/"+subItem)
            if "1810" in subItem:
                os.rename("/Users/ct/Desktop/CPU/"+item+"/"+subItem,"/Users/ct/Desktop/CPU/"+item+"/2018/October/"+subItem)
            if "1811" in subItem:
                os.rename("/Users/ct/Desktop/CPU/"+item+"/"+subItem,"/Users/ct/Desktop/CPU/"+item+"/2018/November/"+subItem)
            if "1812" in subItem:
                os.rename("/Users/ct/Desktop/CPU/"+item+"/"+subItem,"/Users/ct/Desktop/CPU/"+item+"/2018/December/"+subItem)
