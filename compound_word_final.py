my_file=open('Input_02-1.txt','r')
content=my_file.read()
content_list=content.split('\n')
# content_list.remove('')# This line to be used when there is a newline after after every word in txt file
sorted_len_list=sorted(content_list,key=len,reverse=True)
a=0
count=0
def recursion(arg,val,count):
  a = len(arg)
  new_list=[]
  new_list1=[]
  for item in sorted_len_list:
    if item[0]==arg[0]:
      new_list.append(item)
  if count==0:
    new_list.pop(0)
  if new_list:
    for item in new_list:
      matches = arg.startswith(item)
      if (matches):
        new_list1.append(item)
        break
    y=len(new_list1[0])
    arg = arg[y:]
    a=a-y
    if a==0:
      print(f'The longest compounded word is {sorted_len_list[index]}') 
      exit()
    else:
      count+=1
      recursion(arg,val,count)
for index, value in enumerate(sorted_len_list):
  count=0
  recursion(value,index,count)


  

