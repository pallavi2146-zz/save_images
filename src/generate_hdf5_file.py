import argparse
from src.hdf5 import hdf5_file_generator


def generate_hdf5_file(opts):

    data_path = opts.data_path
    output_location = opts.output_location
    output_file_name = opts.output_file_name
    img_target_size = opts.img_target_size

    hdf5_file_generator.generator(data_path, output_location, output_file_name, img_target_size)

    print "DONE!"

    print output_file_name+".h5 saved at location : " + output_location + "."

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Saving image dataset as a single hdf5 file.')
    parser.add_argument('--data_path', action='store', dest='data_path',
                        required=True, help='images directory path')

    parser.add_argument('--output_location', action='store', dest='output_location',
                        required=True, help='directory path to store output file')
    parser.add_argument('--output_file_name', action='store', dest='output_file_name',
                        required=True, help='preferable output file name')

    parser.add_argument('--img_target_size', action='store', dest='img_target_size',
                        required=False, default=(225,225), help='required image dimension')
    opts = parser.parse_args()
    generate_hdf5_file(opts)
