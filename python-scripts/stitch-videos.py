from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip

def stitch_videos(video_paths, output_path):
    video_clips = []
    
    # Load each video clip
    for path in video_paths:
        clip = VideoFileClip(path)

        # Add the subtitles
        txt_clip = TextClip(subtitles[video_paths.index(path)], fontsize=70, color='white')
        txt_clip = txt_clip.set_pos('center').set_duration(clip.duration)

        video_clips.append(CompositeVideoClip([clip, txt_clip]))
    
    # Concatenate the video clips
    final_clip = concatenate_videoclips(video_clips, method="compose")
    
    # Save the final video
    final_clip.write_videofile(output_path, fps=30)

# Example usage
video_paths = ["/home/pranav/Downloads/_import_60e0167b4c3a96.14254367_preview.mp4", "/home/pranav/Downloads/200727_02_Videvo_Stock_Market_2_Growth_Color_2_preview.mp4", "/home/pranav/Downloads/Raindrops_Videvo_preview.mp4"]
subtitles = ["This is the first video", "This is the second video", "This is the third video"]
output_path = "output.mp4"

stitch_videos(video_paths, output_path)