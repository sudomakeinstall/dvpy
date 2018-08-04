# System
import os

# Third Party
import nibabel as nb


def nii_vol_to_slices(input_file, output_dir):
    assert os.path.isfile(input_file)

    os.makedirs(output_dir, exist_ok=True)

    vol = nb.load(input_file).get_data()

    for i in range(vol.shape[2]):
        im = vol[:, :, i]
        nb.save(nb.Nifti1Image(im, np.eye(4)), os.path.join(output_dir, "%d.nii" % (i)))
