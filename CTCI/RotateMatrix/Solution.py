"""
Given ain image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
Can you do this in place?
"""
from PIL import Image
from numpy import asarray
def rotate(img):#Ok, it rotates 90° per iteration. but it requires extra space. basically, 2*size(n). which would actually be just n, just still, it requires twice the space
    result = img.copy()
    print(result.shape)
    for row in range(img.shape[0]-1):
        for cell in range(len(img[row])):
            #result[img.shape[0] - row - 1][cell] = img[row][img.shape[1] - cell - 1]
            result[cell][img.shape[0] - row - 1] = img[row][img.shape[1] - cell - 1]
    return result

def rotateInPlace(imgA):
    img = imgA.copy()#numpy wont allow me to edit the original file
    for i in range(img.shape[0] // 2):
        first = i
        last = img.shape[0] - 1 - i
        for j in range(first, last):
            offset = j - first
            top = img[first][j]
            img[first][j] = img[last-offset][first]
            img[last-offset][first] = img[last][last-offset]
            img[last][last-offset] = img[j][last]
            img[j][last] = top
    return img

if __name__ == "__main__":
    img = Image.open('unnamed.png')
    img = asarray(img)
    #result = rotate(img)
    result = rotateInPlace(img)
    img_result = Image.fromarray(result).save('result.png')