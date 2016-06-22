from pyllist import dllist, dllistnode


def heavy_hitters(e):
   k = int(1.0 / e - 1)
   table = {}
   inner = dllist()
   for i in range(k):
       inner.insert([None, 0])
   outer = dllist([inner])
   min_count = 0

   with open("Data.txt") as data:
       for line in data:
           print line
           if not table.has_key(line):
               if outer.first.value.first.value[1] == min_count:
                   victim = outer.first.value.popleft()
                   if table.has_key(victim[0]) :
                       table.pop(victim[0], None)
                   outer.first.value.insert([line, min_count])
                   table[line] = [outer.first, outer.first.value.last]

           if table.has_key(line):
               a = table.get(line)
               a[1].value[1] += 1
               if a[0].next:
                   if a[0].next.value.first.value[1] == a[1].value[1]:
                       tl = a[0].next
                       tn = a[0].value.remove(a[1])
                       tl.value.appendleft(tn)
                       table[line] = [tl, tl.value.first]
                       if a[0].value.size == 0:
                           outer.remove(a[0])

                   else:
                       tn = a[0].value.remove(a[1])
                       new_inner = dllist()
                       new_inner.appendleft(tn)
                       outer.insert(new_inner, after=a[0])
                       table[line] = [a[0].next, a[0].next.value.first]
                       if a[0].value.size == 0:
                           outer.remove(a[0])
               else:
                   tn = a[0].value.remove(a[1])
                   new_inner = dllist()
                   new_inner.appendleft(tn)
                   outer.insert(new_inner, after=a[0])
                   table[line] = [a[0].next, a[0].next.value.first]
                   if a[0].value.size == 0:
                       outer.remove(a[0])
           else:
               min_count += 1

   return table

hh = heavy_hitters(1 / 10.0)
for key in hh:
   print key
