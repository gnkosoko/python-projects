#Gabriel Kosoko
#3/17/2025
#For my create project I am creating a vacation recomender.
countries=["Afghanistan","Albania","Algeria","American Samoa","Andorra","Angola","Anguilla","Antigua and Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Cayman Islands","Central African Republic","Chad","Chile","China","Colombia","Comoros","Cook Islands","Costa Rica","Croatia","Cuba","Curacao","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Ivory Coast","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kiribati","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Myanmar","Namibia","Nauru","Netherlands","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Niue","North Korea","North Macedonia","Northern Mariana Islands","Norway","Oman","Pakistan","Palau","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Republic of the Congo","Romania","Russia","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Martin","Saint Pierre and Miquelon","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Sint Maarten","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Korea","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Sweden","Switzerland","Syria","Tajikistan","Tanzania","Thailand","Timor Leste","Togo","Tokelau","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Turks and Caicos Islands","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","United States Virgin Islands","Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","Wallis and Futuna","Yemen","Zambia","Zimbabwe"]
population=["43844100","2771510","47435300","46029","82904","39040000","14728","94209","45851400","2952360","108147","26974000","9113570","10397700","403033","1643330","175687000","282623","8997600","11758600","422924","14814500","64555","796682","12581800","3140100","2562120","212812000","39732","466330","6714560","24074600","14390000","17848000","29879300","40126700","527326","75844","5513280","21003700","19859900","1416100000","53425600","882847","13263","5152950","3848160","10937200","185487","1370750","10609200","6002510","1184080","65871","11520500","18289900","118366000","6365500","1938430","3607000","1344230","1256170","135472000","3469","56002","933154","5623330","66650800","282465","2593130","2822090","3806670","84075100","35064300","40126","9938840","55745","117303","168999","18687900","64477","15099700","2249520","835986","11906100","11005800","9632290","398266","1463870000","285721000","92417700","47020800","5308040","84118","9517180","59146300","32711500","2837080","123103000","103989","11520700","20843800","57532500","136488","5026080","7295030","7873050","1853560","5849420","2363320","5731210","7458560","40128","2830140","680453","32740700","22216100","35977800","529676","25198800","545405","36282","5315060","1268280","131947000","113683","38341","3517100","632729","4359","38430800","35631700","54850600","3092820","12025","18346800","295333","5251900","7007500","27917800","237528000","1821","26571000","1813790","43541","5623070","5494690","255220000","17663","5589620","4571190","10762800","7013080","34576700","116787000","38140900","10411800","3235290","3115890","6484440","18908600","143997000","14569300","46922","180149","24941","5574","99924","219306","33572","240254","34566300","18932000","6689040","132779","8819790","5870750","43923","5474880","2117070","838645","19654700","64747300","51667000","12188800","47890000","23229500","51662100","639850","10656600","8967410","25620400","10786700","70545900","71619900","1418520","9721610","2608","103742","1511160","12348600","87685400","7618850","46855","9492","51384900","38980400","11346000","69551300","347276000","84138","3384690","37053400","335169","501","28516900","101599000","11194","41773900","21913900","16950800"]
continents=["Asia","Europe","Africa","Oceania","Europe","Africa","North America","North America","South America","Asia","North America","Oceania","Europe","Asia","North America","Asia","Asia","North America","Europe","Europe","North America","Africa","North America","Asia","South America","Europe","Africa","South America","North America","Asia","Europe","Africa","Africa","Asia","Africa","North America","Africa","North America","Africa","Africa","South America","Asia","South America","Africa","Oceania","North America","Europe","North America","North America","Europe","Europe","Europe","Africa","North America","North America","South America","Africa","North America","Africa","Africa","Europe","Africa","Africa","South America","Europe","Oceania","Europe","Europe","Oceania","Africa","Africa","Asia","Europe","Africa","Europe","Europe","North America","North America","Oceania","North America","Europe","Africa","Africa","South America","North America","North America","Europe","Europe","Asia","Asia","Asia","Asia","Europe","Europe","Asia","Europe","Africa","North America","Asia","Europe","Asia","Asia","Africa","Oceania","Asia","Asia","Asia","Europe","Asia","Africa","Africa","Africa","Europe","Europe","Europe","Africa","Africa","Asia","Asia","Africa","Europe","Oceania","Africa","Africa","North America","Oceania","Europe","Asia","Europe","North America","Africa","Africa","Asia","Africa","Oceania","Europe","Oceania","Oceania","North America","Africa","Africa","Oceania","Asia","Europe","Oceania","Europe","Asia","Asia","Oceania","Asia","North America","Oceania","South America","South America","Asia","Europe","Europe","North America","Asia","Africa","Europe","AsiaEurope","Africa","North America","North America","North America","North America","North America","Oceania","Europe","Africa","Asia","Africa","Europe","Africa","Africa","Asia","North America","Europe","Europe","Oceania","Africa","Africa","Asia","Africa","Europe","Asia","Africa","South America","Europe","Europe","Asia","Asia","Africa","Asia","Asia","Africa","Oceania","Oceania","North America","Africa","Asia","Asia","North America","Oceania","Africa","Europe","Asia","Europe","North America","North America","South America","Asia","Oceania","Europe","South America","Asia","Oceania","Asia","Africa","Africa"]
fahrenheit=["55.47 ","54.39 ","74.48 ","81.28 ","46.89 ","71.19 ","81.88 ","80.96 ","61.34 ","46.08 ","84.51 ","71.69 ","45.39 ","55.33 ","78.04 ","81.84 ","78.28 ","79.90 ","45.41 ","51.21 ","78.26 ","82.44 ","71.01 ","50.68 ","69.37 ","50.63 ","71.76 ","77.79 ","80.06 ","80.51 ","52.43 ","86.72 ","68.92 ","81.34 ","76.64 ","24.75 ","72.55 ","82.08 ","77.85 ","81.73 ","48.90 ","45.66 ","77.00 ","74.71 ","76.48 ","76.69 ","53.53 ","78.46 ","83.12 ","68.02 ","47.48 ","48.02 ","83.28 ","80.29 ","76.19 ","70.57 ","73.65 ","77.41 ","76.39 ","79.93 ","43.41 ","69.15 ","74.05 ","43.88 ","81.10 ","76.42 ","36.43 ","52.97 ","75.74 ","77.36 ","83.08 ","48.22 ","49.26 ","81.79 ","64.67 ","55.71 ","−1.62 ","79.68 ","82.06 ","74.57 ","53.76 ","78.55 ","82.36 ","79.02 ","76.91 ","76.50 ","52.70 ","35.33 ","76.89 ","78.73 ","65.01 ","73.31 ","49.51 ","49.37 ","69.78 ","55.44 ","80.24 ","78.64 ","53.20 ","54.09 ","68.09 ","44.80 ","77.14 ","81.99 ","79.36 ","36.77 ","75.49 ","44.37 ","59.81 ","54.28 ","77.81 ","73.06 ","45.59 ","45.28 ","50.04 ","72.75 ","72.79 ","79.48 ","82.60 ","84.58 ","68.11 ","82.42 ","83.88 ","73.99 ","70.36 ","51.60 ","55.49 ","33.93 ","49.87 ","78.35 ","64.65 ","75.94 ","74.88 ","68.81 ","82.09 ","50.88 ","72.84 ","50.83 ","78.58 ","82.47 ","81.14 ","77.05 ","44.56 ","51.42 ","81.68 ","35.98 ","81.75 ","70.48 ","82.22 ","68.07 ","78.08 ","76.53 ","75.06 ","68.13 ","79.29 ","47.80 ","60.53 ","77.07 ","82.44 ","76.53 ","50.32 ","25.18 ","68.05 ","81.45 ","80.60 ","81.88 ","42.30 ","79.11 ","81.64 ","55.09 ","76.08 ","78.69 ","84.02 ","52.52 ","80.76 ","79.77 ","81.82 ","81.88 ","47.89 ","49.75 ","78.66 ","80.51 ","64.81 ","54.00 ","82.35 ","55.53 ","81.05 ","82.31 ","79.84 ","37.81 ","43.65 ","65.75 ","38.93 ","73.26 ","80.33 ","76.23 ","81.19 ","83.68 ","77.02 ","79.79 ","68.95 ","52.99 ","61.99 ","79.32 ","83.52 ","73.85 ","48.69 ","82.71 ","48.63 ","49.03 ","80.56 ","64.35 ","55.51 ","75.99 ","59.36 ","78.28 ","76.62 ","81.14 ","77.97 ","72.01 ","71.42"]
filtered_list0=[]
filtered_list1=[]
filtered_list2=[]
filtered_list3=[]
filtered_list4=[]
filtered_list5=[]
filtered_list6=[]
filtered_list7=[]
filtered_list8=[]
filtered_list9=[]
filtered_list10=[]
filtered_list11=[]
filtered_list12=[]
filtered_list13=[]
filtered_list14=[]
filtered_list15=[]

