import pandas as pd
df = pd.read_csv('data.csv') #Reads the CSV in a dataframe (Downloaded a random data from internet)
print(df.head()) #Shows the top 5 rows
''' Returned
   id first_name  last_name                            email  gender      ip_address
0   1      Naomi      Dadge         ndadge0@biblegateway.com  Female   89.157.158.46
1   2   Meredeth     Olford             molford1@squidoo.com    Male  56.170.130.119
2   3     Aylmar   Dimsdale             adimsdale2@slate.com    Male   50.134.200.83
3   4     Verina     Dyzart               vdyzart3@wired.com  Female   196.78.87.138
4   5     Nancee  Longfield  nlongfield4@cargocollective.com  Female    87.33.252.24
'''

'''
df.tail() shows the bottom 5 rows
If you want specific amount of rows to be represented, you can write df.head/tail(NUM OF ROWS)

To read an excel file, you can write pd.read_excel('FILENAME')'''

#Read headers
print(df.columns) #Shows the name of the columns

''' Returned
Index(['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address'], dtype='object')
'''
#To read a specific column
print(df['first_name'].head()) # FORMAT - df['NAME OF COLUMN']
''' Returned
0       Naomi
1    Meredeth
2      Aylmar
3      Verina
4      Nancee
Name: first_name, dtype: object
NOTE: IF YOU DONT WANT INDEXING OR A LINE WRITTEN BELOW YOU CAN PUT NAME OF COLUMN LIKE THIS - df[[NAME OF COLUMN]]
'''
#Reading specific rows by indexing
print(df.iloc[0:3]) #Shows the first 3 rows (Its same as df.head(3)) but would be helpful if you want to read middle row
''' Returned
   id first_name last_name                     email  gender      ip_address
0   1      Naomi     Dadge  ndadge0@biblegateway.com  Female   89.157.158.46
1   2   Meredeth    Olford      molford1@squidoo.com    Male  56.170.130.119
2   3     Aylmar  Dimsdale      adimsdale2@slate.com    Male   50.134.200.83
'''
#Reading a specific element by its index
print(df.iloc[1,2]) # Write it in the format df.iloc[ROW, COLUMN]
'''Returned : Olford'''

#If you want to add a condition like only shows rows where gender is equal to Male/Female
print(df.loc[df['gender'] == 'Male'])
'''Returned
      id first_name   last_name                     email gender       ip_address
1      2   Meredeth      Olford      molford1@squidoo.com   Male   56.170.130.119
2      3     Aylmar    Dimsdale      adimsdale2@slate.com   Male    50.134.200.83
5      6       Hank  Faircliffe     hfaircliffe5@youtu.be   Male     182.51.54.50
7      8   Chrotoem       Hemms        chemms7@uol.com.br   Male     55.246.0.122
9     10      Raddy       Negri        rnegri9@oakley.com   Male    233.45.216.57
..   ...        ...         ...                       ...    ...              ...
189  190      Blake        Been      bbeen59@bandcamp.com   Male    208.99.250.50
190  191     Daniel      Simone   dsimone5a@cafepress.com   Male   157.193.26.122
194  195      Hilly    Tomblett  htomblett5e@geocities.jp   Male  230.253.192.153
196  197   Dominick     Holyard        dholyard5g@mail.ru   Male    23.190.128.61
197  198     Guntar       Payle    gpayle5h@shinystat.com   Male    87.64.218.179

AS YOU CAN SEE, IT IS ONLY SHOWING ROWS WHERE GENDER IS MALE
'''

#Applying multiple conditions
filt_df = df.loc[(df['gender']=='Female') & (df['id'] > 50)] # Remember to put conditions in parenthesis and us '&' instead of 'and' and '|' instead of 'or'

print(filt_df)
'''Returned
      id  first_name   last_name                       email  gender       ip_address
50    51     Ethelin      Domoni         edomoni1e@adobe.com  Female    49.213.10.102
51    52      Doreen      Broome       dbroome1f@archive.org  Female   111.180.239.55
54    55       Joice     Crisell    jcrisell1i@clickbank.net  Female    226.67.21.155
57    58       Brett  Zamboniari  bzamboniari1l@examiner.com  Female    39.116.61.139
58    59     Sydelle    Haylands         shaylands1m@pbs.org  Female      2.113.4.190
..   ...         ...         ...                         ...     ...              ...
192  193      Shayna      Mishow        smishow5c@cpanel.net  Female    88.185.183.11
193  194      Paloma      Phelps          pphelps5d@xing.com  Female     46.63.70.142
195  196     Darleen   Bourgourd  dbourgourd5f@indiegogo.com  Female       40.6.63.45
198  199       Ilise   Guerreiro       iguerreiro5i@lulu.com  Female  182.187.182.144
199  200  Philippine      Wonfar         pwonfar5j@apple.com  Female    106.83.93.196
'''

