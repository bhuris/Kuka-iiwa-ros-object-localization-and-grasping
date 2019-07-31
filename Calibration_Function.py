import math

def Calibration(Xcam,Ycam):
    if 281 > Ycam and Ycam >= 234:
        Yposi = 204-1.139*(469-Ycam)+math.log10(469-Ycam+1)*27
    elif Ycam >= 281:
        Yposi = 204-1.139*(469-Ycam)+math.log10(469-Ycam+1)*27-math.sin(Ycam-289)*10
    elif Ycam < 234:
        Yposi = 1.659*(Ycam-234)+math.sin((234-Ycam)*1.46)*15
    else:
        print("error Y-axis")
    if Xcam >= 323:
        Xposi = 609+0.602*(Xcam-323)+((469-Ycam)/9)
    elif Xcam < 323:
        Xposi = 609+0.602*(Xcam-323)-((469-Ycam)/9)
    else:
        print("error X-axis")
    return Xposi,Yposi


#print(Calibration(422,280))
#print(Calibration(386,130))