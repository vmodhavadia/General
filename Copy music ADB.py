import os
import shutil

files = os.listdir('C:\\Users\\Vikram\\Documents')

for filename in files:
    if filename[len(filename) - 3: len(filename)] == 'mp3':
        src = 'C:\\Users\\Vikram\\Documents\\' + filename
        dst = 'C:\\Users\\Vikram\\Documents\\MUSIC KEEP UPDATING'
        mystr = 'cd C:\\Users\\Vikram\\Documents\\platform-tools && adb push C:\\Users\\Vikram\\Documents\\' + filename + ' sdcard/Music'  
        shutil.copy2(src, dst)
        os.system(mystr)
        os.remove(src)
os.system('pause')

