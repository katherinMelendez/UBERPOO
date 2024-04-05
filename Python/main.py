from car import car
from account import account
from uberX import uberX
from user import user

if __name__ == "__main__":
    print ("Inicializando informavion de auto")
    print ("Car")
    car = car("JHY432", account ("Katherine Melendez", "ASD12345", "katherdez24@mail.com", "8765""))
    print(vars(car))
    print(vars(car.driver)
    
    print("UberX"))
    uberX = UberX( "KH8769", account("Isaias", "KJS12345", "isaias@gmail", "654398"), "hyundai", "atos")
    print(vars(uberX))
    print(vars(uberX.driver)
    
    print("User")
    user = user("camila palacios", "RGEH321G", "camilapalacios@gmail", "2765"
    print(vars(user))))))