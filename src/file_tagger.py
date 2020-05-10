from shutil import copyfile
import os
import errno
from os.path import isfile, join
import random
import sys

#name includes full path
def create_output_dir(name):
    try:
        os.mkdir(name)
    except OSError as e:
        if e.errno == errno.EEXIST:
            print "output directory already exist, try using some other directory name"
            exit(-1)
    
   
src_path=""
dst_path=""

#name includes full path
def validate_input_dir(name):
    if not os.path.exists(name):
        print "input directory {} doesn't exist".format(name) 
        exit(-1)

def validate_command():
    if len(sys.argv) < 3:
        print "usage: tag_dir_content <input_dir> <output_dir>" 
        exit(-1) 

    global src_path, dst_path
    src_path = sys.argv[1]
    dst_path = sys.argv[2]
    print "[TAGGING] content of {} to {}".format(src_path, dst_path)


def main():
    global src_path, dst_path
    validate_command()
    validate_input_dir(src_path)
    dir_content = os.listdir(src_path)
    create_output_dir(dst_path)
    
    file_count = len(dir_content) 

    for f in dir_content:
        input_file = src_path + "/"+ f
        print input_file
        if os.path.isfile(input_file):
            file_extension = None
            file_extension = os.path.splitext(f)[1]
            while True:
                rand_file_name = str(random.randint(1, 10*file_count))
                new_dest_name = dst_path + "/" + rand_file_name + file_extension

                if os.path.exists(new_dest_name):
                    print "[INFO] duplicate random number, recorrecting"
                    continue
                else:
                    print "[RENAMING] [{}] -> [{}]".format(f, new_dest_name)
                    copyfile(input_file, new_dest_name)
                    break
            
        elif os.path.isdir(input_file):
            print "[WARNING] directory {} is not renamed".format(input_file)
        else:            
            print "[ERROR] file doesn't exist".format(input_file)

if __name__=="__main__":
    main()


