from PIL import Image

im = Image.open("C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/products_redesign_desktop_full.png")
w, h = im.size
crop_mid = im.crop((0, int(h * 0.25), w, int(h * 0.75)))
crop_mid.save("C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/products_redesign_desktop_middle.png")
print("Cropped middle section saved!")
