#packages
import pandas as pd
import re
import sys

def onedataset(data_column,data_values):
    # We split the column into the two, first column will be the the 
    # dataset name and the second one is the value assigned to it
    
    #we delete all symbols out of the name of the column
    data_column = re.sub(r'[^\w]', '', data_column)
    print(data_column)
    # We split the string into two columns through :
    two_temp = data_values.str.split(":",-1,expand=True)
    # We extract all unique values
    u_values = two_temp[0].unique()
    print(u_values)
    print(type(u_values))
    print(type(data_column))
    # We create the column names
    n_values = data_column+"_"+ u_values
    print(n_values)
    # We create a temporary dataframe with the name of columns
    empty = pd.DataFrame(columns = n_values)
    for i in range(len(u_values)):    
        print(u_values[i])
        # We find all the values containing the name of the u_values
        df2 = two_temp[0].str.contains(u_values[i],na=False)
        print(df2.head())
        print(df2.value_counts())
        print("-------BREAK-------")
        # We store the values into the empty DF
        empty[n_values[i]] = two_temp[1][df2]
    return empty

def more2datasets(d_column,d_values):
    three_temp = d_values.str.split("|",-1,expand=True)
    df_empty = pd.DataFrame()
    print("more2datasets")
    print(three_temp.head())
    print(d_column)
    for column, values in three_temp.iteritems():
        a = onedataset(d_column,values)
        print(a.head())
        break
        if df_empty.empty:
            df_empty = a
        else:
            df_empty = pd.concat([df_empty,a])
    print("-------BREAK-------")
    print(df_empty.head())
    return df_empty
    
    
  
def main():
    #loading the dataframe
    temp = pd.read_csv('./dateset./All.mitab.01-22-2018.txt', sep = "\t")
    #new dataframe
    final = pd.DataFrame()
    for column, values in temp.iteritems():
        a= values.str.split(":",-1,expand=True)
        col_num = len(a.columns)
        if col_num >= 3:
            # Searching that the dataset have more than one entry
            # dataset_1 : dataset1_code , dataset_2 : dataset2_code
            final = more2datasets(column,values)
            print(column)
            print(values[0])
            print("over two columns")
            break
        elif col_num <= 2:
            # Searching that the dataset have one entry dataset : dataset_code
            final = onedataset(column,values)
            print(final.head())
            print(column)
            print(values[0])
            print("two columns")
        else:
            # If there are not internal dataset inside the column
            break
        

if __name__ == "__main__":
    main()