#Functions

def gettingPopulation():#this function gives you 4 list and one of these lists will have the countries based on the population size you wanted. It takes a lot more tries to get the the full list you wanted.
    for i in range(len(countries)):
        number = population[i]
        size = input("What population size are you looking for: tiny, small, medium, or large?")
        if size == "tiny" and int(number) < 1000:
            filtered_list0.append(countries[i])
        elif size == "small" and 1001 <= int(number) <= 1000000:
            filtered_list1.append(countries[i])
        elif size == "medium" and 1000001 <= int(number) <= 1000000000:
            filtered_list2.append(countries[i])
        elif size == "large" and int(number) > 1000000001:
            filtered_list3.append(countries[i])
        print(filtered_list0)
        print(filtered_list1)
        print(filtered_list2)
        print(filtered_list3)

def gettingFahrenheit(): #this function gives you 5 list and one of these lists will have the countries based on the average temperature you wanted. It takes a lot more tries to get the the full list you wanted.
    for i in range(len(countries)):
        degrees = fahrenheit[i]
        temperature = input("What average temperature are you looking for: freezing, cold, brisky, warm or hot?")
        if temperature == "freezing" and float(degrees) <= 15:
            filtered_list4.append(countries[i])
        elif temperature == "cold" and 16. <= float(degrees) <= 32.:
            filtered_list5.append(countries[i])
        elif temperature == "brisky" and 33. <= float(degrees) <= 65.:
            filtered_list6.append(countries[i])
        elif temperature == "warm" and 66. <= float(degrees) <= 80.:
            filtered_list7.append(countries[i])
        elif temperature == "hot" and float(degrees) > 81.:
            filtered_list8.append(countries[i])
        print(filtered_list4)
        print(filtered_list5)
        print(filtered_list6)
        print(filtered_list7)
        print(filtered_list8)

