import csv
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   data=csv.reader(data)
   
   return list(data)[0]
f=open('data.csv')
print(get_first_row(f))
# Read the csv file