#After filtering and saving it to a new variable, you can reset index by
filt_df.reset_index(drop=True, inplace=True)

#Changing data by applying conditions
filt_df.loc[filt_df['id']>150, 'gender'] = 'Male' #In this case, it will convert all the genders where id is greater than 150 to Male
print(filt_df.tail())
'''Returned
     id  first_name  last_name                       email gender       ip_address
78  193      Shayna     Mishow        smishow5c@cpanel.net   Male    88.185.183.11
79  194      Paloma     Phelps          pphelps5d@xing.com   Male     46.63.70.142
80  196     Darleen  Bourgourd  dbourgourd5f@indiegogo.com   Male       40.6.63.45
81  199       Ilise  Guerreiro       iguerreiro5i@lulu.com   Male  182.187.182.144
82  200  Philippine     Wonfar         pwonfar5j@apple.com   Male    106.83.93.196

NOTE: TO CONVERT MULTIPLE COLUMNS WITH SAME ANSWER, YOU CAN USE:
filt_df.loc[filt_df['id']>150, ['gender', 'email']] = 'Male'

TO CONVERT MULTIPLE COLUMNS WITH MULTIPLE ANSWER (ALL GENDER TO MALE, ALL EMAIL TO XYZ@GMAIL.COM ), YOU CAN USE:
filt_df.loc[filt_df['id']>150, ['gender', 'email']] = ['Male', 'XYZ@gmail.com']
'''
#You can even describe data
#When describing data, it shows you mean, standard deviation(std), count, min, max, percentiles of each column to analyse the data
print(df.describe())
'''Returned
               id
count  200.000000
mean   100.500000
std     57.879185
min      1.000000
25%     50.750000
50%    100.500000
75%    150.250000
max    200.000000

HERE IT RETURNED ONLY FOR ID COLUMN AS IT WAS THE ONLY COLUMN INCLUDING INTEGERS AND OTHERS WERE STRING
'''

#Sorting values by a specific column
print(df.sort_values('first_name')) #Write it in the format df.sort_values('NAME OF COLUMN')
#If you want it descending (Z-A), then write df.sort_values('NAME OF COLUMN', ascending=False)
'''Returned
      id first_name   last_name                            email  gender       ip_address
16    17      Abbie  Andreaccio         aandreacciog@auda.org.au  Female     156.0.239.36
24    25    Ailbert      Cookes           acookeso@google.com.au    Male     62.153.36.70
153  154  Alejandro      Cadany             acadany49@oracle.com    Male   236.244.79.191
68    69  Alexandre    Grassick  agrassick1w@theglobeandmail.com    Male   156.216.129.52
31    32       Alie     Lakeman            alakemanv@webnode.com  Female   141.71.128.110
..   ...        ...         ...                              ...     ...              ...
3      4     Verina      Dyzart               vdyzart3@wired.com  Female    196.78.87.138
106  107     Vernon  Neubigging          vneubigging2y@fotki.com    Male   102.134.90.127
152  153      Yorke     MacLeod          ymacleod48@engadget.com    Male   226.128.197.88
104  105    Zachery      Piolli              zpiolli2w@weibo.com    Male  136.205.110.176
20    21     Zaneta     Besnard              zbesnardk@bbc.co.uk  Female     75.68.187.44

SORTS THE first_name ALPHABETICALLY (A-Z)
'''

