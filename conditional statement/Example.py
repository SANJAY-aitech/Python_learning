movie_name = "Final Destination-Bloodlines"
age=int(input("Enter Your birth year: "))

allowed_age =2025-age

if allowed_age >= 18:
    print(f"You can watch the movie:-- {movie_name} ")
else:
    print("Sorry 18+ Only")