class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())

rainy = []
for i in range(n):
    date, day, weather = input().split()
    
    if weather == 'Rain':
        rainy.append(Weather(date, day, weather))
    

idx = 0
for i in range(1, len(rainy)):
    if rainy[idx].date > rainy[i].date:
        idx = i
        

print(f"{rainy[idx].date} {rainy[idx].day} {rainy[idx].weather}")