#!/usr/bin/env python

import argparse
import itk
import sys


def visualize(argv):
    parser = argparse.ArgumentParser(description='Apply median image filter to input image and visualize result')
    parser.add_argument('input_image', type=str,
                        help='Input image file name')
    parser.add_argument('output_image', type=str,
                        help='Output image file name')
    parser.add_argument('radius', type=int,
                        help='Median filter radius')
    args = parser.parse_args()

    # Open image with ITK
    image = itk.imread(args.input_image)
    #median_image = itk.median_image_filter(image, Radius = args.radius)
    median_image = itk.MedianImageFilter(image, Radius = args.radius)
    itk.imwrite(median_image, args.output_image)
    itk.ViewImage[median_image].View(median_image)
    
if __name__ == "__main__":
    sys.exit(visualize(sys.argv))
