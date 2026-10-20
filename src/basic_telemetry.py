import fastf1 #importing the python library fastf1
from fastf1 import plotting #importing the plotting module from fastf1
import matplotlib.pyplot as plt #importing the matplotlib library for plotting

fastf1.Cache.enable_cache('cache') #enabling the cache for fastf1 to store data locally

#picking a session that i want to analyse! im going to do my favourite race: baku 2024!
session = fastf1.get_session(2024, 'Baku', 'R') #getting the race session for Baku 24
session.load() #loading the session data

#picking a driver (in this case piastri) and getting his lap data
driver_code = 'PIA' #driver code for Oscar Piastri
driver_laps = session.laps.pick_driver(driver_code)
fastest_lap = driver_laps.pick_fastest() #picking the fastest lap of the driver

#getting the telemetry data for said fastest lap
car_data = fastest_lap.get_car_data()

#setting up the plotting style
plotting.setup_mpl()

#now onto the actual analysis! im going to plot speed, throttle and brake data!

fig, ax1 = plt.subplots(figsize=(12,6)) #creating a new plot so i can draw on the data
fig, ax2 = plt.subplots(figsize=(12,6))
fig, ax3 = plt.subplots(figsize=(12,6))

#speed data plotting
ax1.plot(car_data['Time'], car_data['Speed'], label='Speed in km/h', color='blue') #plotting speed data over a lap in blue

#throttle data plotting
ax2.plot(car_data['Time'], car_data['Throttle'], label='Throttle in %', color='green') #plotting throttle data over a lap in green

#brake data plotting
ax3.plot(car_data['Time'], car_data['Brake'], label='Brake in %', color='red') #plotting brake data over a lap in red

#show legend, essentially a little box that shows what each line represents, making the graph readable!
ax1.legend()
ax2.legend()
ax3.legend()

#opening the graph in a new window so i can see it and analyse it!
plt.show()