class person:
	 '''Represents a person.'''
	 population=0
	 def __init__(self,name):
		  '''Initializes the person's data.'''
		  self.name=name
		  print '(Initializing %s)' % self.name
		  person.population +=1

	 def sayhi(self):
		  '''Greeting by the person.

		  Really, that's all it does.'''
		  print 'hi, my name is %s.' % self.name

		  
         def howmany(self):
		  '''Prints the current population.'''
		  if person.population==1:
			   print 'I am the only person here.'
		  else:
			   print 'We have %d persons here.' % person.population

			   
