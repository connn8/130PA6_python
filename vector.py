"""This module contains the Vector class, along with methods that can be used on 
   Vectors and/or sequences.
   Imports Failure from misc module 
   #author: CSE130 Staff
"""

from misc import Failure

class Vector(object):
  """Vector class creates Vector objects and defines methods for Vectors."""

  def __init__(self,arg):
    """Initiates a Vector object

    Args:
      arg (int, long, or sequence): if int or long =  length of vector else data contained in vector
  
    Raises:
      ValueError: if length being passed to Vector is negative
      TypeError: if arg is of wrong type

    """
    if isinstance(arg,(int,long)):
      if (arg >= 0):
        self.length = arg
        self.vecList = []
        for i in range(arg):
          self.vecList.append(0.0)
      else:
        raise ValueError("Vector length cannot be negative")
    else:
      try:
        self.length = len(arg)
        self.vecList = [x for x in arg]
      except TypeError:
        print "Argument must be of type int, long, or a sequence"

  def __repr__(self):
    """Returns a string representation of a Vector."""
    return "Vector(" + str(self.vecList) + ")" 

  def __len__(self):
    """Returns the length of a Vector."""
    return self.length

  def __iter__(self):
    """Returns an object that can iterate over the elements of a Vector"""
    for n in self.vecList:
      yield n

  def __add__(self,other):
    """Adds elements of a Vector and another Vector or sequence.

    Args:
      other (Vector or sequence): contains elements we are adding to self

    Raises:
      Failure: if length of self and other are not the same

    Returns: 
      New Vector containing summed data of self and other

    """
    if not(len(self) == len(other)):
      raise Failure("Length of both arguments must be the same") #LengthError??
    else: 
      addList = []
      i = 0
      for x in other:
        addList.append(self.vecList[i] + x)
        i+=1
    return Vector(addList)

  def __radd__(self,other):
    """Same as __add__ but gets called on if right element is not type Vector.

    Args:
      other (Vector or sequence): contains elements we are adding to self

    Raises:
      Failure: if length of self and other are not the same

    Returns: 
      New Vector containing summed data of self and other

    """
    if not(len(self) == len(other)):
      raise Failure("Length of both arguments must be the same") #LengthError??
    else:
      addList = []
      i = 0
      for x in other:
        addList.append(self.vecList[i] + x)
        i+=1
    return Vector(addList)

  def __iadd__(self,other):
    """Same as __add__ but updates the data field of the calling Vector.

    Args:
      other (Vector or sequence): contains elements we are adding to self

    Raises:
      Failure: if length of self and other are not the same

    Returns: 
      Original Vector containing summed data of itself and other

    """
    if not(len(self) == len(other)):
      raise Failure("Length of both arguments must be the same") #LengthError??
    else:
      addList = []
      i = 0
      for x in other:
        addList.append(self.vecList[i] + x)
        i+=1
    self.vecList = addList
    return self


  def dot(self,other):
    """Computes dot product of elements of self and other

    Args:
      other (Vector or sequence): contains elements used to compute dot product

    Raises:
      Failure: if length of self and other are not the same

    Returns: 
      sum: Dot product of elements of self and other

    """
    if not(len(self) == len(other)):
      raise Failure("Length of both arguments must be the same") #LengthError??
    else:
      sum = 0
      i = 0
      for x in other:
        sum+=(self.vecList[i] * x)
        i+=1
    return sum

  def __getitem__(self,key):
    """Accesses an element(s) of the Vector based on the index or slice provided.
    
    Args:
      key (int or slice): index or range of element(s) we are trying to access

    Raises:
      IndexError: if index (key) is out of range 
      TypeError: if index (key) is not type int

    Returns: 
      Element(s) of Vector at given index/slice

    """
    try:
      return self.vecList[key]
    except IndexError:
      print "Index is out of range" 
    except TypeError:
      print "Inappropiate type for index"
  
  def __setitem__(self,key,value):
    """Sets an element(s) of the Vector to a certain value based on the index or slice provided.
    
    Args:
      key (int or slice): index or range of element(s) we are trying to set
      value : new value we are trying to set

    Raises:
      ValueError: if setting the new value will change the length of Vector
      IndexError: if index (key) is out of range 
      TypeError: if index (key) is not type int

    Returns: 
      Self with its updated data field

    """
    try:
      #creates a new list and sets value to check if it would be changing length
      tempList = self.vecList[:]
      tempList[key] = value
      if not(len(tempList)==len(self.vecList)):
        raise ValueError("Cannot change length of Vector")
      else:
        self.vecList = tempList
        return self
    except IndexError:
      print "Index is out of range"
    except TypeError:
      print  "Inappropiate type for index"
  
  def __eq__(self,other):
    """Checks if a Vector is equal to another Vector.

    Args:
      other (Vector or sequence) : what we are checking self against

    Note:
      If a Vector is compared to a non-vector sequence, they are never equal

    Returns:
      True if equal, False if not

    """
    if (isinstance(other,Vector)):
      return self.vecList == other.vecList
    else: return False

  
  def __ne__(self,other):
    """Checks if a Vector is not equal to another Vector.

    Args:
      other (Vector or sequence) : what we are checking self against

    Note:
      If a Vector is compared to a non-vector sequence, they are never equal

    Returns:
      True if not equals, False if equal

    """
    if (isinstance(other,Vector)):
     return (self.vecList != other.vecList)
    else: return True

  def __gt__(self,other):
    """Checks if a Vector is greater than another Vector or sequence.

    Args:
      other (Vector or sequence) : what we are checking self against
     
    Returns:
      True if self > other, False otherwise

    """
    if (isinstance(other,Vector)):
       #sorts data in Vectors and then compares them
       selfsorted = self.vecList[:]
       selfsorted.sort(reverse = True)
       othersorted = other.vecList[:]
       othersorted.sort(reverse = True)
       return selfsorted > othersorted
    else:
      return super(Vector,self) > other

  def __lt__(self,other):
    """Checks if a Vector is smaller than another Vector or sequence (when comparing element values).

    Args:
      other (Vector or sequence) : what we are checking self against

    Returns:
      True if self < other, False otherwise

    """
    if (isinstance(other,Vector)):
      #sorts data in Vectors and then compares them
      selfsorted = self.vecList[:]
      selfsorted.sort(reverse = True)
      othersorted = other.vecList[:]
      othersorted.sort(reverse = True) 
      return selfsorted < othersorted
    else:
      return super(Vector,self) < other

  def __ge__(self,other):
    """Checks if a Vector is greater than or equal to another Vector or sequence.
 
    Note:
      Two vectors could be considered equal if they have the same elements but in different order

    Args:
      other (Vector or sequence) : what we are checking self against

    Returns:
      True if self >= other, False otherwise

    """
    if (isinstance(other,Vector)):
       #sorts data in vectors and then compares them
       selfsorted = self.vecList[:]
       selfsorted.sort(reverse = True)
       othersorted = other.vecList[:]
       othersorted.sort(reverse = True) 
       if (selfsorted == othersorted): return True
       else:
         return (self > other)
    else:
       return (super(Vector,self) >= other) 

  def __le__(self,other):
    """Checks if a Vector is less than or equal to another Vector or sequence.

    Note:
      Two vectors could be considered equal if they have the same elements but in different order

    Args:
      other (Vector or sequence) : what we are checking self against

    Returns:
      True if self <= other, False otherwise

    """
    if (isinstance(other,Vector)):
       #sorts data in vector and then compares them
       selfsorted = self.vecList[:]
       selfsorted.sort(reverse = True)
       othersorted = other.vecList[:]
       othersorted.sort(reverse = True) 
       if (selfsorted == othersorted): return True
       else:
         return (self < other)
    else:
       return (super(Vector,self) <= other) 
