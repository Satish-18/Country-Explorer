import requests
urls = 'https://restcountries.com/v3.1/all'
response = requests.get(urls)

if response.status_code == 200:
  data = response.json()

  for country in data:
    #Getting the name of the country
    country_name = country['name']['common'] 

    #Getting the official name of the country
    country_official_name = country['name']['official'] 

    #Getting population 
    total_people = country['population'] 

    #Getting total population
    total_area = country['area']

    #Getting time zone
    timezones = ','.join(country['timezones'])
    
    #Getting region
    region = country['continents'][0]

    #Getting sub-region
    if 'subregion' in country:
        sub_region = country['subregion']
    else:
      sub_region = 'Not available'
    subregion = sub_region
    

    #Getting map
    street_maps = country['maps']['openStreetMaps']

    #Getting geographic status
    if country['landlocked'] == True:
      landlock = 'Yes'
    else:
      landlock = 'No'
    geographic_status = landlock  

    #Getting UN membership information   
    if 'unMember' in country and country['unMember'] == True:
      un_member = 'Yes'
    else:
      un_member = 'No'
    Member_of_un = un_member
 

    #Getting the information of the flag of particular country
    flag_info = country['flags']
    if 'alt' in flag_info:
      flag_img = flag_info['svg']
      flag_alt = flag_info['alt']
    else:
      flag_img = flag_info['svg']
      flag_alt = 'none'
   
    alt = flag_img
    img = flag_alt

    #Getting capital city name
    if 'capital' in country:
      # city = country['capital']
      capital = ','.join(country['capital'])
    else:
      capital = 'No information'
  
    capital_city = capital 


    #Getting shared boarder
    if 'borders' in country:
      neighbour = ','.join(country['borders'])
    else:
      neighbour = "No data available or don't shared a boarder"
    shared_boarder = neighbour



    #Getting currency details
    if 'currencies' in country:
      currency_detail = country['currencies']
      curr = list(currency_detail.values())[0]['name']
    else:
      curr = 'No data found'
    currency = curr
 



  