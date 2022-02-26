#+---------------------+
#| hw3b - Isaiah Grace |
#+---------------------+

#---Part B---

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

# ask for input measure (F/C/K), output measure, temperature reading
# output new temp
# TODO: follow up on KFC sponsorship

input_measure = input("What measure does your temp use? ['K'/'F'/'C']: ")

while input_measure not in ('K', 'F', 'C'):
    print("ERR: Please enter 'K', 'F', or 'C'.")
    input_measure = input("What measure does your temp use? ['K'/'F'/'C']: ")

#---

output_measure = input("What measure do you want to convert to? ['K'/'F'/'C']: ")

while output_measure not in ('K', 'F', 'C'):
    print("ERR: Please enter 'K', 'F', or 'C'.")
    output_measure = input("What measure do you want to convert to? ['K'/'F'/'C']: ")

#---

while True:
    try:
        input_temp = float(input("What temp do you want to convert? (Decimal): "))
    except:
        print("ERR: Please enter temp in decimal format.")        
        continue
    break

if (input_measure, output_measure) == ('K', 'F'):
    print(f"Your new temp is {KelvinToFahrenheit(input_temp)}.")

if (input_measure, output_measure) == ('K', 'C'):
    print(f"Your new temp is {KelvinToCelsius(input_temp)}.")

if (input_measure, output_measure) == ('F', 'K'):
    print(f"Your new temp is {FahrenheitToKelvin(input_temp)}.")

if (input_measure, output_measure) == ('F', 'C'):
    print(f"Your new temp is {FahrenheitToCelsius(input_temp)}.")

if (input_measure, output_measure) == ('C', 'K'):
    print(f"Your new temp is {CelsiusToKelvin(input_temp)}.")

if (input_measure, output_measure) == ('C', 'F'):
    print(f"Your new temp is {CelsiusToFahrenheit(input_temp)}.")

if input_measure == output_measure:
    print("Your temp is still", input_temp, end=".\n")


