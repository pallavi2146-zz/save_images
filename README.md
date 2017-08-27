# Save Images
Saving large number of images into single HDF5 file or TFRecord.

## Setup
```
$ git clone https://github.com/pallavi2146/save_images.git
$ cd save_images
$ pip install -r requirements.txt
```
## Usage
Note : Your dataset directory structure must as bellow:
```
--/root
    --/train
        --/cat
            --/cat_img1.jpg
            --/cat_imag2.jpg
                .
                .
                .
        --/dog
          --/dog_img1.jpg
          --/dog_img2.jpg
                .
                .
                .         
```
* Commands to run
```
$ python generate_hdf5_file.py --data_path=../root/train --output_location=../root --output_file_name=catvsdog_train --target_size=(225, 225)

# For more info about "command options" check bellow command
$ python generate_hdf5_file.py --help
```




