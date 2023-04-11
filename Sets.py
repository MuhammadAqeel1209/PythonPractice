#SET is data type that replace the list because set cannot allow multiple same object in one sett
#represented by the curly bracket and set cannot replaceable any value
#do not order maintain in sets
"""
sett = {1,2,1,3,4,1,5,1,8,7,1}
print(sett)

info = {1,2,"Red",1,True,"Black",2,2.45}
print(info)

Aqeel = set()
print(type(Aqeel))

for values in info:
    print(values)
    """

#--------------------------------------METHOD OF SETS------------------------------------------
s1 = {1,2,3,5,6}
s2  = {3,6,7}
s3 = {1,4,8}
s4 = {1,2,3,4,5,6,7}

#--------------------------------------UNION AND UPDATE------------------------------------------
#Update -->1st set update with values of second update
"""
print(s1.union(s2))
s1.update(s2)
print(s1,s2)
s2.update(s1)
print(s1,s2)
"""
 
 #---------------------------------INTERSECTION AND INTERSECTION UPDATE------------------------------
"""
print(s1.intersection(s2))
print(s2.intersection_update(s1))
"""

#-----------------------------------------SYMETERIC DIFFERENCE-----------------------------------------
#SYSMETRIC DIFFERENCE  (A – B) ∪ (B – A) Not common
"""
print(s1.symmetric_difference(s2))
"""

#--------------------------------------------------DIFFERENCE-----------------------------------------
"""
print(s1.difference(s2))
"""

#------------------------------------- ---------Isdisjoint ----------------------------------------------
#Disjoint set --> intersection of set is null
"""
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s3))
"""

#---------------------------------------------------issuperset-----------------------------------------
#Superset --> some element part of other set
"""
print(s2.issuperset(s1))
print(s4.issuperset(s2))
"""

#---------------------------------------------------issubset-----------------------------------------
"""
print(s2.issubset(s1))
print(s2.issubset(s4))
"""

#---------------------------------------------------Add----------------------------------------------
"""
s2.add(10)
print(s2)
"""

#---------------------------------------------------Remove-----------------------------------------
"""
s2.remove(10)
print(s2)
"""

#---------------------------------------------------Pop--------------------------------------------
#Pop remove random value 
"""
s5 = s4.pop()
print(s4)
print(s5)
"""

#---------------------------------------------------del Keyword-------------------------------------------
#del keyword used to delete the full entire set
"""
del s2
print(s2)
"""

#---------------------------------------------------clear-------------------------------------------
"""
s2.clear()
print(s2)
"""