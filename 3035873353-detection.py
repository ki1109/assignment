from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput, loadImage
#import jetson.inference
#import jetson.utils

net = detectNet("ssd-mobilenet-v2", threshold=0.5)
#camera = videoSource("/dev/video0") # '/dev/video0' for V4L2
input_image_path = "/home/nvidia/jetson-inference/examples/image/0.jpeg"
#input_image_path = "/home/nvidia/Desktop/1.jpeg"
display = videoOutput("result_0.jpg") # 'my_video.mp4' for file

#while display.IsStreaming():
for i in range(1):

    #img = camera.Capture()
    img = loadImage(input_image_path)
    if img is None: # capture timeout
        continue

    detections = net.Detect(img)

    for ClassID, detection in enumerate(detections):
        width = detection.Width
        height = detection.Height
        area = width * height
        center_x = detection.Center[0]
        center_y = detection.Center[1]

        print(f"-- ClassID: {ClassID}\n -- Confidence: {detection.Confidence:.3f}\n -- Left:   {detection.Left:.3f}\n -- Top:    {detection.Top:.3f}\n -- Right:  {detection.Right:.3f}\n -- Bottom: {detection.Bottom:.3f}\n -- Width:  {width:.3f}\n -- Height: {height:.3f}\n -- Area:   {area:.3f}\n -- Center: ({center_x:.3f}, {center_y:.3f})\n")


    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
