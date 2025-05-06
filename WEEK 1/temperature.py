temp = float(input("Enter temperature: "))
unit = input("Convert to (C/F): ").strip().upper()

if unit == 'F':
    converted = (temp * 9/5) + 32
    print(f"{temp}°C = {converted:.2f}°F")
elif unit == 'C':
    converted = (temp - 32) * 5/9
    print(f"{temp}°F = {converted:.2f}°C")
else:
    print("Invalid option. Use 'C' or 'F'.")
