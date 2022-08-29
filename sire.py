"""
    This file is a utility to generate random/organized files
    for test purposes.

    Usage
        sire <OPTIONS> destination
        sire -conf [configuration file location]


        OPTIONS
            -n [num] - number of files to generate
            -s [size] - size of each file in (B, KB, MB, GB, TB)
                        eg: 10KB, 5MB, 50GB
            
"""

import argparse

parser = argparse.ArgumentParser(description="Utility to generate random files for test purposes")
parser.add_argument("-n", "--num", type=int, help="Number of files to generate in given location", nargs=1)
parser.add_argument("-s", "--size", type=str, help="Size of files to generate in given location", nargs=1)
parser.add_argument("-c", "--conf", type=str, help="Location for file list generation configuration", nargs=1)

class Configuration:
    def __init__()

args = None
configuration = None

def main():
    global args
    args = parser.parse_args()

    # Validate the args here

    if args.conf and (args.num or args.size):
        print ("Use any one of the configuration parameters")
        exit(1)
    
    if (args.conf):
        read_configuration_file()
    else:
        if args.num and args.size:
            read_configuration_from_args()
        else:
            print ("Use any one of the configuration parameters")
            exit(1)
    


def read_configuration_from_args:
    pass


def read_configuration_file:
    pass


if __name__ == "__main__":
    main()