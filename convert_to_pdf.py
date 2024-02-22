import subprocess
import os

def convert_to_pdf(file_path, output_path=None):
    """
    指定されたファイルをPDFに変換する関数。変換後のPDFファイルの保存先も指定できる。
    変換に成功した場合はTrueを返し、失敗した場合はExceptionを発生させる。
    
    Args:
    file_path (str): 変換するファイルのパス。
    output_path (str, optional): 生成されたPDFファイルの保存先パス。指定がない場合は元のファイルと同じ場所に保存される。
    
    Returns:
    str: 生成されたPDFファイルのパス。
    
    Raises:
    Exception: PDFファイルの作成に失敗した場合。
    """
    # 出力パスが指定されていない場合は、元のファイル名に基づいてPDFファイル名を生成
    if output_path is None:
        base_name, _ = os.path.splitext(file_path)
        output_path = f"{base_name}.pdf"
    
    # unoconvコマンドを実行してファイルをPDFに変換
    result = subprocess.run(['unoconv', '-f', 'pdf', '-o', output_path, file_path], capture_output=True, text=True)
    
    # 変換後のPDFファイルが存在するかチェック
    if os.path.exists(output_path):
        print(f"変換完了: {output_path}")
        return output_path
    else:
        # エラーメッセージを含めてExceptionを発生
        error_msg = f"PDFファイルの作成に失敗しました。unoconv出力: {result.stderr}"
        raise Exception(error_msg)
