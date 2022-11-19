import moviepy.editor as mp


class VideoStickerFormatter:
    REQUIRED_WIDTH_PX = 512
    MAX_VIDEO_LENGTH_SEC = 3
    REQUIRED_MAX_FPS = 30

    def __init__(self, filename):
        self.video_clip = mp.VideoFileClip(filename)

    def rescale(self):
        self.video_clip = self.video_clip.resize(width=self.REQUIRED_WIDTH_PX)

    def format_video(self):
        self.remove_audio()
        self.rescale()
        self.trim()
        self.set_fps()

    def set_fps(self):
        if self.video_clip.fps > self.REQUIRED_MAX_FPS:
            self.video_clip = self.video_clip.set_fps(self.REQUIRED_MAX_FPS)

    def trim(self):
        self.video_clip = self.video_clip.subclip(0, self.MAX_VIDEO_LENGTH_SEC)

    def remove_audio(self):
        self.video_clip = self.video_clip.without_audio()

    def save_to_file(self, filename):
        self.video_clip.write_videofile(filename, codec="vp8")

    def format_and_save(self, filename):
        self.format_video()
        self.save_to_file(filename)


if __name__ == "__main__":
    try:
        vsf = VideoStickerFormatter("Video Of Funny Cat.mp4")
        vsf.format_video()
        vsf.save_to_file("test_formatted.WEBM")
    except OSError as e:
        print(e)
