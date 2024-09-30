# from chat import chatlocal
import run_model as slm
import csv  
def predictheaders(file_path):
  rows=""
  with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        rows = [next(reader) for _ in range(2)]
  rows_str = '\n'.join([', '.join(row) for row in rows])
  datatypes=slm.pipe("What are the types of data in this dataset? eg. email, phone number, name, address etc. Return only the headings and not the data itself"+rows_str, max_new_tokens=150)
  return datatypes

def maskobfcsv(file_path):
    print("Masking the data in the csv file")
    return "Masked the data in the csv file"