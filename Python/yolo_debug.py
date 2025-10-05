import os, inspect
import yolov3
from yolov3 import yolo as yolo_mod
import yolov3.models as yolo_models

print("yolov3 package dir:", os.path.dirname(yolov3.__file__))
print("yolo.py:", yolo_mod.__file__)
print("models.py:", yolo_models.__file__)

from yolov3.yolo import YOLOv3
try:
    src = inspect.getsource(YOLOv3.__init__)
    print("\n--- YOLOv3.__init__ (first 80 lines) ---")
    print("\n".join(src.splitlines()[:80]))
except OSError:
    print("Could not read YOLOv3.__init__ source.")

# Quick existence check for YOUR weights file (adjust path if needed)
candidate = "/home/banoodle/git/Vid2DopplerMulti/Environment/data/vibe_data/yolov3.weights"
print("\nYour weights at:", candidate, "exists?", os.path.exists(candidate))
print("Size (bytes) if exists:", os.path.getsize(candidate) if os.path.exists(candidate) else "N/A")


import numpy as np
from psbody.mesh.visibility import visibility_compute
print("psbody-mesh OK with NumPy", np.__version__)

import sys, numpy as np
print("NumPy:", np.__version__, np.__file__)
import psbody, importlib, pkgutil
print("psbody paths:", psbody.__path__)
from psbody.mesh import visibility
print("visibility .so:", visibility.__file__)
print("OK")