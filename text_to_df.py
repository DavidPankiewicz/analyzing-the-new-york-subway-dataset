import csv
import pandas

def fix_turnstile_data(filenames):
    '''
    Takes in raw MTA data txt files with many entries per row and outputs 
    an updated text file with one entry per row. A new output text file is 
    created for every input file.  
    
    Filenames is a list of MTA Subway turnstile text files. 
    
    Example turnstile text:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    For more:
    http://web.mta.info/developers/turnstile.html
    '''

    for files in filenames:
        f_out = open("updated_" + files, 'w')
        with open(files, 'rb') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    length  =len(row)
                    index = 3
                    repeated = row[:3]
                    
                    # iterates over chunks of a line to find where
                    # to split entries into multiples lines
                    # See example input file 
                    while index < length:
                        predicate = row[index:index+5]
                        combined= repeated + predicate
                        write_this = ""
                        combined_index = 0
                        while combined_index < len(combined)-1:
                            write_this += combined[combined_index] + ","
                            combined_index +=1
                        write_this += combined[-1]
                        index += 5
                        #print write_this
                        f_out.write(write_this + '\n')

                f_out.close()
    return 

def create_master_turnstile_file(filenames, output_file):
    '''
    Takes multiple txt files ouptut by the fix_turnstile_data function and 
    creates one consolidated txt file containing all within the inputs. 
    '''
    with open(output_file, 'w') as master_file:
       master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
       for filename in filenames:
            with open (filename, 'r') as f:
                for line in f:
                    master_file.write(line)
    return


def filter_by_regular(filename):
    '''
    Read the csv file located at filename into a pandas dataframe,
    and filter the dataframe to only rows where the 'DESCn' column 
    has the value 'REGULAR'.
    '''
    
    df = pandas.read_csv(filename)
    turnstile_data = df[df['DESCn'] == 'REGULAR']
    return turnstile_data

def get_hourly_entries(df):
    '''
    Raw data is cumulative. Calculate differences to find entries 
    between times. 
    
    If NaN, fill/replace with 1.
    '''
    
    length = len(df['ENTRIESn'])
    ENTRIESn_hourly = []
    for each in range(0, length-1):
       ENTRIESn_hourly.append(df.iloc[each+1]["ENTRIESn"] - df.iloc[each]["ENTRIESn"])
    ENTRIESn_hourly.append(0)
    df['ENTRIESn_hourly'] = ENTRIESn_hourly
    df.ENTRIESn_hourly =    df.ENTRIESn_hourly.shift(1)
    df.ENTRIESn_hourly = df.ENTRIESn_hourly.fillna(1)
    return df

def get_hourly_exits(df):
    '''
    Raw data is cumulative. Calculate differences to find entries 
    between times. 
    
    If NaN, fill/replace with 0.
    '''
    length = len(df['EXITSn'])
    EXITSn_hourly = []
    for each in range(0, length-1):
       EXITSn_hourly.append(df.iloc[each+1]["EXITSn"] - df.iloc[each]["EXITSn"])
    EXITSn_hourly.append(0)
    df['EXITSn_hourly'] = EXITSn_hourly
    df.EXITSn_hourly =    df.EXITSn_hourly.shift(1)
    df.EXITSn_hourly = df.EXITSn_hourly.fillna(0)
    return df

#Examples
fix_turnstile_data(["turnstile_110528.txt", "turnstile_110514.txt"])
create_master_turnstile_file(["updated_turnstile_110528.txt", "updated_turnstile_110514.txt"], "master_turnstile.csv")
