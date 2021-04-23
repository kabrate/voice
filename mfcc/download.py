import pytube
#下载视频地址
my_url="https://www.youtube.com/watch?v=QJ7EVRvRDas&t=20s"
#下载
pytube.YouTube(my_url).streams.filter(only_audio=False, file_extension="mp4")[0].download(output_path="E:/",filename="my_audio")


