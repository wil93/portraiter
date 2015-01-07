#!/usr/bin/env python2

from time import sleep
from SimpleCV import *

def main(argv):
    img = Camera().getImage()
    img.show()
    sleep(2)
    detectedFaces = img.findHaarFeatures("face2.xml")

    for face in detectedFaces:
        center = (face.x, face.y)
        dimens = (1.5 * face.width(), 2.0 * face.height())
        face = img.crop(center[0] - dimens[0] / 2, center[1] - dimens[1] / 2, dimens[0], dimens[1])
        face.show()
        sleep(2)

    sleep(10)

if __name__ == '__main__':
    main(sys.argv)
