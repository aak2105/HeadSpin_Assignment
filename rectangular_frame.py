
"""
Assignment Qstn 2

Write a function that takes a list of strings and 
prints them one per line in a rectangular frame

"""

def rectangular_frame(list_words):
  width = max(len(word) for word in list_words)
  print("*" * (width+2))

  for word in list_words:
    print("*" + word + " " * ((width) - len(word)) + "*")
  
  print("*" * (width+2))

list1 = ["Hello","world","in","a","frame"]
rectangular_frame(list1)


