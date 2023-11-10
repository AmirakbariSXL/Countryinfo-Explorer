# Import the CountryInfo module
from countryinfo import CountryInfo

# Get the country name from the user
name = input("Enter the country name: ")

# Create an instance of the CountryInfo class
country = CountryInfo(name)

# Print the country information
print(f"Capital: {country.capital()}")
print(f"Currencies: {country.currencies()}")
print(f"Languages: {country.languages()}")
print(f"Borders: {country.borders()}")
print(f"Provinces: {country.provinces()}")
print(f"Area: {country.area()} square kilometers")
print(f"Calling codes: {country.calling_codes()}")
print(f"Capital Latitudes and Longitudes: {country.capital_latlng()}")
print(f"Timezones: {country.timezones()}")
print(f"Population: {country.population()}")
print(f"Other names: {country.alt_spellings()}")
