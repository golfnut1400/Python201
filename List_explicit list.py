
"""If you want to prevent changes in areas_copy to also take effect in areas, you'll have to do a more explicit copy of the areas list.
You can do this with list() or by using [:]
"""




# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)  # use of list()

# Change areas_copy
areas_copy[0] = 5.0

# print areas_copy
print("This is the values for areas_copy:",areas_copy) # 5.0 value added to index 0
print
print
# Print areas
print("This is the values for areas:" ,areas)  # areas not impacted by the change to areas_copy

#

type(areas)
