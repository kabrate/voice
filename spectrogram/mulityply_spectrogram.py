
import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display  
import os
filepath = 'E:\\data\\poco1\\'
for root, dirs, files in os.walk(filepath):   #遍历所给地址的所有文件夹和文件 root是路径 dirs路径中的子文件夹 files是路径中文件
    #print(root) #当前目录路径  
    #print(dirs) #当前路径下所有子目录  
    #print(files) #当前路径下所有非目录子文件
    if dirs:
        break
len_dirs=len(dirs)
for j in range(0,len_dirs):
    for root1, dirs1, files1 in os.walk(filepath+dirs[j]):   #遍历所给地址的所有文件夹 root是路径 dirs路径中的子文件夹 files是路径中文件
        pass
    for i in range(0,len(files1)): #文件夹中的文件
        filename = filepath+dirs[j]+'/'+files1[i]
        # 1. Get the file path to the included audio example
        # 2. Load the audio as a waveform `y`
        #    Store the sampling rate as `sr`
        y, sr = librosa.load(filename,sr=None)
        # trim silent edges  减去静音片段
        #y, _ = librosa.effects.trim(y)
        win_length = int(0.025 * sr)  # Window length 15ms, 25ms, 50ms, 100ms, 200ms 音频帧长度
        hop_length = int(0.010 * sr)  # Window shift  10ms 音频帧间隔
        n_fft = 512 #快速傅里叶变换的维度 音频帧中信号不足 补零处理
        #调整大小
        plt.figure(figsize=(12, 6))
        #振幅转化为分贝
        D = librosa.amplitude_to_db(librosa.stft(y,hop_length=hop_length,win_length=win_length), ref=np.max)
        #标签
        librosa.display.specshow(D,sr=sr, hop_length =hop_length,x_axis='time', y_axis='linear')
        #分贝颜色
        #plt.colorbar(format='%+2.0f dB')
        string1=files1[i]
        string1=string1.replace('.WAV','')
        plt.axis('off')  #去掉坐标轴
        #plt.show()
        plt.savefig('E:/data/spec/'+dirs[j]+'//'+string1 +'.png')
        plt.close()
    print(dirs[j]+'finished!')

