print("Welcome to Kenya tax car calulator")

car_year = int(input("Enter registration date of the car: \n"))
csrp = int(input("Enter CSRP value of the car: \n"))
car_age = 2025 - car_year
depreciation_rate = 0.15

if 1 < car_age <= 2:
    depreciation_rate = 0.2  # 20%
elif 2 < car_age <= 3:
    depreciation_rate = 0.3  # 30%
elif 3 < car_age <= 4:
    depreciation_rate = 0.4  # 40%
elif 4 < car_age <= 5:
    depreciation_rate = 0.5  # 50%
elif 5 < car_age <= 6:
    depreciation_rate =  0.55  # 55%
elif 6 < car_age <= 7:
    depreciation_rate = 0.60  # 60%
elif 7 < car_age <= 8:
    depreciation_rate = 0.65  # 65%
else:
    print("Car is too old for depreciation calculation")
    exit()


car_value = csrp * (1 - depreciation_rate)
print(f"The value of the car after depreciation is: {car_value}")

import_duty = car_value * 0.25  # 25% import duty
excise_duty = (car_value * 0.20) + import_duty # 20% excise duty
vat = 0.16 * (car_value + import_duty + excise_duty)  # 16% VAT
idf = (0.0225 * car_value)  # IDF 2.25%

port_charge_SGR = 120000
verification_fee = 15000.00 
interpol = 15000.00 
mss_levy = 2000.00 
radiation = 1000.00 
ntsa_sticker  = 800 
idf_fee = 2000.00 
local_transport = 25000 
agents_fee = 100000

print(f"Import Duty: {import_duty}")
print(f"Excise Duty: {excise_duty}")
print(f"VAT: {vat}")
print(f"IDF: {idf}")
print(f"Port Charge SGR: {port_charge_SGR}")
print(f"Verification Fee: {verification_fee}")
print(f"Interpol: {interpol}")
print(f"MSS Levy: {mss_levy}")
print(f"Radiation: {radiation}")
print(f"NTSA Sticker: {ntsa_sticker}")
print(f"IDF Fee: {idf_fee}")
print(f"Local Transport: {local_transport}")
print(f"Agents Fee: {agents_fee}")

print(f"Total Cost: {import_duty + excise_duty + vat + idf + port_charge_SGR + verification_fee + interpol + mss_levy + radiation + ntsa_sticker + idf_fee + local_transport + agents_fee}")