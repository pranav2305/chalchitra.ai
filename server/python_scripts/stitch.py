import ffmpeg

# list of video files
def stitch_videos(filepaths, path):
    files = [ffmpeg.input(f) for f in filepaths]

    # eparate video and audio, then flat the array
    video_and_audios_files = [item for sublist in map(lambda f: [f.video, f.audio], files) for item in sublist]

    # concat all
    joined = (
        ffmpeg
        .concat(*video_and_audios_files, v=1, a=1)
        .node
    )

    # merge video and audio
    (
        ffmpeg
        .output(joined[0], joined[1], path)
        .run()
    )