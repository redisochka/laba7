def xd1():

    from PIL import Image

    img = Image.open("bruh.jpg")
    print("Размер изображения:", img.size)
    print("Формат изображения:", img.format)
    print("Цветовая модель:", img.mode)
    img.show()

def xd2():

    from PIL import Image

    image = Image.open("bruh.jpg")
    smaller_image = image.resize((int(image.width / 3), int(image.height / 3)))
    smaller_image.save("mini_bruh.jpg")
    horizontal_mirror = image.transpose(method=Image.FLIP_LEFT_RIGHT)
    horizontal_mirror.save("gorizontal_bruh.jpg")
    vertical_mirror = image.transpose(method=Image.FLIP_TOP_BOTTOM)
    vertical_mirror.save("vertikal_bruh.jpg")


def xd3():

    from PIL import Image, ImageFilter
    import os
    source_folder = "C:/Users/HP/Desktop/xd/Учеба/Программирование/7_лаба/old"
    target_folder = "C:/Users/HP/Desktop/xd/Учеба/Программирование/7_лаба/new"
    filter_type = ImageFilter.EMBOSS
    # Можно поставить любой другой фильтр
    for filename in os.listdir(source_folder):
        if filename.endswith('.jpg'):
            image = Image.open(os.path.join(source_folder, filename))
            filtered_image = image.filter(filter_type)
            new_filename = filename.split('.')[0] + '_filtered.jpg'
            filtered_image.save(os.path.join(target_folder, new_filename))


def xd4():

    from PIL import Image, ImageDraw, ImageFont
    import os
    
    images_folder = "C:/Users/HP/Desktop/xd/Учеба/Программирование/7_лаба/mark"
    watermark_text = '2xboots'
    watermark_color = (255, 0, 0)
    for filename in os.listdir(images_folder):
        if filename.endswith('.jpg'):
            image_path = os.path.join(images_folder, filename)
            image = Image.open(image_path)
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype('arial.ttf', 20)
            text_size = draw.textsize(watermark_text, font)
            x = image.width - text_size[0] - 10
            y = image.height - text_size[1] - 10
            draw.text((x, y), watermark_text, font=font, fill=watermark_color)
            image.save(os.path.join(images_folder, f'wm_{filename}'))


xd1()
xd2()
xd3()
xd4()