def gettingContinent(continent, continent1, continent2, continent3, continent4, continent5, continent6):#this function gives you 5 list and one of these lists will have the countries based on the population you wanted. It takes a lot more tries to get the the full list you wanted.
    for i in range(len(countries)):
        land = input("What continent are you looking for: Asia, North America, South America, Europe, Oceania, Africa, or AsiaEurope(if your are planning on going to Russia)?")
        if land in continents:
            if land == continent:
                if continents[i] == continent:
                    filtered_list9.append(countries[i])
            elif land == continent1:
                if continents[i] == continent1:
                    filtered_list10.append(countries[i])
            elif land == continent2:
                if continents[i] == continent2:
                    filtered_list11.append(countries[i])
            elif land == continent3:
                if continents[i] == continent3:
                    filtered_list12.append(countries[i])
            elif land == continent4:
                if continents[i] == continent4:
                    filtered_list13.append(countries[i])
            elif land == continent5:
                if continents[i] == continent5:
                    filtered_list14.append(countries[i])
            elif land == continent6:
                if continents[i] == continent6:
                    filtered_list15.append(countries[i])
            print(filtered_list9)
            print(filtered_list10)
            print(filtered_list11)
            print(filtered_list12)
            print(filtered_list13)
            print(filtered_list14)
            print(filtered_list15)
        else:
            print(f"No countries found on the continent '{land}'.")
            return

def main_menu(): #this function gives you 4 options, the first are the function from above and the last two are extra
    while True:
        print("Vacation Menu")
        print("1. Get vacation spot via population ")
        print("2. Get vaction spot via temperature")
        print("3. Get Vacation spot via contienent")
        print("4. Display all vaction spots")
        print("5. Exit")
        choice = input("Please select an option (1-5): ")
        if choice == "1":
            gettingPopulation()
        elif choice == "2":
            gettingFahrenheit()
        elif choice == '3':
            gettingContinent('Asia', 'North America', 'South America', 'Europe', 'Oceania', 'Africa', 'AsiaEurope')
        elif choice == '4':
            print(countries)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")

#Main
main_menu()
#gettingPopulation()
#gettingFahreneit()
#gettingContinent('Asia', 'North America', 'South America', 'Europe', 'Oceania', 'Africa', 'AsiaEurope')

#https://worldpopulationreview.com/countries
#https://worldpopulationreview.com/country-rankings/list-of-countries-by-continent
#https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature
