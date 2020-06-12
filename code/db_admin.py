import shutil
import glob
import pathlib



backup_path = glob.glob('Backup Server\*.csv')
dr_path = pathlib.Path('DR Server')

class MoveFile:
    for file in backup_path:
        shutil.copy(str(file), str(dr_path))
