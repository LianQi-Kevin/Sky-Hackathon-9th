import os

import numpy as np
from flask import Blueprint, request

try:
    from utils.API_utils import api_return
    from utils.csvParser import CSV_dict_parser
    from utils.NGC_SDXL import get_ngc_SDXL
except Exception:
    from ..utils.csvParser import CSV_dict_parser
    from ..utils.API_utils import api_return
    from ..utils.NGC_SDXL import get_ngc_SDXL

img_bp = Blueprint('img_tools', __name__)


@img_bp.route("/upload", methods=["POST"])
def img_upload():
    """get upload raw img"""
    file = request.files.to_dict()["file"]
    save_path = os.path.join("Backend/static/upload_images", file.filename)
    file.save(save_path)

    return api_return(200, "success", None, {"save_path": save_path})


@img_bp.route("/getStyle", methods=["GET"])
def get_style():
    """decode style.csv and format"""
    return api_return(code=200, status="success", data={
        "style": [{
            "value": index,
            "label": style['name'],
            "prompts": {"prompt": style["prompt"], "negative_prompt": style["negative_prompt"]}
        } for index, style in enumerate(CSV_dict_parser("static/styles.csv"))]})


@img_bp.route("/getSDXL", methods=["POST"])
def get_SDXL():
    """
    get NGC SDXL IMG
    https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-foundation/models/sdxl/api
    """
    if request.json.get("prompt", None) is None:
        return api_return(code=400, status="fail", message="prompt is required")

    prompt = request.json.get("prompt")
    negative_prompt = request.json.get("negative_prompt", "")
    seed = request.json.get("seed", np.random.randint(0, 4294967296, dtype=np.int64))
    sampler = request.json.get("sampler", "DDIM")
    scale = request.json.get("scale", 5)
    steps = request.json.get("steps", 25)

    for index, style in enumerate(request.json.get("styles") if request.json.get("styles", "") != "" else []):
        if index == 0:
            if "{prompt}" in style["prompts"]["prompt"]:
                prompt = style["prompts"]["prompt"].replace("{prompt}", prompt)
            else:
                prompt = ",".join([prompt, style["prompts"]["prompt"].replace("{prompt}", "")])
        else:
            prompt = ",".join([prompt, style["prompts"]["prompt"].replace("{prompt}", "")])
        negative_prompt = ", ".join([style["prompts"]["negative_prompt"].replace("{prompt}", ""), negative_prompt])

    b64_json = get_ngc_SDXL(
        prompt=prompt,
        negative_prompt=negative_prompt,
        seed=seed,
        sampler=sampler,
        scale=scale,
        steps=steps,
        config_path="config_self.json"
    )

    return api_return(code=200, status="success", data=b64_json)
