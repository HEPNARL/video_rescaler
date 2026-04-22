import rescale_image
import rescale_video
import ratio_fit

def main():
    # rescale_image.rescale_images("in", "out")
    rescale_video.rescale_videos("in", "out", size=(1920,1080), target_ratio=16/9)
    ratio_fit.ratio_fit_images("in", "out",size=(1920,1080), prior_ratio=16/9)


if __name__ == "__main__":
    main()