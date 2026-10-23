weight=input("Weight in kg \n")
height=input("Height in meter \n")
w=float(weight)
h=float(height)
bmi=(w/h**2)
#print(bmi)
print("A person with weight "+str(w)+("kg and height of ")+str(h)+(" will have a BMI of ")+str(bmi))
if bmi <=18:
    print("Underweight")
elif bmi <25:
    print("Normal")
else:
    print("Over")













'''' #py -m pip install pandas openpyxl
import pandas as pd
from tkinter import Tk, filedialog

#Select a data file
root=Tk()
root.withdraw()
file_path=filedialog.askopenfilename(
    title="select your data file",
    filetypes=[
        ("Data files","*.csv *.xlsx *.xls *.sav"),
        ("All files", "*.*")
    ]
)

#import the selected file
if file_path:
    if file_path.endswith(".csv"):
        df=pd.read_csv(file_path)
    elif file_path.endswith((".xlsx", ".xls")):
        df=pd.read_excel(file_path)
    elif file_path.endswith(".sav"):
        df=pd.read_spss(file_path)

    print("File imported succesfully!")
    print("\nFirst five rows:")
    print(df.head())
    print("\nDataset shape:")
    print(df.shape)
    print("\nColumn names:")
    print(df.columns.tolist())
else:
    print("No file selected")

print(df.duplicated('Code').sum())
'''

print(df.describe())
