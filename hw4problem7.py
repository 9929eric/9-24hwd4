breakfast = ["Froot Loops", "Wheaties", "Cap'n Crunch"]
def cereal_time(breakfast):
  for cereal in breakfast:
     last_letter = cereal[-1]
     if last_letter == "s":
      print(cereal,"are yummy!")
     else:
       print(cereal,"is yummy!")
cereal_time(breakfast)
