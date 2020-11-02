"""Main interface for the Library user"""

"""All the necessary imports"""

import pandas as pd 
import matplotlib.pyplot as plt
from gsheets import Sheets as s
import time, os, fnmatch, shutil




"""Obtaining Google cloud credentials to access the desired file path (google-sheet path).
Follow seperate instuction to obtain the credentials from google
Download client_secret.json"""

def read_data_from_url(gcp_credential_path,file_url):
	sheets = s.from_files(gcp_credential_path, './storage.json')

	imported_sheet= sheets.get(file_url)
	
	return imported_sheet


def plot_sheet_data(imported_sheet):
	"""Converting sheet to csv and csv to dataframe """
	
	imported_sheet.sheets[0].to_csv('greendeck.csv', encoding='utf-8', dialect='excel')

	df=imported_sheet.sheets[0].to_frame()

	a=df.iloc[0:,1]
	b=df.iloc[0:,0]

	out_df = pd.concat([b, a], axis=1)

	out_df.plot(x='timestamp', y='average_sales', figsize=(20,5))
	
	b1=min(b)
	b2=max(b)
	a1=min(a)
	a2=max(a)
	plt.xlim(b1,b2)
	plt.ylim(a1,a2)
	plt.title("average-sales vs timestamp")

	t = time.localtime()
	timestamp = time.strftime('%b-%d-%Y_%H%M%S', t)
	out_file_name = f'output_{timestamp}.png'
	
	plt.savefig(out_file_name)
	plt.show()


def create_chart(gcp_credential_path,file_url):
	imported_data= read_data_from_url(gcp_credential_path,file_url)
	plot_sheet_data(imported_data)

