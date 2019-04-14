#packages
import pandas as pd
import re
import sys
import multiprocessing as mp
import numpy as np


#Global conditions
iref_df = pd.read_csv('./dataset/All.mitab.01-22-2018.txt', sep = "\t",chunksize=100000)
for chunk in iref_df:
    g_columns = chunk.columns
    break
df = pd.DataFrame()
for iref in iref_df:
    # Script

    # One split columns
    def onesplit(os_df,col):
        # We Remove any symbol from the column names
        col = re.sub(r'[^\w]', '', col)
        '''We split the data values from the column on the : 
        and we store them in separate columns'''
        values_raw = os_df.str.split(":",-1,expand=True)
        '''We create dummies columsn 0 or 1 based on the 
        databases where the column code came from. We also
        add the column name as a prefix to the names of the
        new columns'''
        dummies_df = pd.get_dummies(values_raw[0], prefix=col)
        '''We add the code value to the name of the column'''
        dummies_df[col] = values_raw[1]
        # We re-order the colummns
        col_df = dummies_df.columns.tolist()
        col_df = col_df[-1:] + col_df[:-1]
        # we store the new daframe into its final version and export it
        final_df = dummies_df[col_df]
        return final_df

    # One Split Column but multiple data
    def onesplit_mdata(os_df,col):
        # We divide Tax due to structure in column
        final_df = pd.DataFrame()
        if "tax" in col:
            temp_col = os_df.str.extract('([a-zA-Z]+:[^a-zA-Z]+)', expand=False).str.strip("(")
            temp_col = temp_col.str.extract('([^a-zA-Z]+)', expand=False).str.strip(":(-)[]")
            temp_desc = os_df.str.replace('([a-zA-Z]+:[^a-zA-Z]+)', "").str.strip(")")
            final_df[col] = temp_col
            col1 = "desc_"+col
            final_df[col1]= temp_desc
            return final_df
        else:
            values_raw = os_df.str.split(":",-1,expand=True)
            if len(values_raw.columns) >+ 2:
                # Divive Interaction and method from psi_mi and mi
                print(col)
                # PSI-MI
                psi_mi_df= values_raw[values_raw[0].str.contains('psi-mi')==True]
                psi_mi_df[1]=psi_mi_df[2].str.replace('([a-zA-Z ]+)', "").str.rstrip('"()')
                psi_mi_df[2]=psi_mi_df[2].str.extract("([a-zA-Z ]+)",expand=False)
                # MI
                mi_df= values_raw[values_raw[0].str.contains('psi-mi')==False]
                mi_df[2]=mi_df[1].str.extract("([a-zA-Z ]+)",expand=False)
                mi_df[1]=mi_df[1].str.replace('([a-zA-Z ]+)', "").str.rstrip('"()')
                # Concatenating into a new final DataFrame
                final_df = pd.concat([psi_mi_df, mi_df])
                # New DataFrame Columns
                temp_col=[]
                temp_col.append(col+"_db")
                temp_col.append("code_"+col)
                temp_col.append("desc_"+col)
                final_df = final_df.rename(columns={'0': temp_col[0], '1': temp_col[1],'2': temp_col[2]})
                return final_df
            else:
                # Extract the data from column with the code and description from the column
                code_temp = values_raw[1].str.replace(r'([a-zA-Z ]+)', '').str.strip()
                code_temp = code_temp.str.strip(":()")
                final_df[col]=code_temp
                desc_temp=values_raw[1].str.extract('([a-zA-Z ]+)', expand=False).str.strip()
                desc_col = "desc_"+col
                final_df[desc_col]=desc_temp
                # We creater dummies to store the presence of different code types/databases
                dummies_df = pd.get_dummies(values_raw[0], prefix=col)
                col_dum_df = dummies_df.columns.tolist()
                final_df[col_dum_df]= dummies_df[col_dum_df]
                return final_df.head()

    # Multiple Split Column from Multiple Databases
    def multiplesplit(os_df,col):
        values_raw = os_df.str.split("|",-1,expand=True)
        print(col)
        #print(os_df.head(2))
        #print(values_raw.head(2))
        if "aliasA" == col:
            for i in values_raw.columns:
                print("---------------------------")
                print(values_raw[i].unique())
    # Processing 
    def processing(arg):
        '''The DataFrame has a list of columns that only store one database source at a time
        it is very unlikely for that to change due to the descriptions. It is worth nothing that
        this data is easier to process so they are store separately.'''
        s_split_col = ["#uidA","uidB","pmids","Checksum_A","Checksum_B",
        "OriginalReferenceA",	"OriginalReferenceB",	"FinalReferenceA",
        "FinalReferenceB", "Checksum_Interaction"]
        m_split_one_db_col = ["method","taxa", "taxb", "interactionType", "sourcedb",
        "biological_role_A", "biological_role_B", "experimental_role_A", "experimental_role_B",	
        "interactor_type_A", "interactor_type_B","Host_organism_taxid"]
        sin_val = ["Creation_date", "Update_date","Negative","MappingScoreA", 
        "MappingScoreB", "irogida", "irogidb", "irigid", "crogida", "crogidb", 
        "crigid", "icrogida", "icrogidb", "icrigid","imex_id", "edgetype", 
        "numParticipants", "xrefs_A", "xrefs_B", "xrefs_Interaction", "Annotations_A", 
        "Annotations_B", "Annotations_Interaction","expansion"]
        if arg in s_split_col:
            results = onesplit(iref[arg],arg)
        elif arg in m_split_one_db_col:
            results = onesplit_mdata(iref[arg],arg)
        elif arg in sin_val:
            df_final = pd.DataFrame()
            df_final[arg] = iref[arg]
            #print(df_final.head())
            #return pd.DataFrame(iref_df[arg],columns=arg)
        elif "author" == arg:
            pass
        else:
            results = multiplesplit(iref[arg],arg)
    def main():
        # we set the method for multiprocessing
        #mp.set_start_method('spawn')
        # we choose an appropriate amount of threads to use
        pool = mp.Pool(processes = int(mp.cpu_count()/2))
        results = pool.map(processing,g_columns)
        sys.exit()
        pool.close()
        pool.join()
        results_df = pd.concat(results)
        '''# loading the dataframe
        # clean ulA and ultB columns with only the uniprot code
        uid_a = iref_df["#uidA"].str.split(":",-1,expand=True)
        iref_df["#uidA"] = uid_a[1]
        uid_b = iref_df["uidB"].str.split(":",-1,expand=True)
        iref_df["uidB"] = uid_b[1]
        # creating iterables for multipool processing
        # as well as diving into selected groups by first protein in interaction
        # grp_lst_args = list(iref_df.groupby(["#uidA"]).groups.items())
        uidA = iref_df["#uidA"].unique()
        uidA = np.array_split(uidA,8)
        # df divided in 24 chunks of 100000
        for chunk in iref_df:
            columns = chunk.columns

            break
        # we choose an appropriate amount of threads to use
        if mp.cpu_count() <=2:
            pool = mp.Pool(processes = 1)
        elif mp.cpu_count() <=4:
            pool = mp.Pool(processes = 2)
        elif mp.cpu_count() <= 6:
            pool = mp.Pool(processes = 3)
        elif mp.cpu_count() <= 10:
            pool = mp.Pool(processes = 5)
        else:
            print("hi")
            pool = mp.Pool(processes = (mp.cpu_count() - 1))
        
        for chunk in iref_df:
            results = pool.map(processing,chunk)
            
        sys.exit()

        #  setting up pool number for process
        pool = mp.Pool(processes = (mp.cpu_count() - 1))
        results = pool.map(processing, uidA)
        sys.exit()
        pool.close()
        pool.join()
        results_df = pd.concat(results)
        print(results_df)
    '''
    if __name__ == "__main__":
        main()
        
    break