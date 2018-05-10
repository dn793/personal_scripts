'''
Simple script to scan for and delete duplicate files
within the same folder under a root directory.
'''

import os

ROOT_DIR = 'D:\\'
MAIN_FILE = 'cover.png'
DUPE_FILE = 'cover.jpg'

def main():
    dupe_list = list()
    found_dupes = False

    # Scan for files under root directory
    for dir_name, subdir_list, file_list in os.walk(ROOT_DIR):
        if (MAIN_FILE in (name.lower() for name in file_list) and
            DUPE_FILE in (name.lower() for name in file_list)):
            found_dupes = True
            dupe_list.append(dir_name)

    if (found_dupes):
        # Print directories where duplicates are found
        print("-W- The following directories have both specified files:")
        print("\n\t{}\n".format('\n\t'.join(dir for dir in dupe_list)))

        # Prompt for deletion
        if (input("-?- Do you want to delete the duplicate files? (y/n)\n").strip().lower() == 'y'):
            for dir in dupe_list:
                try:
                    os.remove(os.path.join(dir, DUPE_FILE))
                except OSError as err:
                    print("-E- Error occurred during file deletion:")
                    print("{0} - {1}".format(err.filename, err.strerror))
    else:
        print("-I- No dupes found!")

if __name__ == '__main__':
    main()
