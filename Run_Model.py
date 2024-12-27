from yolov9.detect_dual import run

def custom_yolo_run():
    # Customize the options for the YOLO run
    run(
        source='yolov9/test.jpg',  # Image/Video file
        device="cpu",  # Device to run the model
        # weights= 'best.pt', # Model weights
        name= 'yolov9_ppe_640_detect' # Experiment name"
    )

if __name__ == "__main__":
    custom_yolo_run()
