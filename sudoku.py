oggrid = []
with open("/Users/nathanyao/dev/git/sudoku/sudoku.in") as fr:
  for line in fr:
    sline = line.strip()
    sline = sline.split(",")
    oggrid.append(sline)
#print(oggrid)
pregrid1 = []
pregrid2 = []
grid = {}
count_y = 0
def no_rep_digit(l):
    l_new = []
    digits = []
    for num in l:
        if not any([(digit in digits) for digit in str(num)]):
            l_new.append(num)
            digits.extend([digit for digit in str(num)])
        else:
            digits.extend([digit for digit in str(num)])
    return l_new

def posibility_checker(grid,x,y):
  can_not_be = []
  whichone = []
  can_be= [100000,10000000]
  for val in range(1,10):
    #print(val)
    if grid[x,val] != []:
      can_not_be.append(grid[x,val])
    if grid[val,y] != []:
      can_not_be.append(grid[val,y])

  #print(can_not_be)
  #print(x,y)

  if x<4 and y<4:
    for xval in range(1,4):
      for yval in range(1,4):
        if grid[xval,yval] != []:
          whichone.append(1)
          can_not_be.append(grid[xval,yval])
          #print(grid[xval,yval],xval)
  elif x>=4 and x<=6 and y<4:
    for xval in range(4,7):
      for yval in range(1,4):
        if grid[xval,yval] != []:
          #print(grid[xval,yval],xval)
          whichone.append(2)
          can_not_be.append(grid[xval,yval])
  elif x>=7 and y<4:
    for xval in range(7,10):
      for yval in range(1,4):
        if grid[xval,yval] != []:
          #print(grid[xval,yval],xval)
          whichone.append(3)
          can_not_be.append(grid[xval,yval])
  elif y>=4 and y<=6 and x<4:
    for xval in range(1,4):
      for yval in range(4,7):
        if grid[xval,yval] != []:
          whichone.append(4)
          #print(grid[xval,yval],xval)
          can_not_be.append(grid[xval,yval])
  elif x>=4 and x<=6 and y>=4 and y<=6:
    for xval in range(4,7):
      for yval in range(4,7):
        if grid[xval,yval] != []:
          whichone.append(5)
          #print(grid[xval,yval],xval)
          can_not_be.append(grid[xval,yval])
  elif y>=4 and y<=6 and x>=7:
    for xval in range(7,10):
      for yval in range(4,7):
        if grid[xval,yval] != []:
          whichone.append(6)
          #print(grid[xval,yval],xval)
          can_not_be.append(grid[xval,yval])
  elif y>=7 and x<=3:

    for xval in range(1,4):
      for yval in range(7,10):
        if grid[xval,yval] != []:
          #print(grid[xval,yval],xval)
          can_not_be.append(grid[xval,yval])
  elif y>=7 and x>=4 and x<=6:
    for xval in range(4,7):
      for yval in range(7,10):
        if grid[xval,yval] != []:
          whichone.append(8)
          #print(grid[xval,yval],xval)
          can_not_be.append(grid[xval,yval])
  elif y>=7 and x>=7:
    for xval in range(7,10):
      for yval in range(7,10):
        whichone.append(grid[xval,yval])
        if grid[xval,yval] != []:
          #print(grid[xval,yval],xval)
          can_not_be.append(grid[xval,yval])
  can_not_be = no_rep_digit(can_not_be)
  if len(can_not_be) == 8:
    can_be = []
    for one_t_nine in range(1,10):
      #print(grid[xval,yval],xval)
      if one_t_nine not in can_not_be:
        can_be.append(one_t_nine)
        print(f"whichone: {whichone}")
        print(can_not_be)
    print(can_be)
  return(can_be)

epty = 0
for index in oggrid:
  #print(index)
  count_y += 1
  count_x = 0
  for index2 in index:
    count_x+= 1
    #print(index2)
    if index2 == "0":
      grid[count_x,count_y] = []
      epty += 1
    else:
      grid[count_x,count_y] = int(index2)

#print(grid)
not_full = True
fill = 0
while not_full == True:
  for x in range(1,10):
    for y in range(1,10):
      if grid[x,y] != [] :
        #print(grid[x,y])
        continue
      else:
        #print(grid[x,y])
        pos = posibility_checker(grid,x,y)
        #print(pos)
        if len(pos) == 1:
          grid[x,y] = pos[0]
          print(x,y)
          print(grid)
          fill+=1
          print(fill)
          if fill == epty:
            not_full == False
        else:
          continue
  




































'''
def qmaker(lst):
    count = 0
    local = 0
    localfind = 0
    for ele in lst:
      localfind += 1
      if count >= 2:
        return (False,-1)
      if (ele == -1):
        local = localfind
        count = count + 1
    if count == 1:
      return (True,local)
    else:
      return (False,-1)


def not_their(list_of_ele,empty_local):
  if 1 not in list_of_ele:
    list_of_ele.pop(empty_local)
    list_of_ele.insert(empty_local,1)
  if 2 not in list_of_ele:
    list_of_ele.pop(empty_local)
    list_of_ele.insert(empty_local,2)
  if 3 not in list_of_ele:
    list_of_ele.pop(empty_local)
    list_of_ele.insert(empty_local,3)
  if 4 not in list_of_ele:
    list_of_ele.pop(empty_local)
    list_of_ele.insert(empty_local,4)
  if 5 not in list_of_ele:
    list_of_ele.pop(empty_local)
    list_of_ele.insert(empty_local,5)
  if 6 not in list_of_ele:
    list_of_ele.pop(empty_local)
    list_of_ele.insert(empty_local,6)
  if 7 not in list_of_ele:
    list_of_ele.pop(empty_local)
    list_of_ele.insert(empty_local,7)
  if 8 not in list_of_ele:
    list_of_ele.pop(empty_local)
    list_of_ele.insert(empty_local,8)
  if 9 not in list_of_ele:
    list_of_ele.pop(empty_local)
    list_of_ele.insert(empty_local,9)
def colom_check(colom_list):
  (bul,pos) = qmaker(colom_list)
  if bul == True:
    not_their(colom_list,pos)
    gate2 = False
full = True

while full == True:
  gate1 = True
  for line in grid:
    (bul,pos) = is_there_8(line)
    if bul == True:
      not_their(line,pos)
      gate1 = False



  if gate1 == True:
    for line in grid:
      colom_check(line[0])
      colom_check(line[1])
      colom_check(line[2])
      colom_check(line[3])
      colom_check(line[4])
      colom_check(line[5])
      colom_check(line[6])
      colom_check(line[7])
      colom_check(line[8])
'''