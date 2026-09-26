from PIL import Image

im = Image.open("C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/products_redesign_desktop_full.png")
w, h = im.size
# Crop near bottom of products page where PDF section sits
crop_pdf = im.crop((0, int(h * 0.72), w, int(h * 0.95)))
crop_pdf.save("C:/Users/91867/.gemini/antigravity/brain/b40a29b1-f116-49cb-a23d-de3945320d99/products_pdf_section_full.png")
print("Cropped PDF section saved!")
