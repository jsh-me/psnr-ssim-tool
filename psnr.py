import numpy
import math
import cv2
import os
import argparse
from tqdm import tqdm

ap = argparse.ArgumentParser()
ap.add_argument("-o","--original", required=True, type=str, help="require original file path")
ap.add_argument("-s","--contrast", required=True, type=str, help="require contrast file path")
ap.add_argument("-i","--interpolation", type=str, default=cv2.INTER_AREA)
ap.add_argument("-v","--video", action='store_true')
args = ap.parse_args()

def psnr(img1, img2):
    mse = numpy.mean((img1 - img2)**2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20*math.log10(PIXEL_MAX/math.sqrt(mse))

def main():
    if args.video:
        dir_len = len(os.walk(args.original).__next__()[2])
        print("total file number:{}".format(dir_len))
        total = 0

        for i in tqdm(range(1, dir_len)):
            try:
                o_image = "%05d" % i +".png"
                c_image = "%05d" % i +".png"

                original = cv2.imread(args.original + o_image)
                contrast = cv2.imread(args.contrast + c_image)

                o_height, o_width, o_channel = original.shape
                contrast = cv2.resize(contrast, dsize=(o_width,o_height), interpolation=cv2.INTER_AREA)

                total += psnr(original, contrast)

            except Exception as e:
                    print(str(e) + ": Total count mismatch!!!!")

            #if(i%100 == 0):
            #     print("PSNR: {}".format(psnr(original, contrast)))

        video_psnr_mean = total / dir_len
        print("Video PSNR Mean : {}".format(video_psnr_mean))

    else:
        original = cv2.imread(args.original)
        contrast = cv2.imread(args.contrast)

        o_height, o_width, o_channel = original.shape
        contrast = cv2.resize(contrast, dsize=(o_width, o_height), interpolation=args.interpolation)

        print("Image PSNR Mean: {}".format(psnr(original, contrast)))

if __name__ == '__main__':
    main()
