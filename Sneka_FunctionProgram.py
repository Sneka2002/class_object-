class and objects
 
 class flight:
      def_init_(self, flight_no,source, destination,fare):
              self.flight_no=flight_no
              self.source=source
              self.destination=destination
              self.fare=fare
info=flight (19943450,"Bangalore","Mumbai",10000)
class F_name:
     def fun(self):
            print("SNEKA Airlines")
            print("**Flight details**")
F=F_name()
F.fun()
print("Flight Number: ",info.flight_no)
print("From : ",info.source)
print("To : ",info.destination)
print("Fare : ",info.fare)
