from PIL import Image

def blackAndWhite():
    img = Image.open(r"C:\Users\pc\Desktop\Praveen\2.jpg")
    BlackAndwhite = img.convert("L")
    BlackAndwhite.save(r"C:\Users\pc\Desktop\Praveen\baw.png")

if __name__ == '__main__':
    blackAndWhite()
        