import click
import cv2 as cv
import datetime
from . import blurframe


now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


@click.command()
@click.option(
    "-o",
    "--output",
    "outpath",
    default=f"fac_{now}.mp4",
    show_default=f"fac_{now}.mp4",
    type=click.Path(writable=True),
    help="Enter output filename or path/filename",
)
@click.option(
    "-fl",
    "--flip",
    "flip_webcam",
    default=1,
    show_default="1",
    type=click.IntRange(0, 1),
    help="1: Flips 0: Doesnot flips webcam",
)
def webcam(outpath, flip_webcam):
    capture = cv.VideoCapture(0)

    ## webcam width and height define the codec and create VideoWriter object
    height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
    width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
    fps = int(capture.get(cv.CAP_PROP_FPS))

    if fps == 0:
        fps = 30

    fourcc = cv.VideoWriter_fourcc(*"MJPG")
    writer = cv.VideoWriter(outpath, fourcc, fps, (width, height))

    if not capture.isOpened():
        print("Cannot Open Camera")
        return 1

    if not writer.isOpened():
        print("Cannot Open Video writer")
        return 1

    while True:
        isTrue, frame = capture.read()

        if isTrue:

            flipped_frame = blurframe.blurframe(frame, flip_webcam)

            writer.write(flipped_frame)
            cv.imshow(f"Recording {outpath}", flipped_frame)
            if cv.waitKey(1) == ord("q"):
                break

        else:
            break

    capture.release()
    writer.release()
    cv.destroyAllWindows()
