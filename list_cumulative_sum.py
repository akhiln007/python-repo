def cumulative_all(number_list):
 for num in range(1,len(number_list)):
  number_list[num]=number_list[num]+number_list[num-1]
 return number_list  
  

print(cumulative_all([4, 3, 6]))