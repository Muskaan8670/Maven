from PIL import Image

im = Image.open("C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/products_redesign_desktop_full.png")
w, h = im.size
crop_cat = im.crop((0, int(h * 0.1), w, int(h * 0.45)))
crop_cat.save("C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/products_redesign_cat_grid.png")
print("Cropped category grid saved!")
