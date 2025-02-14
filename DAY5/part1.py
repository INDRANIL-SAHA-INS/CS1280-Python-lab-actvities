
mobile={
    "brand":"Nokia",
    "model":"s20",
    "screen size":6.6
}
for key ,value in mobile.items():
    print(f"{key}:{value}",end="\n")
    
mobile["battery"]="7999mh"

for key ,value in mobile.items():
    print(f"{key}:{value}",end="\n")
    
print()
i=1
names={}
while True:
    x=input("Enter your name: ")
    names["student"+str(i)]=x
    i=i+1
    y=input("do you want to continue(y/n): ").strip().lower()
    if y=="n":
        break


for key ,value in names.items():
    print(f"{key}:{value}",end="\n")
