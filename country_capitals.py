
capital={"USA": "Washington, D.C.",
"France": "Paris",
"Germany": "Berlin",
"Japan": "Tokyo",
"UK": "London"}

country=input("Enter one of the following countries: USA,France, Germany,Japan, UK to see the capital: " )
 
if country in capital:
    print(f"The capital of {country} is {capital[country]}")







