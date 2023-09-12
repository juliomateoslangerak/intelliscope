import pathlib

image_width = 1392
image_height = 1040
roi_width = 64

dataset = "H2b_20x_MD_exp911"
# dataset = "Tub_20x_MD_exp911"

if dataset == "Tub_20x_MD_exp911":
    # As for tubulin
    class_definitions = {
        "inter": 0,
        "aster": 1,
        "prometa": 2,
        "bipolar": 3,
        "ana": 4,
        "midbody": 5,
    }
else:
    # As for H2b
    class_definitions = {
        "inter": 0,
        "pro": 1,
        "prometa": 2,
        "meta": 3,
        "earlyana": 4,
        "lateana": 5,
        "telo": 6,
        "apo": 7,
    }

with (open(f"datasets/Kyoto_cells/labels/{dataset}/data/features.samples.txt", "r") as ann_file):

    for line in ann_file:
        ann_class = line.split("\t")[0]
        ann_class = class_definitions[ann_class]
        p, t, x, y = line.split("\t")[1].split("_")
        label_file = pathlib.Path(f"datasets/Kyoto_cells/labels/training/tubulin_{p}_{t}.txt")
        if label_file.exists():
            with open(label_file, "a") as f:
                f.write(f"{ann_class} {int(x[1:]) / image_width} {int(y[1:]) / image_height} {roi_width / image_width} {roi_width / image_height}\n")
        else:
            with open(label_file, "w") as f:
                f.write(f"{ann_class} {int(x[1:]) / image_width} {int(y[1:]) / image_height} {roi_width / image_width} {roi_width / image_height}\n")


