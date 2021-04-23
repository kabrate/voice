import librosa
import librosa.display
import matplotlib.pyplot as plt
filename = 'E:/data/poco1/0218_2-1-1/about.wav'
y, sr = librosa.load(filename)
# trim silent edges  减去静音片段
voice, _ = librosa.effects.trim(y)
librosa.display.waveplot(voice, sr=sr);
plt.show();
