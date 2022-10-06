# example of recursion(while)

# def look_for_key(main_box):
#   pile = main_box.make_a_pile_to_look_through()
#   empty = False
#   while pile is not empty:
#     box = pile.grab_a_box()
#     for item in box:
#       if item.is_a_box():
#         pile.append(item)
#       elif item.is_a_key():
#         print("found the key!")

# example of recusion calling itself

# def look_for_key(box):
#  for item in box:
#    if item.is_a_box():
#      look_for_key(item)
#    elif item.is_a_key():
#      print ('found the key!')

# def countdown(i):
#  print(i)
#  if i <= 1:
#    #print("happy new year!")
#    return
#  else:
#    countdown(i-1)

#countdown(10)

#Stack:

# def greet2(name):
  # print ("how are you, " + name + "?")

# def bye():
  # print("ok bye!")

# def greet(name):
  # print("hello, " + name + "!")
  # greet2(name)
  # print("getting ready to say bye...")
  # bye()

#greet(name="Andres")

# Stack with recursion:

def fact(x):
    print(x)
    if x == 1:
     return 1
    else:
     return x * fact(x-1)

fact(x= 15)