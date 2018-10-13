#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
class Car: #this class seems kind of awkward i need to learn python better
    def __repr__(self): #to strring
        return self.name + " is going " + str(self.current_speed) + "mph" + "and wants to go " + str(self.desired_speed) + " mph" + " and has traveled " + str(self.distance_traveled) + "miles"
    
    def __init__(self,name,distance_traveled=0,current_speed=0,current_acceleration=0,desired_speed=0,distance_to_reaction=0,step_acceleration_limit=0,total_acceleration_limit=0):
        self.name = str(name)
        self.distance_traveled = distance_traveled
        self.current_speed = current_speed
        self.current_acceleration = current_acceleration
        self.desired_speed = desired_speed
        self.distance_to_reaction = distance_to_reaction #how close a car has to be to change acceleration
        self.step_acceleration_limit = step_acceleration_limit #in one 'step' this is basically how bold the driver is
        self.total_acceleration_limit = total_acceleration_limit #how quickly the car can accelerate

    def generate_random_values(self,start_speed_limits,start_acceleration_limits,desired_speed_limits,distance_to_reaction_limits,step_acceleration_limit_limits,total_acceleration_limit_limits):
        self.current_speed = random.uniform(start_speed_limits[0],start_speed_limits[1])
        self.current_acceleration = random.uniform(start_acceleration_limits[0],start_acceleration_limits[1])
        self.desired_speed = float(random.randint(desired_speed_limits[0],desired_speed_limits[1]))
        self.distance_to_reaction = random.uniform(distance_to_reaction_limits[0],distance_to_reaction_limits[1])
        self.total_acceleration_limit = random.uniform(total_acceleration_limit_limits[0],total_acceleration_limit_limits[1])
        self.step_acceleration_limit = random.uniform(step_acceleration_limit_limits[0],step_acceleration_limit_limits[1])

    @staticmethod
    def generate_random_car(): ##this should be more sophisticated (most people want to go a certain speed )
        temp = Car(name="random_car_" + str(random.randint(1,1000000000)))
        temp.generate_random_values([1,2],[.05,.1],[1,2],[1,2],[.05,.1],[1,2])
        return temp
    def on_update():
        space
        

        


# In[11]:


#the lane holds all the cars
class Lane: 
    cars = [] #in tuples, [boolean,Car] the boolean is whether the car is on the road or not
    length = 100 #in miles
    addCarCount = 70 #placeholder
    addCarCounter = 0
    def __init__(self,number_of_cars):
        self.addRandomCars(number_of_cars)
    def update(self):
        if(self.addCarCounter == 0):
            self.addCarCounter = self.addCarCount
            for car in self.cars:
                if(car[0]==False):
                    car[0]=True
                    break
        else :
            self.addCarCounter = self.addCarCounter - 1
        for x in range(len(self.cars)):
        	car=self.cars[x]
        	if(car[0]):
	            car=car[1]
	            car.distance_traveled += car.current_speed
	            car.current_speed += car.current_acceleration
	            if(car.current_speed < car.desired_speed):
	                car.current_acceleration = car.step_acceleration_limit
	            elif(car.current_speed > car.desired_speed):
	            	car.current_acceleration = -1 * car.step_acceleration_limit
	            if(x>1):
	            	if((self.cars[x-1][1].distance_traveled - car.distance_traveled) < 10+30):
	            		car.current_acceleration = -1 * car.step_acceleration_limit
	            if(car.current_speed <= 0 and car.current_acceleration < 0 ):
	                car.current_speed = 0
    def addCar(self,aCar):
        self.cars.append([False,aCar])
    def addRandomCar(self):
        self.cars.append([False,Car.generate_random_car()])
    def addRandomCars(self,number_of_cars):
        for x in range(number_of_cars):
            self.addRandomCar()


# In[17]:


#this is rendering logic which won't be needed if we just want to simulate a certain amount of stuff
import tkinter as tk
import timer





car_size = 10
class renderLane(object): ##renders the lane and the cars in the lane
    lane_width= 50 # in pixels
    lane_length= 60 #in miles
    mainlane = Lane(30)

    def __init__(self, canvas, canvasWidth,canvasHeight, **kwargs):
        self.canvas = canvas
        self.canvas_width = canvasWidth
        self.canvas_height = canvasHeight
        print(str(self.canvas_width) + "," + str(self.canvas_height))
        self.lane_position= self.canvas_width/2.0 #mesaured from center of lane in pixels                     
        self.vy = 5
        self.renderCarList = []
        
    def draw_rectangle(self,centerX,centerY,width,height,**kwargs):
        return self.canvas.create_rectangle(centerX-width,centerY-height,centerX+width,centerY+height,**kwargs)    
    def draw_lane(self):
        self.canvas.delete("all")
        self.canvas.create_line(self.lane_position-self.lane_width/2,0 ,self.lane_position-self.lane_width/2 , self.canvas_height, fill="#476042")
        self.canvas.create_line(self.lane_position+self.lane_width/2,0 ,self.lane_position+self.lane_width/2 , self.canvas_height, fill="#476042")
        #print(self.mainlane.cars[0])
        for car in self.mainlane.cars:
            if(car[0]): #if the car is on the road
                    self.draw_rectangle(self.lane_position,self.canvas_height-car[1].distance_traveled,10,10,fill="black")
        
    def animation(self):
        self.draw_lane()
        self.mainlane.update()
        
class App(object): #preforms the animation and readouts
    
    miles_per_pixel = 1 #how many miles in a single pixel
    hours__per_second = 1 #the speed of the simulation, how many hours to simulate in one second
    delay_to_spawn = 100 #inmicroseconds
    canvas_width = 400
    canvas_height = 400
    lane = []

    def __init__(self,master,**kwargs):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=self.canvas_width,height=self.canvas_height)
        self.lane = renderLane(self.canvas,self.canvas_width,self.canvas_height)
        self.canvas.pack()
        self.master.after(0,self.animation)
        

   
    def animation(self):
            self.lane.animation()
            self.master.after(12, self.animation)
    
root = tk.Tk()
app = App(root)
root.mainloop()
print(app.lane.mainlane.cars)



