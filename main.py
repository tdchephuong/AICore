import argparse
import os
import shutil
import sys
from ultils.ultils import mkdir, log_error, log_message


def initialize_test(source):
    log_error("Google Drive Error :", sys.exc_info()[0], "occurred.")

def initialize(source):
    try:
        from google.colab import drive
    except ImportError as error:
        log_error(error.__class__.__name__ + ": " + error.message)

    # mount drive folder
    for i in range(3):
        try:
            drive.mount('/content/drive')
            log_message("Drive has mounted.")
            break
        except:
            log_error("Google Drive Error :", sys.exc_info()[0], "occurred.")
            log_message("- Try again !.")
            print()

    # make dir Videos
    mkdir('/content/Videos')

    # make dir Videos
    mkdir('/content/Dataset')

    # # unzip dataset
    # if not os.path.isfile(source):
    #     log_error("The source file not exist !!!")
    #     return

    # shutil.unpack_archive(source, "/content/Dataset")
    # log_message("File has Unzipped into directory [Dataset]." + source)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, help='/content/drive/MyDrive/BillardAI/<file>.zip, the zip file google drive')
    opt = parser.parse_args()
    print(opt)
    local = '0'
    try:
        from decouple import config

        local = config('LOCAL')
        if local == '1':
            initialize_test(**vars(opt))

    except ImportError as error:
        log_message("--- We are run in PROD ---")
    
    if local != '1':
        initialize(**vars(opt))
    