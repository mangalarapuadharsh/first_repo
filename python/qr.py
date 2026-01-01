import qrcode
url =input("enter url: ")
file="C:\\Users\\rider\\Downloads\\qrcode.png"
img = qrcode.make(url)
img.save(file)
print("qr generator successfully created at "+file)
a=int(input("enter 1 to open the file:"))
# print("helolo wolrd")
print("this is a test message")

if a==1:
    import os
    os.startfile(file)
    # print("press any key to exit")
    os.system("pause")
    os._exit(0)


else:
    print("ok bye")


    