#If you want to sort by multiple columns in descending order,then:
print(df.sort_values(['first_name', 'last_name'], ascending=False))
'''Returned
      id first_name   last_name                            email  gender       ip_address
20    21     Zaneta     Besnard              zbesnardk@bbc.co.uk  Female     75.68.187.44
104  105    Zachery      Piolli              zpiolli2w@weibo.com    Male  136.205.110.176
152  153      Yorke     MacLeod          ymacleod48@engadget.com    Male   226.128.197.88
106  107     Vernon  Neubigging          vneubigging2y@fotki.com    Male   102.134.90.127
3      4     Verina      Dyzart               vdyzart3@wired.com  Female    196.78.87.138
..   ...        ...         ...                              ...     ...              ...
31    32       Alie     Lakeman            alakemanv@webnode.com  Female   141.71.128.110
68    69  Alexandre    Grassick  agrassick1w@theglobeandmail.com    Male   156.216.129.52
153  154  Alejandro      Cadany             acadany49@oracle.com    Male   236.244.79.191
24    25    Ailbert      Cookes           acookeso@google.com.au    Male     62.153.36.70
16    17      Abbie  Andreaccio         aandreacciog@auda.org.au  Female     156.0.239.36
'''

#If you want to sort one column by ascending and second one by descending,then:
print(df.sort_values(['first_name', 'last_name'], ascending=[1, 0])) #1 means ascending and 0 means descending
'''Returned
      id first_name   last_name                            email  gender       ip_address
16    17      Abbie  Andreaccio         aandreacciog@auda.org.au  Female     156.0.239.36
24    25    Ailbert      Cookes           acookeso@google.com.au    Male     62.153.36.70
153  154  Alejandro      Cadany             acadany49@oracle.com    Male   236.244.79.191
68    69  Alexandre    Grassick  agrassick1w@theglobeandmail.com    Male   156.216.129.52
31    32       Alie     Lakeman            alakemanv@webnode.com  Female   141.71.128.110
..   ...        ...         ...                              ...     ...              ...
3      4     Verina      Dyzart               vdyzart3@wired.com  Female    196.78.87.138
106  107     Vernon  Neubigging          vneubigging2y@fotki.com    Male   102.134.90.127
152  153      Yorke     MacLeod          ymacleod48@engadget.com    Male   226.128.197.88
104  105    Zachery      Piolli              zpiolli2w@weibo.com    Male  136.205.110.176
20    21     Zaneta     Besnard              zbesnardk@bbc.co.uk  Female     75.68.187.44
'''


#Adding a column that shows full name (first name and last name combined)
df['Full_Name'] = df['first_name'] + ' ' + df['last_name']
print(df.head())
'''
   id first_name  last_name                            email  gender      ip_address         Full_Name
0   1      Naomi      Dadge         ndadge0@biblegateway.com  Female   89.157.158.46       Naomi Dadge
1   2   Meredeth     Olford             molford1@squidoo.com    Male  56.170.130.119   Meredeth Olford
2   3     Aylmar   Dimsdale             adimsdale2@slate.com    Male   50.134.200.83   Aylmar Dimsdale
3   4     Verina     Dyzart               vdyzart3@wired.com  Female   196.78.87.138     Verina Dyzart
4   5     Nancee  Longfield  nlongfield4@cargocollective.com  Female    87.33.252.24  Nancee Longfield
'''

#Deleting columns
df.drop(columns=['Full_Name'], inplace=True) #You can delete multiple columns by adding column name besides full name
#inplace = True means that it will delete the column in the original dataframe or it is simply:
#df = df.drop(columns=['Full_Name'])

print(df.head())
'''
IT IS THE ORIGINAL DATAFRAME AS LOADED PREVIOUSLY WITHOUT Full_Name Column
'''

#For example, if you want all emails to be extracted which includes google in it, you can write
print(df.loc[df['email'].str.contains('google')])
'''Returned
      id first_name last_name                    email  gender       ip_address
24    25    Ailbert    Cookes   acookeso@google.com.au    Male     62.153.36.70
48    49  Concordia     Corby       ccorby1c@google.it  Female    12.236.93.129
69    70   Jourdain  Billings    jbillings1x@google.ru    Male       95.33.70.9
74    75     Benita  Sherwill    bsherwill22@google.cn  Female   135.58.210.235
78    79      Ringo     Bilby       rbilby26@google.cn    Male      72.58.195.5
149  150      Flint    Masdon      fmasdon45@google.ca    Male  209.129.186.212
165  166   Clemence   Gilmour  cgilmour4l@google.co.uk  Female    124.89.70.103
'''

#To count the values of each individual value
print(df['gender'].value_counts())
'''
Female    110
Male       90
'''

#Dropping all the rows/columns which has no value
pdf = pdf.dropna()
