from skimage.measure import compare_ssim
import argparse
import imutils
import cv2
import os
from tqdm import tqdm

ap = argparse.ArgumentParser()
ap.add_argument("-o","--original", required=True, type=str, help="require original image")
ap.add_argument("-s","--contrast", required=True, type=str, help="require contrast image")
ap.add_argument("-i","--interpolation", type=str, default=cv2.INTER_AREA)
ap.add_argument("-v","--video", action='store_true')
args = ap.parse_args()

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
                contrast = cv2.resize(contrast, dsize=(o_width,o_height), interpolation=args.interpolation)

                o_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
                c_gray = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)

                (score, diff) = compare_ssim(o_gray, c_gray, full = True)

                diff = (diff*255).astype('uint8')
                total+=score

            except Exception as e:
                    print(str(e) + ": Total count mismatch!!!!")




            #if(i%100 == 0):
            #     print("SSIM: {}".format(score))

        video_ssim_mean = total / dir_len
        print("Video SSIM Mean : {}".format(video_ssim_mean))

    else:
        original = cv2.imread(args.original)
        contrast = cv2.imread(args.contrast)

        o_height, o_width, o_channel = original.shape
        contrast = cv2.resize(contrast, dsize=(o_width, o_height), interpolation=args.interpolation)

        o_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
        c_gray = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)

        (score, diff) = compare_ssim(o_gray, c_gray, full = True)
        diff = (diff*255).astype('uint8')
        print("Image SSIM Mean: {}".format(score))

if __name__ == '__main__':
    main()
