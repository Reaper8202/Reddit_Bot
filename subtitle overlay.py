from moviepy.editor import TextClip, CompositeVideoClip, VideoFileClip
from moviepy.video.tools.subtitles import SubtitlesClip



main_video = VideoFileClip("C:\\Users\\billa\\Desktop\\PYTHON STUFF\\youtube\\M1.mp4")
generator = lambda txt: TextClip(txt, font="arial", fontsize=50, color="white", method='caption', size=main_video.size)

sub_clip = SubtitlesClip('C:\\Users\\billa\\Desktop\\PYTHON STUFF\\youtube\\subtitles.srt', generator)

result = CompositeVideoClip((main_video, sub_clip), size=main_video.size)
result.write_videofile('C:\\Users\\billa\\Desktop\\PYTHON STUFF\\youtube\\output.mp4', fps=main_video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
