# Development
## 1. Package dependency
`pip install python-decouple`

py -m debugpy --listen 5678 yolov5/detect.py --weights ModelTrained/best.pt --img 720 --conf 0.5 --source Videos/Video_1.mp4 --save-txt
python -m debugpy --listen 5678 yolov5/detect.py --weights ModelTrained/best.pt --img 720 --conf 0.5 --source Videos/Video_1.mp4 --save-txt

================Detect Object Moving===================
python -m debugpy --listen 5678 yolov5/detect_billard.py --weights ModelTrained/best.pt --img 720 --conf 0.5 --source Videos/Bilardo_1.1.mp4 

================Scenario===================
- test ball order: 
  1. 1 ball moving
  2. 2 ball moving
  3. all ball moving

ball name
  0: "Red",
  1: "White",
  2: "Yello",