import pandas 
import numpy
import time


def pull():
   return
    



def main():
    start_time = time.time()
    excel_data_df_1 = pandas.read_excel('2012.xlsx', sheet_name= 'Sheet1')
    excel_data_df_2 = pandas.read_excel('2019.xlsx', sheet_name= 'Sheet1')
    print("Welcome to the HCA Healthcare IBM Technical Demo!")
    print("Here we will show how Spectrum Virtualize will operate over various storage arrays in the case of a particular patient")
    print("Please enter a patients name to pull all information regarding them")
    x = input()
    print("Searching over 400 storage arrays...")
    curr_time = time.time()
    while(time.time() < 5 + curr_time):
        x = 5
    print("Found Records of Carlson Jensen from 2012...")
    print(excel_data_df_1)
    while(time.time() < 12 + curr_time):
        x = 5
    print("Found Records of Carlson Jensen from 2019...")
    print(excel_data_df_2)
    print("Search complete, merging records into a homogonous storage array")
    print("Carlsen Jensen complete record after pulling from 400 homogonous storage arrays:")
    print(excel_data_df_2)
    print("Time to complete: ")
    print(time.time() - curr_time)
    print("Carlson Jensen records fully merged, ready to be used for later analysis!")
    return

if __name__ == "__main__":

    main()