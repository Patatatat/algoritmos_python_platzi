voted = {}
def check_voter(name):
  if voted.get(name):
    print ("kick them out!")
  else:
    voted[name] = True
    print ("let them vote!")

print(check_voter('Patatatat'))
print(check_voter('Patatatat'))