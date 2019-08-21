# MISSING VALUES
===================================================

# create a column with missing value
df['Col'] = np.nan
df['Date']= pd.NaT


# find which column has missing data
pd.isnull(df).any()


# count NaN
df.isnull()                  #DataFrame of booleans
df.isnull().sum()            #List the NaN count for each column:
df.isnull().sum().sum()      #Count the total number of NaNs present in whole df

# sum
df[['a','b']].sum(axis=1)
df[['a','b']].values.sum()


# Counting Missing values: missing values are usually excluded by default
df['column_x'].value_counts()             # excludes missing values
df.column_x.value_counts(dropna=False) # includes missing values


# Finding Missing Columns by using a boolean series to filter rows
df[df['x'].isnull()]        #only show rows where column_x is missing
df[df['x'].notnull()]       #only show rows where column_x is not missing


# fill NaN
df['col1'].fillna(value='NA', inplace=True) 
df = df.fillna({
    'col1': 'missing',
    'col2': '99.999',
    'col3': '999',
    'col4': 'missing',
    'col5': 'missing',
    'col6': '99'
})

df['col1'] = df['col1'].replace(-77, np.NaN) # replace values with NaN



# Change all NaNs to None (useful before loading to a db)
df = df.where((pd.notnull(df)), None)


# drop missing values
df.dropna(inplace=True)             # drop rows if ANY values are missing, defaults to rows, with columns with axis=1
df.dropna(how=’all’, inplace=True)  # drop a row only if ALL values are missing
df.dropna(thresh=5)                 # drop rows less than 5 nan in a rwo
df = df.dropna(axis=0, subset=['Col']) # drop NaN from a particular col


# turn off the missing value filter, replaces NaN with /s
df = pd.read_csv(‘df.csv’, header=0, names=new_cols, na_filter=False)


# Conditional replacing Nan Value
df['new'] = np.where(pd.isnull(df['col1']),0,df['col1']) + df['col2'] # swap in 0 for df['col1'] cells that contain null
df['X'] = np.where(df['X'].isnull(),"BROKER",df['X']) # change null value only in a series
df['X'] = ('BROKER').where(df['X'].isnull())

# Conditional Mapping with np.select
conditions = [
            (df['ORIGINATOR']=='Capital One'),
            (df['ORIGINATOR']=='Meridian Broker')
            ]
df['BUSINESS_MIX'] = np.select(conditions,['CAPITAL ONE','MERIDIAN'],default='DIRECT')
