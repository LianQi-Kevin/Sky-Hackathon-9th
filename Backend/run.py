"""
所有 API 遵循 RESTful API 设计规范
{
    code: int,  # http 状态码
    status: "success" | "error" | "fail",
    message: str,   # 当 status 为 error 或 fail 的时候提供原因
    data: dict  # 实际的数据体，一般为 dict
}
"""

import logging

from flask import Flask
from flask_cors import CORS

from apis.img_detect import img_bp
from utils.logging_utils import log_set

# from utils.API_utils import api_return

# init flask & CORS
app = Flask(__name__)
CORS(app)

# logging
log_set(log_level=logging.DEBUG, log_save=True)

# register BP
app.register_blueprint(img_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
