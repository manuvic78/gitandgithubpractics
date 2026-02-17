
weight= float(input('what is yor weigth?:  '))
list=('1. mercury, 2. venus, 3. mars, 4. jupiter, 5. saturn, 6. uranus, 7. neptune')
print (list)
planet_select=int(input('what is your planet? (SELECT 1-7): '))


 
if planet_select==1:
   destination_weight= weight * 0.38
   print (f'your weigth in mercury is {destination_weight}')
elif planet_select==2:
   destination_weight= weight * 0.91
   print (f'your weigth in venus is {destination_weight}')
elif planet_select==3:
   destination_weight= weight * 0.38
   print (f'your weigth in mars is {destination_weight}')
elif planet_select==4:
   destination_weight= weight * 2.34
   print (f'your weigth in jupiter is {destination_weight}')
elif planet_select==5:
   destination_weight= weight * 1.06
   print (f'your weigth in saturn is {destination_weight}')
elif planet_select==6:
   destination_weight= weight * 0.92
   print (f'your weigth in uranus is {destination_weight}')
elif planet_select==7:
   destination_weight= weight * 1.19
   print (f'your weigth in neptune is {destination_weight}')    

else:
   print ('wrong input')