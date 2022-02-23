#+---------------------+
#| hw3b - Isaiah Grace |
#+---------------------+

#---Part B---

# TODO: add input and prompts

def CelsiusToFahrenheit(temp):
    # F = C * (9/5) + 32
    return temp * (9/5) + 32

def CelsiusToKelvin(temp):
    # K = C + 273.15
    return temp + 273.15

def FahrenheitToCelsius(temp):
    # C = (F - 32) * (5/9)
    return (temp - 32) * (5/9)

def FahrenheitToKelvin(temp):
    # K = ((F - 32) * (5/9)) + 273.15
    return ((temp - 32) * (5/9)) + 273.15

def KelvinToCelsius(temp):
    # C = K - 273.15
    return temp - 273.15

def KelvinToFahrenheit(temp):
    # F = (K - 273.15) * (9/5) + 32
    return (temp - 273.15) * (9/5) + 32

