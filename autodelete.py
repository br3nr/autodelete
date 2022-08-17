import os
import time
import datetime

#"C:\\Users\\max\\Desktop"
def get_days(dtime):

    days, months = dtime.day, dtime.month * 30
    return days + months


def autodelete():
    for folder, subs, files in os.walk("C:\\Users\\max\\Pictures"):

        print(bcolors.WARNING + folder + bcolors.ENDC)
        for file in files:
           
            time_str = time.ctime(os.path.getctime(os.path.join(folder,file)))
            curr_time = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y") 
            format_time = datetime.datetime.strptime(time_str, "%a %b %d %H:%M:%S %Y")
            
            file_age = get_days(curr_time) - get_days(format_time)
            

            if file_age > 5:
                print(bcolors.OKCYAN + file + bcolors.FAIL + " : " + str(file_age) + " DAYS OLD"  + bcolors.ENDC) 
            else:
                print(bcolors.OKCYAN + file + bcolors.OKGREEN + " : " + str(file_age) + " DAYS OLD"  + bcolors.ENDC) 

            
            


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