# python string method 
text = "hello world"; 

# Capitalize method 
x= text.capitalize(); 
print(x); 


# Convert to upper case 
x= text.upper(); 
print(x); 

# Convert to lower case 
x= text.lower()
print(x); 

# getting length of string 
x= len(text); 
print(x); 

# replacing parts of string 
a= "hello world"; 
x= a.replace("world", "Rezaul"); 
print(x); 

# define how many word replace 
c= "hello world world"; 
x= c.replace("world", "rejaul", 1); 
print(x); 


# check if a value present in a string
text = "my name is rejaul karim"; 
x= "rejaul" in text; 
print(x); 

y= "rejaul" not in text; 
print(y); 