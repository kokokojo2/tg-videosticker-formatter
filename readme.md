# Telegram video-sticker formatter utility
This script allows you to reformat any video file(s) to be compatible with Telegram`s
[requirements](https://core.telegram.org/stickers#video-stickers-and-emoji) for video-sticker sources.

## Trying out
### Installation
The installation process is as straightforward as it can be.
```
git clone https://github.com/kokokojo2/tg-videosticker-formatter
cd tg-videosticker-formatter
pip install -r requirements.txt
```

### Processing single video file
Specify path to your video file using `-in` flag and
output folder where the formatted video should be stored via `-out` flag.
```
python tg-videosticker-formatter.py format -in cats.webm -out .
```
### Processing a directory of video files
You can also batch process video files. Specify the path to a
folder that contains your video files using `-in` flag.
```
python tg-videosticker-formatter.py format -in cats/ -out cats-reformatted/
```
You can know more about the args by specifying the `--help` flag like this
```
python tg-videosticker-formatter.py --help
```

### Things to notice
If submitted video is longer than 3 seconds a subclip from `00:00-00:03` will be selected.

