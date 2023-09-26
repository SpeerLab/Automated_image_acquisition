import shutil
import os
import time

"""This file is updated on 11.19.2021. Now it shouldn't corrupt when trying to transfer an unfinished image"""

def _copyfileobj_patched(fsrc,fdst,length = 16*1024*1024):
    """Patches shutil method to hugely improve copy speed"""
    """Note on 6.17.2019: somehow the transfering of .dax files is quite slow and
    when taking images over 80 sections, drive E will be full before the acquisition
    finishes. This is annoying because there won't be error message, and the laser will
    be on for 9999999+ frames if not manually engaged.
    This code is from https://stackoverflow.com/questions/21799210/python-copy-larger-file-too-slow
    , which increase the shutil buffer zone from 16KB to 16MB so that the file transfering becomes much
    faster (at least at the same speed as manual file transfer)"""
    while True:
        buf = fsrc.read(length)
        if not buf:
            break
        fdst.write(buf)
shutil.copyfileobj = _copyfileobj_patched


#os.mkdir("Z:\\Kyle\\New_Data\\SCN_Wt_adult_21Sep2020\\")
#os.mkdir("Z:\\Kyle\\New_Data\\SCN_Wt_adult_21Sep2020\\acquisition\\")

destination_dir = "Y:\\Chenghang\\ET33_Tigre\\20230828_1\\acquisition\\"

acquisition_dir = "E:\\chenghaz_temp\\"
rc_dir = destination_dir
rc_dir_extensions = destination_dir


while True:
    filelist = os.listdir(acquisition_dir)
    print("Regenerating file list in 10s")
    time.sleep(10)
    for file in filelist:
        file_name, file_extension = os.path.splitext(file)
        new_file = os.path.join(acquisition_dir, file)
        if new_file.endswith(".inf"):
            #Updated on 11.18.2021. Now the code will move the image when its size is not increasing, rather than simply wait for 60s
            while 1:
                temp_size = os.path.getsize(acquisition_dir + file_name + '.dax')
                time.sleep(10)
                temp_size_2 = os.path.getsize(acquisition_dir + file_name + '.dax')
                if temp_size_2 == temp_size:
                    break
            print("moving " + new_file)
            #And also other files.
            shutil.move(new_file,rc_dir)
            shutil.move(acquisition_dir + file_name + ".dax",rc_dir)
            shutil.move(acquisition_dir + file_name + ".png", rc_dir_extensions)
            shutil.move(acquisition_dir + file_name + "_lock_cam.png", rc_dir_extensions)
            shutil.move(acquisition_dir + file_name + ".off", rc_dir_extensions)
            shutil.move(acquisition_dir + file_name + ".power", rc_dir_extensions)
            shutil.move(acquisition_dir + file_name + ".xml", rc_dir_extensions)
            print("drive cleared")
           # new = open(acquisition_dir + 'new_inf.txt', 'a')
           # new.write(str(file) + os.linesep)

        #extensions = ('.png', '.insight', '.off', '.power', '.xml')
        #if any(new_file.endswith(ext) for ext in extensions):
        #    shutil.move(new_file, rc_dir_extensions)
        #    print("drive cleared")
        #    print("searching for new movies")
            

