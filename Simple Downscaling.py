from PIL import Image

def reduce_image_size(input_image_path, output_image_path, scale_factor, output_format='JPEG', quality=85):
    """
    Parametrlər:
    - input_image_path: str, giriş şəkil faylının yolu.
    - output_image_path: str, ölçüləri dəyişdirilmiş şəkilin saxlanılacağı yol.
    - scale_factor: float, şəkilin ölçüsünün neçə qat azaldılacağını göstərən əmsal.
      scale_factor-un 0.5 olması şəklin hər ölçüsünü yarıya endirəcək.
    - output_format: str, çıxış şəklinin formatı ('JPEG' və ya 'PNG'). JPEG - standart kimi sechilib
    - quality: int, JPEG formatı üçün çıxış keyfiyyəti (1-95). Yüksək dəyərlər daha yaxşı keyfiyyət və daha böyük fayl ölçüsü deməkdir.

    """


    with Image.open(input_image_path) as img:

        new_width = int(img.width * scale_factor)
        new_height = int(img.height * scale_factor)


        resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)


        if output_format.upper() == 'JPEG':
            resized_img.save(output_image_path, output_format, quality=quality)
        else:
            resized_img.save(output_image_path, output_format)

