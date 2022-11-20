import os
import mimetypes
from alive_progress import alive_bar

from argparser import parser
from formatter import VideoStickerFormatter


def is_video_file(file_name):
    return mimetypes.guess_type(file_name)[0].startswith("video")


def collect_video_paths(folder):
    return [
        os.path.join(folder, file)
        for file in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, file)) and is_video_file(file)
    ]


def process_video(input_path, output_path):
    video_formatter = VideoStickerFormatter(input_path)
    video_formatter.format_video()
    video_formatter.save_to_file(output_path)


def check_video(*args):
    input_path = args[0]
    raise NotImplementedError


def get_action(action_type):
    if action_type == "format":
        return process_video

    if action_type == "check":
        return check_video


def run(input_path, output_folder, action_type, batch):
    video_paths = collect_video_paths(input_path) if batch else [input_path]
    action_func = get_action(action_type)

    print(f"collected {len(video_paths)} video file(s)")
    print(f"executing {action_type} action\n")

    with alive_bar(len(video_paths)) as progress_bar:
        for path in video_paths:
            try:
                action_func(
                    path,
                    os.path.join(
                        output_folder,
                        os.path.basename(path).split(".")[0] + "-tg-video-sticker.webm",
                    ),
                )
            except OSError as e:
                print(e)
                print("Skipping...")

            progress_bar()


if __name__ == "__main__":
    args = vars(parser.parse_args())

    batch_mode = os.path.isdir(args["input_path"])
    action = args["action-type"]

    run(args["input_path"], args["output_path"], args["action-type"], batch_mode)
