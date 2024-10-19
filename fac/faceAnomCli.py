import click
import cv2 as cv


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """
    Entry point to preview the webcam.
    """

    if ctx.invoked_subcommand is None:

        capture = cv.VideoCapture(0)

        while True:
            isTrue, frame = capture.read()

            if isTrue:
                cv.imshow("Preview", frame)

                if cv.waitKey(1) == ord("q"):
                    break

            else:
                break

        capture.release()
        cv.destroyAllWindows()


@click.command()
def other_commands():
    pass


main.add_command(other_commands)
