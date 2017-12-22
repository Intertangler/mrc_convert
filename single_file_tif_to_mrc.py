import mrcfile
import cv2
import os

def define_local_input_directory(default_input_directory):
    import os
    directories_decided = "n"
    while directories_decided == "n":
        print '\n \n default input directory is: ', default_input_directory
        input_directory = raw_input(
            'INPUT DIR: Enter path to folder that contains files to process, \n press Enter to use default directory, \n or type "cwd" to use current directory: ')
        if input_directory == 'cwd':
            input_directory = os.getcwd()+r'./'
        elif input_directory == '':
            input_directory = default_input_directory+r'./'
        else:
            pass
        print 'using ', input_directory, ' as input directory. \n'
        directories_decided = raw_input('Are you sure? Y/n')
        if directories_decided == '':
            directories_decided = "Y"
            break
        elif directories_decided == "Y":
            break
        else:
            directories_decided = "n"
    return input_directory

def define_local_output_directory(default_output_directory):
    import os
    directories_decided = "n"
    while directories_decided == "n":
        print '\n \n default output directory is: ', default_output_directory
        output_directory = raw_input('OUTPUT DIR: Enter path to folder where output files will be stored, \n press Enter to use default directory, \n or type "cwd" to use current directory: ')
        if output_directory == 'cwd':
            output_directory = os.getcwd()+r'./'
        elif output_directory == '':
            output_directory = default_output_directory+r'./'
        else:
            pass
        print 'using ', output_directory, ' as output directory. \n'
        directories_decided = raw_input('Are you sure? Y/n')
        if directories_decided == '':
            directories_decided = "Y"
            break
        elif directories_decided == "Y":
            break
        else:
            directories_decided = "n"
    return output_directory
input_dir = define_local_input_directory("D:/Google Drive/_PROJECTS_/MRC_convert/stacktest/file_source")
output_dir = define_local_output_directory("D:/Google Drive/_PROJECTS_/MRC_convert/stacktest/file_source")

job_name = raw_input('Job name: name sub-directory to create: ')
file_name = raw_input('Input file: without extension, enter name of tif file to process: ')
output_path = output_dir+job_name
if not os.path.exists(output_path):
    os.makedirs(output_path)
img = cv2.imread(input_dir + '/'+ file_name +'.tif', 0)
with mrcfile.new(output_path+ '/'+ file_name + '.mrc',overwrite=True) as mrc:
    mrc.set_data(img)#, dtype=np.int8)
    mrc.data
print 'mrc validation for: ' + output_path+'/'+file_name+'.mrc \n', mrcfile.validate(output_path+'/'+file_name+'.mrc')
print img
print '#################################'

# for i in range(0,20):
#     img = cv2.imread('origamis'+'%04d'% i+'.tif', 0)
#     #np.savetxt(newpath+'/text_image'+'%04d'% i+'.txt',img)
#     with mrcfile.new(newpath+'/origamis'+'%04d'% i+'.mrc',overwrite=True) as mrc:
#         mrc.set_data(img)#, dtype=np.int8)
#         mrc.data
#     print 'mrc validation for: ' + newpath+'/origamis'+'%04d'% i+'.mrc \n', mrcfile.validate(newpath+'/origamis'+'%04d'% i+'.mrc')
#     print '\n origamis'+'%04d'% i, img
#     print '#################################'





