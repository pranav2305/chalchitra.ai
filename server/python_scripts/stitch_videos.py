from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
import os

def stitch_videos(video_paths, subtitles, output_path):
    # print current working directory
    print(os.getcwd())
    
    video_clips = []
    
    # Load each video clip
    for i, path in enumerate(video_paths):
        clip = VideoFileClip(path)

        # Add the subtitles
        txt_clip = TextClip(
            subtitles[i], fontsize=36, color='white')
        txt_clip = txt_clip.set_pos('bottom').set_duration(clip.duration)

        video_clips.append(CompositeVideoClip([clip, txt_clip]))
    
    # Concatenate the video clips
    final_clip = concatenate_videoclips(video_clips, method="compose")
    
    # Save the final video
    final_clip.write_videofile(output_path, fps=30, codec="libx264")

# # Example usage
# video_paths = ["/home/pranav/Downloads/_import_60e0167b4c3a96.14254367_preview.mp4", "/home/pranav/Downloads/200727_02_Videvo_Stock_Market_2_Growth_Color_2_preview.mp4", "/home/pranav/Downloads/Raindrops_Videvo_preview.mp4"]
# subtitles = ["This is the first video", "This is the second video", "This is the third video"]
# output_path = "output.mp4"

# stitch_videos(video_paths, output_path)