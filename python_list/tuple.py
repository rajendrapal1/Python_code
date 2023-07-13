rgb = ('red', 'green', 'blue','red') # tuple we can not change 
#rgb[0] = 'yellow'
#print(rgb)
# b=rgb[0]
# print(b)
# print(b[:])
########################################################
companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]


# define a sort key
def sort_key(company):
    return company[1]

# sort the companies by revenue
companies.sort(key=sort_key, reverse=False)

# show the sorted companies
print(companies)

###############################################################

# #using lambda fun
# companies = [('Google', 2019, 134.81),
#              ('Apple', 2019, 260.2),
#              ('Facebook', 2019, 70.7)]

# # sort the companies by revenue
# companies.sort(key=lambda company: company[1])



# # show the sorted companies
# print(companies)
