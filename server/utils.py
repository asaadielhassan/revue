import os
import uuid
from flask import abort

import config

id = 0

def save_image(image):
    if not image.filename.endswith(tuple([".jpg", ".png"])):
        abort(409, "Image is not valid")

    # Generate random filename
    filename = str(uuid.uuid4()).replace("-", "") + "." + image.filename.split(".")[-1]
    image.save(os.path.join(config.image_upload_folder, filename))
    return filename

def get_current_id():
    id + 1
    return id
