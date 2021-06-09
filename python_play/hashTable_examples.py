import csv
def get_nyc_weather_dict():    
    with open('nyc_weather.csv', mode='r') as csv_file:    
        csv_reader = csv.reader(csv_file, delimiter =",")
        skip_header = True
        nyc_temp = {}
        for line in csv_reader:
            if skip_header:
                skip_header = False
                continue
            nyc_temp[line[0]] = int(line[1])
    return nyc_temp

def get_nyc_weather_list():    
    with open('nyc_weather.csv', mode='r') as csv_file:    
        csv_reader = csv.reader(csv_file, delimiter =",")
        skip_header = True
        nyc_temp = []
        for line in csv_reader:
            if skip_header:
                skip_header = False
                continue
            nyc_temp.append(int(line[1]))
        return nyc_temp
            
def get_avg_temp():
    temp_list = get_nyc_weather_list()
    avg_temp = 0
    week = 7
    for i in range(week):
        avg_temp+=temp_list[i]
    return avg_temp/week

def get_max_temp():
    temp_list = get_nyc_weather_list()
    return max(temp_list)

print("Avg temp of the first week was ",get_avg_temp())
print("Max temp of the first 10 days was ",get_max_temp())
print("Temp on Jan 9th is",get_nyc_weather_dict()['Jan 9'])
print("Temp on Jan 4th is",get_nyc_weather_dict()['Jan 4'])



