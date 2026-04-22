import rescale_image
import rescale_video

def main():
    rescale_image.rescale_images("in", "out")
    rescale_video.rescale_videos("in", "out")


if __name__ == "__main__":
    main()