"""
author -Maruti Bhosale
date -12-11-2020
time -20:00
package -functional_programs
Statement - finding weather condition using temperature and wind speed

"""

import math


class WindChill:

    def findWeatherCondition(self):   # finding weather condition
        """
        :return: Weather condition value as per formula
        """
        weather = 35.74+(0.6215*self.temp)+(0.4275*self.temp-35.75)*math.pow(self.windSpeed, 0.16)
        return weather

    def inputTempAndWindSpeed(self):  # taking input from user for temperature and wind speed
        try:
            self.temp = float(input("Enter temperature in fahrenheit: "))
            self.windSpeed = float(input("Enter wind speed in miles per our: "))
        except ValueError:
            print("not valid float type")

        if self.temp > 50:
            print("Temperature should be less then 50 fahrenheit")
            self.inputTempAndWindSpeed()
        if 3 > self.windSpeed > 120:
            print("Wind speed should be between 3 to 120")
            self.inputTempAndWindSpeed()


if __name__ == "__main__":
    windchill = WindChill()
    windchill.inputTempAndWindSpeed()
    weather = windchill.findWeatherCondition()
    print("Weather condition value is: ", weather)
