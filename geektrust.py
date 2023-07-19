# from sys import argv
#
# def main():
#
#     """
#     Sample code to read inputs from the file
#
#     if len(argv) != 2:
#         raise Exception("File path not entered")
#     file_path = argv[1]
#     f = open(file_path, 'r')
#     Lines = f.readlines()
#     //Add your code here to process the input commands
#     """
#
# if __name__ == "__main__":
#     main()
import argparse
# from Logic.rider_sharing import RiderSharing
from Logic import rider_sharing


def process_command(command):
    # rider_sharing = RiderSharing()
    parts = command.split()
    if parts[0] == 'ADD_DRIVER':
        rider_sharing.add_driver(parts[1], float(parts[2]), float(parts[3]))
    elif parts[0] == 'ADD_RIDER':
        rider_sharing.add_rider(parts[1], float(parts[2]), float(parts[3]))
    elif parts[0] == 'MATCH':
        rider_sharing.match(parts[1])
    elif parts[0] == 'START_RIDE':
        rider_sharing.start_ride(parts[1], int(parts[2]), parts[3])
    elif parts[0] == 'STOP_RIDE':
        rider_sharing.stop_ride(parts[1], float(parts[2]), float(parts[3]), int(parts[4]))
    elif parts[0] == 'BILL':
        rider_sharing.bill(parts[1])


def main():
    parser = argparse.ArgumentParser(description='Ride-sharing service')
    parser.add_argument('input_file', help='Path to the input file')

    args = parser.parse_args()

    input_file = args.input_file
    # print(input_file)

    with open(input_file, 'r') as file:
        for line in file:
            # print(line)
            command = line.strip()
            process_command(command)


if __name__ == '__main__':
    main()
