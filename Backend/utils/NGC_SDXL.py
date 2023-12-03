import json

import numpy as np
import requests

INVOKE_URL = "https://api.nvcf.nvidia.com/v2/nvcf/pexec/functions/89848fb8-549f-41bb-88cb-95d6597044a4"
FETCH_URL_FORMAT = "https://api.nvcf.nvidia.com/v2/nvcf/pexec/status/"


def get_ngc_SDXL(prompt: str, negative_prompt: str = '',
                 seed: int = np.random.randint(0, 4294967296, dtype=np.int64), sampler: str = "DDIM",
                 scale: int = 5, steps: int = 25, config_path: str = "../config.json"):
    with open(config_path, "r") as f:
        NGC_API_KEY = json.loads("".join(f.readlines()))["NGC_SDXL_API_KEY"]

    authorization_header = {
        "Authorization": f"Bearer {NGC_API_KEY}",
        "Accept": "application/json"
    }

    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "sampler": sampler,  # str ("DDIM", "DPM", "LMS", "EulerA")
        "seed": int(seed),  # int (0-4294967296)
        "unconditional_guidance_scale": scale,  # int (1-9)
        "inference_steps": steps  # int (5-100)
    }

    # re-use connections
    session = requests.Session()

    response = session.post(INVOKE_URL, headers=authorization_header, json=payload)

    while response.status_code == 202:
        request_id = response.headers.get("NVCF-REQID")
        fetch_url = FETCH_URL_FORMAT + request_id
        response = session.get(fetch_url, headers=authorization_header)

    response.raise_for_status()
    return response.json()  # {'b64_json': 'b64_img'}


if __name__ == '__main__':
    print(get_ngc_SDXL("beach", "", 18, "DDIM", 5, 5, "../config_self.json"))
