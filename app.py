# coding:utf-8

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import re
from ocr_recognition import get_ocr_result

app = Flask(__name__)


@app.route('/upload/image', methods=['POST'])
def upload():
    f = request.files['file']
    basepath = os.path.dirname(__file__)  # 当前文件所在路径
    upload_path = os.path.join(basepath, 'static\\uploads', secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
    f.save(upload_path)
    orc_content = get_ocr_result(upload_path)
    # 正则匹配

    reg = '[A-F0-9a-f]{2}[-:][A-F0-9a-f]{2}[-:.][A-F0-9a-f]{2}[-:][A-F0-9a-f]{2}[-:.][A-F0-9a-f]{2}[-:][' \
          'A-F0-9a-f]{2}'
    return {"success": True, "data": {
        "orc_data": orc_content,
        "mac": re.findall(reg, orc_content)
    }}


if __name__ == '__main__':
    app.run(debug=True)
