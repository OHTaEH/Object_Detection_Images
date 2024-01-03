from roboflow import Roboflow
rf = Roboflow(api_key="5HRlMG01N3CS6kNrdlTF")
project = rf.workspace("roboflow-gw7yv").project("fish-yzfml")
dataset = project.version(44).download("yolov8")
