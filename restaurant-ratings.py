# your code goes here
def print_rating(filename):
    
    restaurants = open(filename)
    
    restaurant_ratings = {}

    for line in restaurants:
        line = line.rstrip()
        split_line = line.split(":")
       
        restaurant = split_line[0]
        value = split_line[1]

        restaurant_ratings[restaurant] = value

    for restaurant in sorted(restaurant_ratings):
        print restaurant, "is rated at", restaurant_ratings[restaurant]

    restaurants.close()

print print_rating("scores.txt")