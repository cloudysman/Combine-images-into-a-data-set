from PIL import Image

def create_collage(image_files, collage_width, output_file):
    images = [Image.open(file) for file in image_files]
    widths, heights = zip(*(i.size for i in images))

    max_height = max(heights)
    total_width = collage_width
    num_rows = len(images) // collage_width + int(len(images) % collage_width > 0)

    new_im = Image.new('RGB', (total_width * max(widths), num_rows * max_height))

    x_offset = 0
    y_offset = 0
    for count, im in enumerate(images):
        new_im.paste(im, (x_offset, y_offset))
        x_offset += im.size[0]
        if (count + 1) % collage_width == 0:
            x_offset = 0
            y_offset += max_height

    new_im.save(output_file)

# Example usage:
image_files = ['image_page_2_xref_83.png', 'image_page_2_xref_85.png', 'image_page_2_xref_87.png',
               'image_page_2_xref_88.png', 'image_page_2_xref_89.png', 'image_page_2_xref_90.png',
               'image_page_2_xref_91.png', 'image_page_2_xref_92.png', 'image_page_2_xref_93.png',
               'image_page_2_xref_94.png', 'image_page_2_xref_95.png', 'image_page_2_xref_96.png',
               'image_page_2_xref_97.png', 'image_page_2_xref_99.png']  # list of image paths
collage_width = 7  # or however many images you want in a row
output_file = 'collage.jpg'  # the output file
create_collage(image_files, collage_width, output_file)
