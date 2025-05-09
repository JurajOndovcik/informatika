subor = open("skola/(21)fahrenheit.txt", "w", encoding='utf-8')
subor.write("Prevodník z Celzia na Fahrenheita\n")
subor.write("X°C = Y°F\n")
subor.write("===================================\n")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

for i in range(-10, 101):
    fahrenheit = celsius_to_fahrenheit(i)
    subor.write(f"{i}°C = {fahrenheit:.1f}°F\n")
    print(f"{i}°C = {fahrenheit:.1f}°F")

subor.close()