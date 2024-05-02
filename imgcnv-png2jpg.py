from PIL import Image
import os
import glob

# ユーザー設定可能なパラメータ
IMAGE_QUALITY = 95  # JPEG保存時の品質設定
TARGET_WIDTH = 1000  # 縮小後の画像の幅
ROTATE_IF_TALL = 1  # 縦が長い場合に回転するか（0: 回転なし, 1: 回転あり）

def resize_and_convert_png_to_jpeg(input_directory):
    # 指定ディレクトリ内のすべてのPNGファイルを検索
    png_files = glob.glob(f"{input_directory}/*.png")
    
    # PNGファイルが見つからない場合、処理を終了
    if not png_files:
        print("PNGファイルが見つかりませんでした。")
        return
    
    # 出力用のディレクトリを作成（存在しない場合）
    output_directory = os.path.join(input_directory, "converted_jpeg")
    os.makedirs(output_directory, exist_ok=True)
    
    for png_file in png_files:
        img = Image.open(png_file)
        
        # 画像が縦長の場合の回転処理判定
        if img.height > img.width and ROTATE_IF_TALL:
            img = img.rotate(90, expand=True)
        
        # RGBAモードの画像をRGBモードに変換
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        
        # 縦横比を保持してリサイズ
        aspect_ratio = img.height / img.width
        new_height = int(TARGET_WIDTH * aspect_ratio)
        img_resized = img.resize((TARGET_WIDTH, new_height), Image.LANCZOS)
        
        # 生成した画像をJPEG形式で保存
        output_file_name = os.path.basename(png_file).replace(".png", ".jpg")
        output_file_path = os.path.join(output_directory, output_file_name)
        img_resized.save(output_file_path, "JPEG", quality=IMAGE_QUALITY)
        
        print(f"{png_file} を {output_file_path} に変換しました。")

# メイン実行部分
if __name__ == "__main__":
    # ユーザーから入力を受け取る
    input_directory = input("PNGファイルが保存されているディレクトリを入力してください：")
    
    # 入力されたディレクトリが存在するか確認
    if not os.path.exists(input_directory):
        print("指定されたディレクトリが存在しません。")
    else:
        resize_and_convert_png_to_jpeg(input_directory)
