import librosa
import librosa.display
import matplotlib.pyplot as plt
filename = 'C:/Users/jing/Desktop/语音比赛/waveform.wav'
y, sr = librosa.load(filename)
# trim silent edges  减去静音片段
whale_song, _ = librosa.effects.trim(y)
librosa.display.waveplot(whale_song, sr=sr);
plt.show();
