from ultralytics import YOLO
from tkinter.filedialog import askopenfilenames

# Load an official or custom model
model = YOLO("yolov8x-oiv7.pt")

# Perform tracking with the model
results = model.predict(
    askopenfilenames(
        title="Please select",
        filetypes=(
            (
                "Image Files",
                (
                    "*.avic",
                    "*.bmp",
                    "*.dng",
                    "*.heic",
                    "*.heif",
                    "*.jp2",
                    "*.jpeg",
                    "*.jpg",
                    "*.mpo",
                    "*.png",
                    "*.tif",
                    "*.tiff",
                    "*.webp",
                )
            ),
            (
                "Video Files",
                (
                    "*.asf",
                    "*.avi",
                    "*.gif",
                    "*.m4v",
                    "*.mkv",
                    "*.mov",
                    "*.mp4",
                    "*.mpeg",
                    "*.mpg",
                    "*.ts",
                    "*.wmv",
                    "*.webm",
                )
            ),
        )
    ),
    save_dir="results",
    stream=True,
    verbose=True
)

for result in results:
    result.save()
    result.save_crop(save_dir="crops")
