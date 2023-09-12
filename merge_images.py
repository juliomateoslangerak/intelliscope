import pathlib
import numpy as np
from PIL import Image

# pos_list = [13, 37, 38, 39, 40, 41, 42, 45, 46]
pos_list = [13, 37, 46]

for pos in pos_list:
    images_path = pathlib.Path(f"datasets/Kyoto_cells/images/prediction/00{pos}").glob("*.tif")
    crfp_image_files = sorted([x for x in images_path if x.is_file() and "Crfp" in x.name])
    images_path = pathlib.Path(f"datasets/Kyoto_cells/images/prediction/00{pos}").glob("*.tif")
    cgfp_image_files = sorted([x for x in images_path if x.is_file() and "Cgfp" in x.name])

    for r_file, g_file in zip(crfp_image_files, cgfp_image_files):
        r_image = Image.open(r_file)
        g_image = Image.open(g_file)
        r_image = np.array(r_image)
        g_image = np.array(g_image)
        r_image = r_image[:, :, np.newaxis]
        g_image = g_image[:, :, np.newaxis]
        image = np.concatenate((r_image, g_image, np.zeros_like(r_image)), axis=2)
        image = Image.fromarray(image)
        image.save(f"datasets/Kyoto_cells/images/validation/{r_file.name[:-15]}.tif")
