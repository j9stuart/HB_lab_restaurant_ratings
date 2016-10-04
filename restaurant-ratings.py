# your code goes here
def print_rating(filename):
    
    restaurants = open(filename)
    
    restaurant_ratings = {}

    for line in restaurants:
        line = line.rstrip()
        split_line = line.split(":")
       
        restaurant = split_line[0]
        rating = split_line[1]

        restaurant_ratings[restaurant] = rating

    for restaurant, rating in sorted(restaurant_ratings.items()):
        print restaurant, "is rated at", rating

    restaurants.close()

print_rating("scores.txt")
