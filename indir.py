import argparse,requests,re,urllib,os,shutil
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,help="Video Linki")
args = ap.parse_args()
qts = ["144","240","360","480","720","1080"]
sqt = []
tmp = re.findall("https:..cdnvideo.eba.gov.tr.v.+[a-zA-Z]",requests.get(args.video).text)[0][:-9]
print("Video Hangi Kalitede İnsin ?")
vhic = -1
for qt in qts:
    if requests.get(tmp + qt +"p_001.ts").status_code == 200:
        vhic += 1
        sqt.append(qt)
        print(qt + " İçin " + str(vhic) + " Yaz")
print("Ve Entera Bas")
kalnum = int(input())
print("Video İndiriliyor Bu İşlem Birazcık Sürebilir")
dqt = sqt[kalnum]
if(not os.path.exists("videotemp")):
    os.mkdir("videotemp")
else:
    shutil.rmtree("videotemp")
    os.mkdir("videotemp")
if(os.path.exists("yol.txt")):
    os.remove("yol.txt")
if(os.path.exists("video.mp4")):
    os.remove("video.mp4")
for blob in range(1,999999):
    if len(str(blob)) == 1:
        blob = "00" + str(blob)
    elif len(str(blob)) == 2:
        blob = "0" + str(blob)
    else:
        blob = str(blob)
    if requests.get(tmp + dqt +"p_" + blob + ".ts").status_code == 200:
        urllib.request.urlretrieve(tmp + dqt + "p_"+blob+".ts", 'videotemp/'+ blob +'.mp4')
        with open('yol.txt', 'a') as the_file:
            the_file.write("file '{yol}'\n".format(yol='videotemp/'+ blob +'.mp4'))
    else:
        os.system("ffmpeg -f concat -safe 0 -i yol.txt -c copy video.mp4")
        shutil.rmtree("videotemp")
        os.remove("yol.txt")
        print("İşlem Tamamlandı")
        os.system("video.mp4")
        break