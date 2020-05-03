import csv
from matplotlib import pyplot as plt
import matplotlib.ticker as plticker
import numpy as np
#Citations
#https://matplotlib.org/3.1.1/api/markers_api.html
#https://matplotlib.org/tutorials/index.html
#https://matplotlib.org/3.1.1/api/ticker_api.html
#
filename = "IHME_USA_LIFE_EXPECTANCY_1985_2010.csv"
def worst_county(year):
    #parse through data
    with open('Life/IHME_USA_LIFE_EXPECTANCY_1985_2010.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter =',')
        lifeavg = 1000000
        counteravg = 0
        state = ''
        county = ''
        for row in reader:
            if row[3] == str(year):
                counteravg = (float(row[4]) + float(row[7]))/2
                if counteravg < lifeavg:
                    lifeavg = counteravg
                    state = row[0]
                    county = row[1]
        return(state,county)
        
def plotdata(state,county):
    with open('Life/IHME_USA_LIFE_EXPECTANCY_1985_2010.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter =',')
        countyfemalelist = []
        statefemalelist = []
        nationalfemalelist = []
        countymalelist = []
        statemalelist = []
        nationalmalelist = []
        years = [1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
        for row in reader:
            if (row[0] == state and row[1] == county):
                countyfemalelist.append(float(row[4]))
                statefemalelist.append(float(row[6]))
                nationalfemalelist.append(float(row[5]))
                countymalelist.append(float(row[7]))
                statemalelist.append(float(row[9]))
                nationalmalelist.append(float(row[8]))
        
        
    
    plt.plot(years,countyfemalelist, color = 'magenta', label = 'life expectancy female(county)')
    plt.plot(years,statefemalelist, color = 'magenta', label = 'life expectancy female(state)', marker = 'v')
    plt.plot(years,nationalfemalelist, color = 'magenta', label ='life expectancy female(national)', marker = 'x')
    plt.plot(years,countymalelist, color = 'blue', label = 'life expectancy male(county)', marker = 's')
    plt.plot(years,statemalelist, color = 'blue', label = 'life expectancy male(state)', marker = '>')
    plt.plot(years,nationalmalelist, color = 'blue', label ='life expectancy male(national)', marker = '2')

    
    
    plt.title("{0} , {1}: Life expectancy".format(county,state))
    plt.legend(loc ='lower right')
    ax = plt.axes()
    ax.set_xlabel('Years')
    ax.set_ylabel('Life expectancy')
    tick_spacing = 1
    ax.yaxis.set_major_locator(plticker.MultipleLocator(tick_spacing))
    plt.savefig('state_county.png')
    plt.show()

   


    

if __name__ == "__main__":
    state,county =  worst_county(2010)  
    plotdata(state,county)