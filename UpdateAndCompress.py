import os
import zipfile

#create current year folder for each record and populate with folders for each month
for folder in os.listdir("/Users/ct/Desktop/CPU"):
    if os.path.exists("/Users/ct/Desktop/CPU/"+folder+"/2018"):
       print("Exists!")
    else:
       os.makedirs("/Users/ct/Desktop/CPU/"+folder+"/2018")
       os.makedirs("/Users/ct/Desktop/CPU/"+folder+"/2018/January")
       os.makedirs("/Users/ct/Desktop/CPU/"+folder+"/2018/February")
       os.makedirs("/Users/ct/Desktop/CPU/"+folder+"/2018/March")
       os.makedirs("/Users/ct/Desktop/CPU/"+folder+"/2018/April")
       os.makedirs("/Users/ct/Desktop/CPU/"+folder+"/2018/May")
       os.makedirs("/Users/ct/Desktop/CPU/"+folder+"/2018/June")
       os.makedirs("/Users/ct/Desktop/CPU/"+folder+"/2018/July")
       os.makedirs("/Users/ct/Desktop/CPU/"+folder+"/2018/August")
       os.makedirs("/Users/ct/Desktop/CPU/"+folder+"/2018/September")
       os.makedirs("/Users/ct/Desktop/CPU/"+folder+"/2018/October")
       os.makedirs("/Users/ct/Desktop/CPU/"+folder+"/2018/November")
       os.makedirs("/Users/ct/Desktop/CPU/"+folder+"/2018/December")

#determine month of file and move to corresponding folder
try:
    for root, dirs, files in os.walk("/Users/ct/Desktop/CPU"):
        for fileName in files:
            if ".txt" in fileName: #only grab .txt files
                if "1801" in fileName:
                    filePath = os.path.join(root, fileName)
                    os.rename(filePath, root+"/2018/January/"+fileName)
                if "1802" in fileName:
                    filePath = os.path.join(root, fileName)
                    os.rename(filePath, root+"/2018/February/"+fileName)
                if "1803" in fileName:
                    filePath = os.path.join(root, fileName)
                    os.rename(filePath, root+"/2018/March/"+fileName)
                if "1804" in fileName:
                    filePath = os.path.join(root, fileName)
                    os.rename(filePath, root+"/2018/April/"+fileName)
                if "1805" in fileName:
                    filePath = os.path.join(root, fileName)
                    os.rename(filePath, root+"/2018/May/"+fileName)
                if "1806" in fileName:
                    filePath = os.path.join(root, fileName)
                    os.rename(filePath, root+"/2018/June/"+fileName)
                if "1807" in fileName:
                    filePath = os.path.join(root, fileName)
                    os.rename(filePath, root+"/2018/July/"+fileName)
                if "1808" in fileName:
                    filePath = os.path.join(root, fileName)
                    os.rename(filePath, root+"/2018/August/"+fileName)
                if "1809" in fileName:
                    filePath = os.path.join(root, fileName)
                    os.rename(filePath, root+"/2018/September/"+fileName)
                if "1810" in fileName:
                    filePath = os.path.join(root, fileName)
                    os.rename(filePath, root+"/2018/October/"+fileName)
                if "1811" in fileName:
                    filePath = os.path.join(root, fileName)
                    os.rename(filePath, root+"/2018/November/"+fileName)
                if "1812" in fileName:
                    filePath = os.path.join(root, fileName)
                    os.rename(filePath, root+"/2018/December/"+fileName)

#compress generated directories, files
except IOError:
    for folder in os.listdir("/Users/ct/Desktop/CPU"):
    for monthFolder in os.listdir(folder+"/2018"):
        zipfile.ZipFile(monthFolder+".zip", 'w').write(monthFolder)
