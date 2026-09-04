from calculator import add, subtract
from user import create_user

user1 = create_user("Alex", 23, "USA")
user2 = create_user("Dimitri", 25, "Russia")
user3 = create_user("Shi jhao", 20, "China")


user1_age_after_two_years = add(user1["age"], 2)
user2_age_after_two_years = add(user2["age"], 2)
user3_age_after_two_years = add(user3["age"], 2)

print(user1_age_after_two_years, user2_age_after_two_years, user3_age_after_two_years)