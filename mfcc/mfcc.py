import librosa
from matplotlib import pyplot 
waveform, sample_rate=librosa.core.load("C:/Users/jing/Desktop/语音比赛/LA_T_5250203.wav",sr=None)
features =librosa.feature.mfcc(waveform,sr=sample_rate,n_mfcc=40,hop_length=sample_rate//100,
                               win_length=sample_rate//40,n_fft=512,fmin=100,fmax=16000 )
# mfcc特征数 音频帧间隔 音频帧长度 快速傅里叶变换维度 fmin fmax最小和最大频率 
#二维矩阵 mfcc特征数 音频帧总帧数 
#
pyplot.matshow(features, origin="lower")
pyplot.savefig('mfcc.png')
