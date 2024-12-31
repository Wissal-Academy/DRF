import os
import uuid
from datetime import datetime


def file_uploder(instance, filename):
    # ex: my.photo.png ['my', 'photo', 'png']
    ext = filename.split(".")[-1]
    # format date 2024/12/31
    date_str = datetime.now().strftime("%Y/%m/%d")
    # New filename full path : date_str/uuid.ext
    new_filename = f"{date_str}/{uuid.uuid4()}.{ext}"
    # RETURN FULL PATH : projects/date_str/uuid.ext
    return os.path.join("projects/", new_filename)
