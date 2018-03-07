import re
f = open('price.dat', 'r')
pefile = open('ratiopelow.tmp', 'w')
pehigh = open('ratiopehigh.tmp', 'w')

for line in f:
   m = re.match("Company\t(.*)\t52.*\tEPS(.*)\t(-?.*)\tPE\t(.*)", line)
   if m:
      symbol = m.group(1)
      #print m.group(1)
      #print m.group(2)
      percent = m.group(3)
      #print m.group(3)
      pe = m.group(4)

      try:
         intpe = float(pe)
         if (intpe < 10.0):
            pefile.write (symbol + "\t\t" + pe + "\n")
         if (intpe > 30.0):
            pehigh.write (symbol + "\t\t" + pe + "\n")
      except ValueError:
         continue
         #print "ValueError" + symbol
