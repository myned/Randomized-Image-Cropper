import os
from glob import iglob
from random import randint, choice


from PIL import Image


# Decrease this value to widen the range of randomization
PERCENT = 0.2


def main():
    for path in ('images', 'crops'):
        if not os.path.exists(path):
            os.mkdir(path)

    images = []
    for filename in iglob('images/*'):
        images.append(Image.open(filename))
    if not images:
        print('ERROR : PROJECT_HOME/images is empty')
        exit()

    for image in images:
        percentw = int(image.width * PERCENT)
        percenth = int(image.height * PERCENT)
        randw = randint(percentw, image.width - percentw)
        randh = randint(percenth, image.height - percenth)

        if choice((True, False)):
            crop = image.crop((
                randw,
                randh,
                image.width,
                image.height
            ))
        else:
            crop = image.crop((
                0,
                0,
                image.width - randw,
                image.height - randh
            ))

        crop.save(f'crops/{os.path.basename(image.filename)}')

        print(f'Cropped : {images.index(image) + 1}/{len(images)}', end='\r')

    print('\nFINISHED : Cropped images in PROJECT_HOME/crops')


if __name__ == '__main__':
    main()
