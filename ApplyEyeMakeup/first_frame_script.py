import os
import subprocess

sourcedir = "D:\Keras\ApplyEyeMakeup"

png_count = 0

for file in os.listdir(sourcedir):
	name = file[:file.rfind(".")]
	png_count_st = str(png_count)
	subprocess.call('ffmpeg -i '+name+'.avi '+'-ss 00:00:0.435 -vframes 1 out'+png_count_st+'.png', 
		shell="True")
	png_count += 1
 
