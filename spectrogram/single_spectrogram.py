
import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display  
import os
filepath = 'E:/data/eval/a17'
for root, dirs, files in os.walk(filepath):   
    #print(root) #当前目录路径  
    #print(dirs) #当前路径下所有子目录  
    #print(files) #当前路径下所有非目录子文件
    pass
#length=len(files)
length=1
for i in range(0,length): 
    #filename = filepath+'//'+files[i]
    filename='E:\\data\\poco4\\wolf\\false/0203_2-2-1_wolf.WAV'
    # 1. Get the file path to the included audio example
    # 2. Load the audio as a waveform `y`
    #    Store the sampling rate as `sr`
    y, sr = librosa.load(filename,sr=None)
    duration = librosa.get_duration(filename=filename)#音频时间长度
    # trim silent edges  减去静音片段
    y, _ = librosa.effects.trim(y)
    win_length = int(0.025 * sr)  # Window length 15ms, 25ms, 50ms, 100ms, 200ms 音频帧长度
    hop_length = int(0.010 * sr)  # Window shift  10ms 音频帧间隔
    n_fft = 512 #快速傅里叶变换的维度 音频帧中信号不足 补零处理
    #调整大小

    plt.figure(figsize=(12, 6))
    #振幅转化为分贝
    D = librosa.amplitude_to_db(librosa.stft(y,n_fft=2205,hop_length=hop_length,win_length=win_length), ref=np.max)
    f=librosa.fft_frequencies(sr=sr,n_fft=2205)
    times = abs(librosa.frames_to_time(np.arange(0,D[0].size), sr=sr, hop_length=hop_length))# nftt*1/sr  length of the windowed signal
    D=D[0:10,:] #切片后一个数值取不到  表示f[0:10]频率内的stft
    #标签
    librosa.display.specshow(D,sr=sr, hop_length =hop_length,x_axis='time', y_axis='linear')
    #librosa.core.fft_frequencies(D,sr=sr, hop_length =hop_length,x_axis='time', y_axis='linear')
    #分贝颜色
    plt.colorbar(format='%+2.0f dB')
    #string1=files[i]
    #string1=string1.replace('.flac','')
    #plt.axis('off')  #去掉坐标轴
    plt.show()
    plt.savefig(filepath+'_fig/'+string1 +'.png')
    plt.close()

