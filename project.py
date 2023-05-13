import requests
import sys

'''
In this program , the program asked the user about the information user wants (1 for weather or 2 for location)
whatever user choices it will show which type of specefic-information they want like
{if user choose 'weather' then what specefic info user want temparature or humidity or etc..}
then returns it and prints it in main func

def check is checking that input is in range or not
def output is printing the output in readable format
def weather is taking input of city and specefic-info and returning output of specific weather info what user wants
def location is taking input of city and specefic-info and returning output of specific location info what user wants

*****NOTE: please read category.txt file to see what specefic informations is avilable for user

'''

def main():
    check()
    output()

def output():
    while True:
      print("\nNOTE: if there are two different places with same name please put{,countryname}  Example:- [cambridge,US] for USA Address and [cambridge,UK] for England\n")
      city=input("Enter your city: ")
    
      print("\nWhich type of Information do you want\ntype '1' for weather info or type '2' for Location info or type '0' to exit\n")
  
      c = int(input("Enter your choice: "))




      if c == 1 :
        try:
          print("\n!!!! please visit category.txt file to see avilable category !!!\n" )
          category=input("Enter your Category(i.e temp,visibility,humidity etc): ").lower()
          
          if category == "temp":
            op=[]
            h = weather(city,category)
            op.append(h)
          
            k=((5*op[0])-160)/9 #formula c/5 = (f-32)/9
            sys.exit(f"\nthe temprature of {city} is {op[0]} °F or {k:.02f} °C")
          elif category == "feelslike":
            op=[]
            h = weather(city,category)
            op.append(h)
          
            k=((5*op[0])-160)/9 #formula c/5 = (f-32)/9
            sys.exit(f"\nFeeling Temparature of {city} is {op[0]} °F or {k:.02f} °C")
            
          elif category == "windspeed":
            op=[]
            h = weather(city,category)
            op.append(h)
            sys.exit(f"\nthe windspeed of {city} is {op[0]} km/h")
            
          elif category == "winddir":
            op=[]
            h = weather(city,category)
            op.append(h)

            if op[0] >0 and op[0]<=75:
              sys.exit(f"\nthe wind direction of {city} is {op[0]} NorthEast")
            if op[0] >75 and op[0]<=120:
              sys.exit(f"\nthe wind direction of {city} is {op[0]} East")
            if op[0] >120 and op[0]<=195:
              sys.exit(f"\nthe wind direction of {city} is {op[0]} SouthEast")
            if op[0] >175 and op[0]<=210:
              sys.exit(f"\nthe wind direction of {city} is {op[0]} South")
            if op[0] >210 and op[0]<=260:
              sys.exit(f"\nthe wind direction of {city} is {op[0]} South West")
            if op[0] >260 and op[0]<=310:
              sys.exit(f"\nthe wind direction of {city} is {op[0]} West")
            if op[0] >310 and op[0]<=359:
              sys.exit(f"\nthe wind direction of {city} is {op[0]} North West")
          elif category == "pressure":
            op=[]
            h = weather(city,category)
            op.append(h)
            sys.exit(f"\nthe wind pressure of {city} is {op[0]} Hg") 

          elif category == "humidity":
            op=[]
            h = weather(city,category)
            op.append(h)
            sys.exit(f"\nthe Humidity of {city} is {op[0]} %")
          elif category == "cloud cover":
            op=[]
            h = weather(city,category)
            op.append(h)
            sys.exit(f"\nthe cloud cover of {city} is {op[0]} %")

          elif category == "visibility":
            op=[]
            h = weather(city,category)
            op.append(h)
            sys.exit(f"\nthe Visibility of {city} is {op[0]} km")

          elif category == "datetime":
            op=[]
            h = weather(city,category)
            op.append(h)
            sys.exit(f"\nthe Date of {city} is {op[0]}")
          

         
          
          else:
            op=[]
            h = weather(city,category)
            op.append(h)
            sys.exit(f"\n today the {category} of {city} is {op[0]}")

        except requests.exceptions.JSONDecodeError:
          print("\nInvalid city Name please type the correct name")
        except KeyError:
          print("\nInvalid Category please visit category.txt file to see avilable commands\n")
        




          
      elif c == 2 :
        try:
          print("\n!!!! please visit category.txt file to see avilable category !!!\n" )
          category=input("Enter your Category(i.e latitude,resolvedAddress,  etc): ")
          
          op=[]
          h = location(city,category)
          op.append(h)
          sys.exit(f"\nthe {category} of {city} is {op[0]}")
        except requests.exceptions.JSONDecodeError:
          print("\nInvalid city Name please type the correct name")
        except KeyError:
          print("\nInvalid Category please visit category.txt file to see avilable commands\n")

     
        
        
      
      elif c == 0:
          sys.exit("Thanks for your visit 😊\n")
  
      else:
        print("\nInvalid Choice entered retype again\n")



def check():
  
    if len(sys.argv) >1:
      sys.exit("Too many arguments entered")
    elif len(sys.argv) <1:
      sys.exit("Too little arguments entered")

  



def weather(city,category):
  
    api_url = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?key=DSF33KQVH5KMGANS5XXAZA3RD")
    r= api_url.json()
    current= (r['days'][0][category])
    return current
  
 
      


def location(city,category):
    api_url = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?key=DSF33KQVH5KMGANS5XXAZA3RD")
    r= api_url.json()
    
    current= (r[category])
    return current



if __name__ == "__main__":
  main()
