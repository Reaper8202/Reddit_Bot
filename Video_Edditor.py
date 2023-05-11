from moviepy.editor import VideoFileClip, CompositeVideoClip, AudioFileClip
import os

# Set the paths to your video clips and audio file
Background_clip = "/Users/derek/Desktop/Python Code/Reddit Optimization/Reddit_Bot_2/background.mp4"  # Need to change path
audio_path = "/Users/derek/Desktop/Python Code/Reddit Optimization/askreddit.mp3"

# Load video clips and audio
clip2 = VideoFileClip(Background_clip)
audio = AudioFileClip(audio_path)

# Resize clips to compatible resolution (e.g., 1080x1920 for vertical video)
target_resolution = (1080, 1920)  # Adjust as needed

clip2 = clip2.resize(target_resolution)

# Cut clip2 to the length of the audio file
clip2 = clip2.subclip(0, audio.duration)

# Set the audio duration to match the minimum of the audio and the composite video
audio_duration = min(audio.duration, clip2.duration)
audio = audio.set_duration(audio_duration)

# Composite the clips
final_clip = CompositeVideoClip([clip2])
final_clip = final_clip.set_audio(audio)

# Set the output file path
output_path = "output.mp4"

# Write the final composite video with audio
final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

# Close the video and audio clips to release resources
clip2.close()
audio.close()
final_clip.close()
