from moviepy.editor import VideoFileClip, CompositeVideoClip, AudioFileClip
import os

# Set the paths to your video clips and audio file
Reddit_clip = "/Users/derek/Desktop/Python Code/Reddit Optimization/filler.mp4"  # Need to change path
Background_clip = "/Users/derek/Desktop/Python Code/Reddit Optimization/background.mp4"  # Need to change path
audio_path = "/Users/derek/Desktop/Python Code/Reddit Optimization/askreddit.mp3"

# Load video clips and audio
clip1 = VideoFileClip(Reddit_clip)
clip2 = VideoFileClip(Background_clip)
audio = AudioFileClip(audio_path)

# Resize clips to compatible resolution (e.g., 1080x1920 for vertical video)
target_resolution = (1080, 1920)  # Adjust as needed

clip1 = clip1.resize(target_resolution)
clip2 = clip2.resize(target_resolution)

# Cut clip2 to the length of the audio file
clip2 = clip2.subclip(0, audio.duration)

# Set the duration of the composite video based on the longer clip
duration = max(clip1.duration, clip2.duration)

# Extend the shorter clip if needed
clip1 = clip1.set_duration(duration)

# Set the audio duration to match the minimum of the audio and the composite video
audio_duration = min(audio.duration, duration)
audio = audio.set_duration(audio_duration)

# Composite the clips
final_clip = CompositeVideoClip([clip1, clip2])
final_clip = final_clip.set_audio(audio)

# Set the output file path
output_path = "output.mp4"

# Write the final composite video with audio
final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

# Close the video and audio clips to release resources
clip1.close()
clip2.close()
audio.close()
final_clip.close()
