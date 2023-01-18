#https://96lovefootball.hatenablog.com/entry/2019/01/06/210000
#https://smart-hint.com/python/graph-label/#%E5%87%A1%E4%BE%8B%EF%BC%9Alegend
import pandas as pd
import matplotlib.pyplot as plt

path = r"C:\Users\norir\Desktop\ReiFujimura_study\中間発表会\FWHM_作図用.csv"
df = pd.read_csv(path,header=0)
#print(df)
fig = plt.figure(figsize=[15,7])
processed = df["FWHM_processed"]
before = df["FWHM_before"]
xaxis = df["number"]
lb = df["lb"]

plt.subplot(121) #1行×2列の配置の内、1番目
plt.title("processed vs before") #タイトル
plt.xlabel("sample number") #x軸ラベル
plt.ylabel("FWHM (Hz)") #y軸ラベル
plt.plot(xaxis[:143],processed[:143],label="processed",color="red",linestyle="-",marker="o",markersize=1)
plt.plot(xaxis[:143],before[:143],label="before",color="tomato",linestyle="-",marker="o",markersize=1)
plt.legend() #凡例
plt.grid(axis="y") #補助線

plt.subplot(122)#1行×2列の配置の内、2番目
plt.title("lb for apodization") #タイトル
plt.xlabel("sample number") #x軸ラベル
plt.ylabel("lb") #y軸ラベル
plt.plot(xaxis[:143],lb[:143],label="lb",color="blue",linestyle="-",marker="o",markersize=1)
plt.grid(axis="y") #補助線
plt.show()