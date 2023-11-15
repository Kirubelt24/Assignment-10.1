#main
from apiPackage.api import *

if __name__ == "__main__":
    #this is the instance of the TimeZoneInfo class
    timezone_info = TimeZoneInfo()

    #this calls the method to print time zone information
    timezone_info.print_timezone()