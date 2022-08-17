import os
import time
import glob 


def autodelete():
    for folder, subs, files in os.walk("."):

        print(bcolors.WARNING + folder + bcolors.ENDC)
        for file in files:
           
            age = os.path.getctime(os.path.join(folder,file))

            clock = time.time()

            new = clock - age

            print(time.ctime(new))

            print(bcolors.OKCYAN + file + bcolors.ENDC)






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