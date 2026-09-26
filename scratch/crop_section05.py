from PIL import Image

im = Image.open("C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/solutions_8cards_desktop.png")
# Full height is around 4000+ px, crop section 05 (around y=2000 to y=3500)
w, h = im.size
crop_im = im.crop((0, int(h * 0.55), w, int(h * 0.85)))
crop_im.save("C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/solutions_section05_desktop.png")
print("Cropped Section 05 saved!")
