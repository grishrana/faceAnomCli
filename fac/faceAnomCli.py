import click
import cv2 as cv
from .Scripts import blurframe, webcam, image


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """
    Entry point to preview the webcam.
    """

    if ctx.invoked_subcommand is None:

        capture = cv.VideoCapture(0)

        if not capture.isOpened():
            print("Cannot Open Camera")
            return 1

        while True:
            isTrue, frame = capture.read()

            if isTrue:
                flipped_frame = blurframe.blurframe(frame)
                cv.imshow("Preview", flipped_frame)

                if cv.waitKey(1) == ord("q"):
                    break

            else:
                break

        capture.release()
        cv.destroyAllWindows()


main.add_command(webcam.webcam)
main.add_command(image.image)
