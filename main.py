import rescale_image
import rescale_video
import ratio_fit
import argparse

def parse_size(value: str):
    try:
        w, h = value.lower().split("x")
        return int(w), int(h)
    except ValueError:
        raise argparse.ArgumentTypeError("Size must be in format WIDTHxHEIGHT (e.g. 1920x1080)")


def parse_ratio(value: str):
    try:
        w, h = value.split(":")
        return int(w) / int(h)
    except ValueError:
        raise argparse.ArgumentTypeError("Ratio must be in format W:H (e.g. 16:9)")


def main():
    parser = argparse.ArgumentParser(description="Image & video rescaling pipeline")

    parser.add_argument("--input", default="in", help="Input directory (default: in)")

    parser.add_argument("--output", default="out", help="Output directory (default: out)")

    parser.add_argument("--size", type=parse_size, default=(1920, 1080), help="Target size as WIDTHxHEIGHT (default: 1920x1080)")

    parser.add_argument("--ratio", type=parse_ratio, default=3 / 2, help="Source aspect ratio as W:H (default: 3:2)")
    args = parser.parse_args()

    # Video processing
    rescale_video.rescale_videos(args.input, args.output, size=args.size, target_ratio=args.ratio)
    # Image processing
    ratio_fit.ratio_fit_images(args.input, args.output, size=args.size, prior_ratio=args.ratio)

if __name__ == "__main__":
    main()