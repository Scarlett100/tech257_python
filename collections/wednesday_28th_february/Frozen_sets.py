#Objective
#Understand the concept and usage of immutable sets (frozen sets).
#can add to sets but cannot update frozen sets.
#hashable and immutable

#The task
#Create a frozen set named frozen_set containing elements "hello", "world".
frozen_set  = frozenset(["hello", "world"])
print(frozen_set)
#Try to add "!" to frozen_set. What happens?
#cannot be modified they are frozen! immutable

#Create a normal set named normal_set containing elements "let's", "learn".
normal_set ={"let's", "learn" }
#Try to add frozen_set to normal_set. Why does it work? Explain.
normal_set = {"let's", "learn", frozen_set }
#normal_set.update(frozen_set)
#normal_set.add(frozen_set)
#Print normal_set.
print(normal_set)
#Run your script half a dozen times. What do you notice about where frozen_set is added to normal_set? Hint: Look at the order of the items.
#What makes a frozen set different to a normal set? Explain.
# Moves around

# Olivers way <--neater
#frozen_set = frozenset({"hello", "world"})
#normal_set = {"let's", "learn"}
#normal_set.update(frozen_set)
#print(normal_set)
