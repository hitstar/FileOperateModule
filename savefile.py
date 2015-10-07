import os
import os.path

def save_file(file_src, file_path, file_name):
    '''
    save the file_buf into file_path with file_name 
    '''
    if not os.path.isdir(file_path):
        os.mkdir(file_path)

    file_location = file_path + file_name
    
    if not os.path.exists(file_location):
        file_dst = open(file_location, 'wb')

        for line in file_src.readline():
            file_dst.write(line)

        file_dst.close()


