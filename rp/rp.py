from pyrqa.time_series import TimeSeries
from pyrqa.settings import Settings
from pyrqa.analysis_type import Classic
from pyrqa.neighbourhood import FixedRadius
from pyrqa.neighbourhood import Unthresholded
from pyrqa.metric import EuclideanMetric
from pyrqa.computation import RQAComputation
from pyrqa.computation import RPComputation
from pyrqa.image_generator import ImageGenerator
import librosa
import librosa.display
import matplotlib.pyplot as plt
filename = 'E:/data/poco1/0218_2-1-1/about.wav'
y, sr = librosa.load(filename)
# trim silent edges  减去静音片段
voice, _ = librosa.effects.trim(y)
#librosa.display.waveplot(voice, sr=sr);
#plt.show();

data_points = voice
time_series = TimeSeries(data_points,
                         embedding_dimension=1,
                         time_delay=1)
settings = Settings(time_series,
                    analysis_type=Classic,
                    neighbourhood=Unthresholded(),
                    similarity_measure=EuclideanMetric,
                    theiler_corrector=1)
computation = RPComputation.create(settings)
result = computation.run()
ImageGenerator.save_recurrence_plot(result.recurrence_matrix_reverse,
                                    'recurrence_plot.png')

