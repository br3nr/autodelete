import os
import time


def autodelete():
    for folder, subs, files in os.walk("C:\\Users\\max\\Desktop"):

        print(bcolors.WARNING + folder + bcolors.ENDC)
        for file in files:
           
            sub_time = time.time() - os.path.getctime(os.path.join(folder,file))
            time_str = time.ctime(sub_time).split()
            
            print(bcolors.OKCYAN + file + bcolors.ENDC)
            print("Days old = " + time_str[2])


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == "__main__":
    autodelete()