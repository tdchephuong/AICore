# Development
## 1. Package dependency
`pip install python-decouple`

py -m debugpy --listen 5678 yolov5/detect.py --weights ModelTrained/best.pt --img 720 --conf 0.5 --source Videos/Video_1.mp4 --save-txt
python -m debugpy --listen 5678 yolov5/detect.py --weights ModelTrained/best.pt --img 720 --conf 0.5 --source Videos/Video_1.mp4 --save-txt