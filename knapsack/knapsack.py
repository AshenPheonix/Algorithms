#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def sort_on(item):
  return item['vplb']

def sort_final(item):
  return item.index

def knapsack_solver(items, capacity):
  final=[]
  vplb=[]
  for item in items:
    vplb.append({"vplb":item.value/item.size,"item":item})
  
  vplb.sort(key = sort_on,reverse=True)
  
  for item in vplb:
    print('vplb:', item['vplb'],'item:',item['item'])

  for item in vplb:
    if item['item'].size < capacity - sum([tested.size for tested in final]):
      final.append(item['item'])
  

  temp = [item for item in final]
  while capacity - sum([tested.size for tested in final]) > 0 and len(temp)>0:
    print('culling', temp)
    removed = temp.pop()
    for item in vplb:
      if item['item'] == removed:
        vplb.remove(item)
        break
    for item in vplb:
      if item['item'].size < capacity - sum([tested.size for tested in temp]):
        print('adding temp')
        temp.append(item['item'])

  if sum([item.value for item in temp]) > sum([item.value for item in final]):
    final = temp

  final.sort(key=sort_final)

  return {
    "Value":sum([item.value for item in final]),
    "Chosen":[item.index for item in final]
  }
  

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')