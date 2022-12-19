
from fastapi import FastAPI
import pandas as pd
import os

#dfCity = pd.read_csv('./city.csv')

app = FastAPI()

@app.get("/")
def read_root():
	return {"check": "appOn"}

#@app.get("/{x}/{y}/")
#def return_place(x, y):
#	place = search_in_csv_by_coordinates(x, y)
#	return({"place": place})


@app.get("/he/{place}/")
def return_coordinates_he(place):
	x,y = search_in_csv_by_place_he(place)
	return({"x": x, "y": y})

@app.get("/en/{place}/")
def return_coordinates_en(place):
	x,y = search_in_csv_by_place_en(place)
	return ({"x": x, "y": y})


def search_in_csv_by_place_he(place):
	try:
		dfCity = pd.read_csv('./city.csv')
		rowCity = dfCity.loc[dfCity['MGLSDE_LOC'] == place]
		return rowCity.iloc[0]['X'], rowCity.iloc[0]['Y']
	except:
		return 0,0

def search_in_csv_by_place_en(place):
	try:
		dfCity = pd.read_csv('./city.csv')
		rowCity = dfCity.loc[dfCity['MGLSDE_L_4'] == place]
		return rowCity.iloc[0]['X'], rowCity.iloc[0]['Y']
	except:
		return 0,0


def search_in_csv_by_coordinates(x, y):
	try:
		dfCity = pd.read_csv('./city.csv')
		rowCity = dfCity.loc[((dfCity['X'] == x) & (dfCity['Y'] == y))]
		return rowCity.iloc[0]['MGLSDE_LOC']
	except:
		return 'Not exist'
