# IB Labs Calculator Menu
modeoptions = ['Plain Calculator','Variables']
print("""This is the homepage for the IB Labs Calculator.
Enter in your criteria:""")
for i in range(len(modeoptions)):
    print(i,modeoptions[i])
def limit(mode, minimum=0, maximum=3):
#Limits input of mode to 0-1
  return max(min(mode, maximum), minimum)
  limit(input)

"""if mode == 0:
    #insertmode0

elif mode == 1:
    #insertmode1
elif mode == 2
    #insertmode2
elif mode == 3
    #insertmode3
else
    print(Invalid Input)"""
    
