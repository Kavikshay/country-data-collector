import requests
import json

def fetch(key):
	try:
		url ='https://api.restcountries.com/countries/v5'
		headers={'Authorization': f'Bearer {key}'}
		params={'limit':100,'offset':0}
		response=requests.get(url,headers=headers,params=params,timeout=10)
		data=response.json()
		country_list=[]
		country=data["data"]["objects"]
		for i in country:
			if i["names"]["common"]:
				name=i["names"]["common"]
			else:
				name="no country name"
			if i["capitals"]:
				capital=i["capitals"][0]["name"]
			else:
				capital="no capital in data"
			if i["region"]:
				region=i["region"]
			else:
				region="no region"
			if i["currencies"]:
				currencies=i["currencies"][0]["name"]
			else:
				currencies="no currencie in data"
			if i["population"]:
				population=i["population"]
			else:
				population="no population data"
			country_data={
			"name":name,
			"capital":capital,
			"region":region,
			"currencie":currencies,
			"population":population
			}
			country_list.append(country_data)
		print("fetch successfully")
		return country_list
		print("\ndata fetched successfully\n")
	except requests.exceptions.Timeout:
	   	print("Request timed out. Please try again.")
	except requests.exceptions.ConnectionError:
	   	print("No internet connection.")
	except requests.exceptions.RequestException:
	   	print("There was a problem with the API request.")
	except (KeyError, TypeError):
	  	  print("Unexpected data received from the API.")

def load_json():
	try:
		with open("country.json","r")as file:
			data=json.load(file)
		for i in data:
			print(f"countrys name:",i["name"])
			print("capital:",i['capital'])
			print("region:",i["region"])
			print("currencie:",i["currencie"])
			print("population:",i["population"])
			print()
	except FileNotFoundError:
		print(" The file does not exist yet. Please fetch and save the data first!")
	except json.JSONDecodeError:
		print("The JSON file is corrupted or improperly formatted.")
	
def convert_json(country):
	try:
		country_list=country			
		with open("country.json","w")as file:
				json.dump(country_list,file,indent=4)
		print("data saved successfully ")
		
	except requests.exceptions.Timeout:
	   	print("Request timed out. Please try again.")
	except requests.exceptions.ConnectionError:
	   	print("No internet connection.")
	except requests.exceptions.RequestException:
	   	print("There was a problem with the API request.")
	except (KeyError, TypeError):
	  	  print("Unexpected data received from the API.")
	except FileNotFoundError:
			print(" The file does not exist yet. Please fetch and save the data first!")
	except json.JSONDecodeError:
        	print("The JSON file is corrupted or improperly formatted.")

	  	  
def all(country):
	try:
		print(f"total countrys:{len(country)}\n")
		count=0
		for i in country:
			print(count+1)
			print(f"countrys name:",i["name"])
			print("capital:",i['capital'])
			print("region:",i["region"])
			print("currencie:",i["currencie"])
			print("population:",i["population"])
			count+=1
			print()
	except requests.exceptions.Timeout:
	   	print("Request timed out. Please try again.")
	except requests.exceptions.ConnectionError:
	   	print("No internet connection.")
	except requests.exceptions.RequestException:
	   	print("There was a problem with the API request.")
	except (KeyError, TypeError):
	  	  print("Unexpected data received from the API.")
		
						
						
	
def country(name,headers,params):   
	try:
		url=f"https://api.restcountries.com/countries/v5/names.common/{name}"
		response=requests.get(url,headers=headers,params=params,timeout=10)
		data = response.json()
		if data["data"]["objects"][0]:
			country=data["data"]["objects"][0]
		else:
			print("wrong country name")
		if country["names"]["common"]:
			name=country ["names"]["common"]
			if country["capitals"]:
				capital=country["capitals"][0]["name"]
			else:
				capital="no caption found"
			if country["region"]:
				region=country["region"]
			else:
				region="region not found"
			if country["population"]:
				pop=country["population"]
			else:
				pop="population not found "
			if country["currencies"]:
				currencie=country["currencies"][0]["name"]
			else:
				currencie="currencie not found "
		else:
			print("not data found for",name)
		print()
		print(f"country name:{name}")
		print(f"capital:{capital}")
		print(f"region:{region}")
		print(f"currencie:{currencie}")
		print(f"population:{pop}")
		print()
	except requests.exceptions.Timeout:
	   	print("Request timed out. Please try again.")
	except requests.exceptions.ConnectionError:
	   	print("No internet connection.")
	except requests.exceptions.RequestException:
	   	print("There was a problem with the API request.")
	except (KeyError, TypeError):
	  	  print("Unexpected data received from the API.")

def mane():
	key=input("enter your key:")
	if not key.strip():
		print("key can be empty")
	while True:	
		print("=====COUNTRY DATA MENU=====")
		headers={'Authorization': f'Bearer {key}'}
		
		params={'limit':100,'offset':0}
		print("1. Fetch country data from API")
		print("2. Display all countries")
		print("3. Search for a country")
		print("4. Save data to JSON")
		print("5. Load saved JSON data")
		print("6. Exit")
		try:
			a=int(input("Enter your choice:"))
			if a==6:
				print("thank you visit again")
				break
			elif a==3:
				name=input("enter country name:")
				if not name.strip():
					print("the can't me empty")
					continue
				else:
					country(name,headers,params)
			
			elif a==1:
				result=fetch(key)
				if result is not None:
					country=result			
			elif a==2:
				all(country)
			elif a==4:
				convert_json(country)
			elif a==5:
				load_json()
			else:
				print("wrong number enter again")
					
		except ValueError:
			print("enter number not text")
			
			
mane()				
			
	