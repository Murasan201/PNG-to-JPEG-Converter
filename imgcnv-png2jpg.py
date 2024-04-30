
from PIL import Image
import os
import glob

def resize_and_convert_png_to_jpeg(input_directory):
    # 指定ディレクトリからPNGファイルのリストを取得
    png_files = glob.glob(f"{input_directory}/*.png")
    
    if not png_files:
        print("PNGファイルが見つかりませんでした。")
        return
    
    output_directory = os.path.join(input_directory, "converted_jpeg")
    os.makedirs(output_directory, exist_ok=True)
    
    for png_file in png_files:
        img = Image.open(png_file)
        
        if img.height > img.width:
            img = img.rotate(90, expand=True)
        
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        
        aspect_ratio = img.height / img.width
        new_height = int(1200 * aspect_ratio)
        img_resized = img.resize((1000, new_height))
        
        output_file_name = os.path.basename(png_file).replace(".png", ".jpg")
        output_file_path = os.path.join(output_directory, output_file_name)
        img_resized.save(output_file_path, "JPEG")
        
        print(f"{png_file} を {output_file_path} に変換しました。")

if __name__ == "__main__":
    input_directory = input("PNGファイルが保存されているディレクトリを入力してください：")
    
    if not os.path.exists(input_directory):
        print("指定されたディレクトリが存在しません。")
    else:
        resize_and_convert_png_to_jpeg(input_directory)
