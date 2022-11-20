import argparse
import os


def validate_path(path):
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError("Invalid path.")

    return path


def validate_folder(path):
    validate_path(path)

    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError("This path is not a directory.")

    return path


parser = argparse.ArgumentParser(
    prog="Telegram Video Sticker Formatter",
    description="Use this tool to prepare your video files to be used as Telegram video stickers.",
    epilog="Written by @kokokojo2.",
)
parser.add_argument(
    "action-type",
    choices=["format", "check"],
    help="Action to perform on files.",
)
parser.add_argument(
    "-in",
    "--input-path",
    required=True,
    type=validate_path,
    help="source file or folder to process the video from. If the folder is submitted, all contained video-files are processed",
)
parser.add_argument(
    "-out",
    "--output-path",
    required=True,
    type=validate_folder,
    help="destination folder where the processed video(s) will be stored",
)
