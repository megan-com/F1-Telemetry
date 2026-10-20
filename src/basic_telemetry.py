import fastf1 #importing the python library fastf1
from fastf1 import plotting #importing the plotting module from fastf1
import matplotlib.pyplot as plt #importing the matplotlib library for plotting

fastf1.Cache.enable_cache('cache') #enabling the cache for fastf1 to store data locally

#picking a session that i want to analyse! im going to do my favourite race: baku 2024!
year = int(input("Enter the year: ")) #getting the year from the user
race = input("Enter the race name: ") #getting the race name from the user
session_type = input("Enter the session type (Practice (FP1, FP2, FP3), Qualifying (Q), Race (R)): ") #getting the session type from the user
session = fastf1.get_session(year, race, session_type) #setting the session to the one that the user has inputted
print("Loading session...")
session.load(telemetry=True, weather=True)
print("Session loaded successfully!")


#picking a driver (in this case piastri) and getting his lap data
driver_code = input("Enter the driver code for driver 1: ") 
driver_laps = session.laps.pick_driver(driver_code)
fastest_lap = driver_laps.pick_fastest() #picking the fastest lap of the driver

#getting the telemetry data for said fastest lap
car_data = fastest_lap.get_car_data()

#i want to now compare oscars fastest quali lap to charles' pole lap so i need to get all of charles' lap data too
driver_code2 = input("Enter the driver code for driver 2: ") 
driver_laps2 = session.laps.pick_driver(driver_code2)
fastest_lap2 = driver_laps2.pick_fastest() #picking the pole lap
car_data2 = fastest_lap2.get_car_data() #getting the telemetry data for charles' pole lap


#setting up the plotting style
plotting.setup_mpl()


#now onto the actual analysis! im going to plot speed, throttle and brake data!

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(12,6)) #creating a new plot so i can draw on the data
fig.suptitle(f'{driver_code} vs {driver_code2} - {session.event["EventName"]} {session.event.year} - {session.name} Session', fontsize=16) #setting the title of the graph to the session name and year (updates automatically)

#speed data plotting
ax1.plot(car_data['Time'], car_data['Speed'], label=f'{driver_code}', color='blue') #plotting speed data over a lap in blue
ax1.set_title('Speed') #setting the title of the graph to speed
ax1.set_ylabel('Speed in km/h') #setting the y-axis label to speed in km/h
ax1.set_xlabel('Time in seconds') #setting the x-axis label to time in seconds

#speed data plotting for the second driver
ax1.plot(car_data2['Time'], car_data2['Speed'], label=f'{driver_code2}', color='red') #plotting speed data over a lap in orange


#throttle data plotting
ax2.plot(car_data['Time'], car_data['Throttle'], label=f'{driver_code}', color='blue') #plotting throttle data over a lap in green
ax2.set_title('Throttle') #setting the title of the graph to throttle
ax2.set_ylabel('Throttle in %') #setting the y-axis label to throttle in %
ax2.set_xlabel('Time in seconds') #setting the x-axis label to time in seconds

ax2.plot(car_data2['Time'], car_data2['Throttle'], label=f'{driver_code2}', color='red') #plotting throttle data over a lap in purple


#brake data plotting
ax3.plot(car_data['Time'], car_data['Brake'], label=f'{driver_code}', color='blue') #plotting brake data over a lap in red
ax3.set_title('Brake') #setting the title of the graph to brake
ax3.set_ylabel('Brake in %') #setting the y-axis label to brake in %
ax3.set_xlabel('Time in seconds') #setting the x-axis label to time in seconds

ax3.plot(car_data2['Time'], car_data2['Brake'], label=f'{driver_code2}', color='red') #plotting brake data over a lap in brown


#show legend, essentially a little box that shows what each line represents, making the graph readable!
ax1.legend()
ax2.legend()
ax3.legend()

#opening the graph in a new window so i can see it and analyse it!
plt.tight_layout() #adjusting the layout of the graph so it looks nice and neat
plt.show()