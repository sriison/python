#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
for int in range(1500,2701):
    #print(int)
    if (int%7 == 0) and (int%5 == 0):
        print(int)