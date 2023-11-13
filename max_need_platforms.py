#max_need_platforms
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n=len(arr)
arr.sort()
dep.sort()
max_plat = 1
need_plat= 1
i=1
j=0
while (i < n and j < n):
    if (arr[i]<dep[j]):
            max_plat += 1
            i += 1
    elif (arr[i] > dep[j]):
            max_plat -= 1
            j +=1
 
        # Update result if needed
    if (max_plat > need_plat):
        need_plat = max_plat
 
print(need_plat) 
