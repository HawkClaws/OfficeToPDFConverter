import subprocess
import os

def convert_to_pdf(file_path, output_path=None):
    """
    指定されたファイルをPDFに変換する関数。変換後のPDFファイルの保存先も指定できる。
    
    Args:
    file_path (str): 変換するファイルのパス。
    output_path (str, optional): 生成されたPDFファイルの保存先パス。指定がない場合は元のファイルと同じ場所に保存される。
    
    Returns:
    str: 生成されたPDFファイルのパス。
    """
    # 出力パスが指定されていない場合は、元のファイル名に基づいてPDFファイル名を生成
    if output_path is None:
        base_name, _ = os.path.splitext(file_path)
        output_path = f"{base_name}.pdf"
    
    # unoconvコマンドを実行してファイルをPDFに変換
    subprocess.run(['unoconv', '-f', 'pdf', '-o', output_path, file_path])
    
    print(f"変換完了: {output_path}")
    return output_path
