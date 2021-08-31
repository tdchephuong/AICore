import shutil
import datetime
import os
import logging

def copy_file_to_folder(pathFile, dest_path):
    exist = os.path.isfile(pathFile)

    if not exist:
        log_error("file not exist." + pathFile)
        return
        
    shutil.copyfile(pathFile, dest_path)
    print("file has copied to : " + dest_path)

def backup_file(pathFile):
    date = datetime.datetime.now().strftime("%m%d%Y_%h%M%s")

    dest_file = "/content/drive/MyDrive/BillardAI/Models/best_" + date + ".pt"

    exist = os.path.isfile(dest_file)

    if exist:
        os.remove(dest_file)
        log_message("file has removed : " + "best_" + date + ".pt")
        return
        
    shutil.copyfile(pathFile, dest_file)
    log_message("file has copied to : " + "best_" + date + ".pt")

def movefile(pathFile):
    date = datetime.datetime.now().strftime("%m%d%Y")
    dest_file = "/content/drive/MyDrive/BillardAI/Models/best_" + date + ".pt"
    exist = os.path.isfile(dest_file)

    if exist:
        os.remove(dest_file)
        log_message("file has removed : " + "best_" + date + ".pt")
        return
        
    shutil.move(pathFile, dest_file)
    log_message("file has moved to : " + "best_" + date + ".pt")

    
def zipdir(zipFolder):
    date = datetime.datetime.now().strftime("%m%d%Y")
    output_filename = zipFolder + "label_" + date + ".zip"
    shutil.make_archive(output_filename, 'zip', zipFolder)

def unzip(zipFile):
    # unzip dataset
    if not os.path.isfile(zipFile):
        log_error("The zip file not found !!!")
        return 0
    shutil.unpack_archive(zipFile, "/content/Dataset")
    log_message("The file has unzip.")
    return 1

def log_error(message, *arguments):
    prefix = colorstr('red', 'bold', 'Error:')
    print(f"{prefix} {message}", arguments)


def log_message(message):
    prefix = colorstr('green', 'bold', 'Message:')
    print(f"{prefix} {message}")

def colorstr(*input):
    *args, string = input if len(input) > 1 else ('blue', 'bold', input[0])  # color arguments, string
    colors = {'black': '\033[30m',  # basic colors
              'red': '\033[31m',
              'green': '\033[32m',
              'yellow': '\033[33m',
              'blue': '\033[34m',
              'magenta': '\033[35m',
              'cyan': '\033[36m',
              'white': '\033[37m',
              'bright_black': '\033[90m',  # bright colors
              'bright_red': '\033[91m',
              'bright_green': '\033[92m',
              'bright_yellow': '\033[93m',
              'bright_blue': '\033[94m',
              'bright_magenta': '\033[95m',
              'bright_cyan': '\033[96m',
              'bright_white': '\033[97m',
              'end': '\033[0m',  # misc
              'bold': '\033[1m',
              'underline': '\033[4m'}
    return ''.join(colors[x] for x in args) + f'{string}' + colors['end']

def mkdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)
        return 1

    log_error(f"The path {path} has existed !" )
    return 0