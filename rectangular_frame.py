
"""
Assignment Qstn 2

Write a function that takes a list of strings and 
prints them one per line in a rectangular frame

"""

#"""
def rectangular_frame(list_words):
  width = max(len(word) for word in list_words)
  print("*" * (width+2))

  for word in list_words:
    print("*" + word + " " * ((width) - len(word)) + "*")
  
  print("*" * (width+2))
#"""

"""
redefined function for adding a space before and after 
each word in the list for better readability
"""
"""
def rectangular_frame(list_words):
  width = max(len(word) for word in list_words)
  print("*" * (width+4)) # 2 extra * needed

  for word in list_words:
    print("*" + " " + word + " " * ((width+1) - len(word)) + "*") #additional space before and after word
  
  print("*" * (width+4)) # 2 extra * needed
"""

list1 = ["Hello","world","in","a","frame"]
rectangular_frame(list1)


