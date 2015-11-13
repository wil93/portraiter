#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Portraiter.

Usage:
  portraiter.py <input_file> <output_file> [--quiet]
  portraiter.py <output_file> --webcam [--quiet]

Options:
  -h --help     Show this screen.
  -q --quiet    Avoid showing the preview.

"""

import sys
import cv2
from docopt import docopt

def main():
    args = docopt(__doc__, version='Portraiter 0.1')

    if args["--webcam"]:
        print("Not supported yet. PRs welcome.")
        sys.exit(1)
    else:
        imcolor = cv2.imread(args["<input_file>"])

    haarFace = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
    detectedFace = haarFace.detectMultiScale(imcolor)

    area = 0
    best = None
    for face in detectedFace:
        if not args["--quiet"]:
            tx, ty = face[0], face[1]
            l = face[2]
            bx, by = tx + l, ty + l
            cv2.rectangle(imcolor, (tx, ty), (bx, by),
                          (155, 255, 25), 2)

        if face[2] ** 2 > area:
            best = face
            area = face[2] ** 2

    if not args["--quiet"]:
        cv2.imshow('Face Detection', imcolor)
        cv2.waitKey()

    if area == 0:
        print "Non ho trovato facce"
        sys.exit(0)

    face = best

    l = face[2]
    tx, ty = face[0], face[1] - l/3
    bx, by = tx + l, ty + 5*l/3

    ll = (2 * (by - ty) / 3) - l
    tx -= ll/2
    bx += ll/2

    crop_img = imcolor[ty:by, tx:bx]
    cv2.imwrite(args["<output_file>"], crop_img)
