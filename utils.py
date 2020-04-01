import json, requests
from flask import Flask
from flask_cors import CORS

reset="Day are reset at 2:00 GMT"

def get_data():
    
    try:
        res=requests.get("https://corona.lmao.ninja/countries")
        print("End")
        json_data=json.loads(res.text)
        return json_data
    except:
        return None
        

def get_world_data():

    countries_data=get_data()

    if not countries_data:
        return None

    world_data={}

    cases=0
    deaths=0
    todayCases=0
    todayDeaths=0
    recovered=0

    for country in countries_data:

        cases += int(country['cases'])
        deaths += int(country['deaths'])
        todayCases += int(country['todayCases'])
        todayDeaths += int(country['todayDeaths'])
        recovered += int(country['recovered'])
        updated=int(int(country['updated'])/1000)


    world_data['cases']=cases
    world_data['deaths']=deaths
    world_data['todayCases']=todayCases
    world_data['todayDeaths']=todayDeaths
    world_data['recovered']=recovered
    world_data['updated']=updated

    return world_data


def get_continent_data(cont_iso2="AF", if_world_data=False):

    countries_data=get_data()
    if not countries_data:
        return None
    
    cont_data={}

    cont_iso_file = open("./data_utils/iso2_continent_country.json")
    cont_iso = json.loads(cont_iso_file.read())
    cont_iso_file.close()

    continent_name_fr_file = open("./data_utils/iso2_continent_french.json", encoding="Utf-8")
    continent_name_fr = json.loads(continent_name_fr_file.read())
    continent_name_fr_file.close()

    continent_name_en_file = open("./data_utils/iso2_continent_english.json")
    continent_name_en = json.loads(continent_name_en_file.read())
    continent_name_en_file.close()

    try:
        a=continent_name_fr[cont_iso2]
    except:
        res={}
        res['message']="Unknow Continent"
        return json.dumps(res)
    
    cont_data['name_fr']=continent_name_fr[cont_iso2]
    cont_data['name_en']=continent_name_en[cont_iso2]

    cont_data['iso2']=cont_iso2
    print(cont_data)

    
    cases=0
    deaths=0
    todayCases=0
    todayDeaths=0
    recovered=0
    updated=0

    for country in countries_data:
        if country['countryInfo']['iso2']:
            if cont_iso[country['countryInfo']['iso2']] == cont_iso2:

                cases += int(country['cases'])
                deaths += int(country['deaths'])
                todayCases += int(country['todayCases'])
                todayDeaths += int(country['todayDeaths'])
                recovered += int(country['recovered'])
                updated=int(int(country['updated'])/1000)


    cont_data['cases']=cases
    cont_data['deaths']=deaths
    cont_data['todayCases']=todayCases
    cont_data['todayDeaths']=todayDeaths
    cont_data['recovered']=recovered
    cont_data['updated']=updated

    

    if if_world_data:
        world_data = get_world_data()
        if not world_data:
            return None

        per_cases=round((cont_data['cases']/world_data['cases'])*100)
        per_deaths=round((cont_data['deaths']/world_data['deaths'])*100)

        if world_data['todayCases'] :
            per_todayCases=round((cont_data['todayCases']/world_data['todayCases'])*100)
        else:
            per_todayCases=0

        if world_data['todayDeaths']:
            per_todayDeaths=round((cont_data['todayDeaths']/world_data['todayDeaths'])*100)
        else:
            per_todayDeaths=0
            
        
        
        per_recovered=round((cont_data['recovered']/world_data['recovered'])*100)

        cont_data['per_cases']=per_cases
        cont_data['per_deaths']=per_deaths
        cont_data['per_todayCases']=per_todayCases
        cont_data['per_todayDeaths']=per_todayDeaths
        cont_data['per_recovered']=per_recovered
    

    return cont_data

def get_country_data(country_iso2="", if_cont_data=False):

    countries_data=get_data()

    country_data={}

    cont_iso_file = open("./data_utils/iso2_continent_country.json")
    cont_iso = json.loads(cont_iso_file.read())
    cont_iso_file.close()

    country_names_fr_file = open("./data_utils/iso2_country_french.json", encoding="Utf-8")
    country_names_fr = json.loads(country_names_fr_file.read())
    country_names_fr_file.close()

    country_names_en_file = open("./data_utils/iso2_country_english.json")
    country_names_en = json.loads(country_names_en_file.read())
    country_names_en_file.close()

    continent_name_fr_file = open("./data_utils/iso2_continent_french.json", encoding="Utf-8")
    continent_name_fr = json.loads(continent_name_fr_file.read())
    continent_name_fr_file.close()

    d="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/"

    country_list=[]
    
    for iso2 in country_names_fr:
        a=[]
        a.append(iso2)
        a.append(country_names_fr[iso2])
        a.append(d+iso2.lower()+".png")
        country_list.append(a)
    country_data["countries_list"]=country_list

    continent_name_en_file = open("./data_utils/iso2_continent_english.json")
    continent_name_en = json.loads(continent_name_en_file.read())
    continent_name_en_file.close()

    country_data['name_fr']=country_names_fr[country_iso2]
    country_data['name_en']=country_names_en[country_iso2]
    country_data["iso2"]=country_iso2
    
    country_data['continent_fr']=continent_name_fr[cont_iso[country_iso2]]
    country_data['continent_en']=continent_name_en[cont_iso[country_iso2]]

    country_data['continent_iso2']=cont_iso[country_iso2]

    cases=0
    deaths=0
    todayCases=0
    todayDeaths=0
    recovered=0
    updated=0
    
    for country in countries_data:

        if country['countryInfo']['iso2'] == country_iso2:

            cases = int(country['cases'])
            deaths = int(country['deaths'])
            todayCases = int(country['todayCases'])
            todayDeaths = int(country['todayDeaths'])
            recovered = int(country['recovered'])
            flag = country['countryInfo']['flag']
            updated=int(int(country['updated'])/1000)
            

    country_data['cases']=cases
    country_data['deaths']=deaths
    country_data['todayCases']=todayCases
    country_data['todayDeaths']=todayDeaths
    country_data['recovered']=recovered
    country_data['flag']=flag
    country_data['updated']=updated


    if if_cont_data:

        cont_data=get_continent_data(cont_iso[country_iso2])
        if not cont_data:
            return None

        per_cases=round((country_data['cases']/cont_data['cases'])*100)
        per_deaths=round((country_data['deaths']/cont_data['deaths'])*100)

        if cont_data['todayCases'] :
            per_todayCases=round((country_data['todayCases']/cont_data['todayCases'])*100)
        else:
            per_todayCases=0

        if cont_data['todayDeaths']:
            per_todayDeaths=round((country_data['todayDeaths']/cont_data['todayDeaths'])*100)
        else:
            per_todayDeaths=0
            
        per_recovered=round((country_data['recovered']/cont_data['recovered'])*100)

        country_data['per_cases']=per_cases
        country_data['per_deaths']=per_deaths
        country_data['per_todayCases']=per_todayCases
        country_data['per_todayDeaths']=per_todayDeaths
        country_data['per_recovered']=per_recovered


    return country_data





            

    
