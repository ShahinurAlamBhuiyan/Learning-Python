def greet_user(first_name, last_name):  # first_name, last_name are parameters
    print(f"Hi {first_name} {last_name}! Welcome aboard.")


greet_user("Shahin", "Bhuiyan")  # Positional arguments
greet_user(first_name="Nur", last_name="Tonmay")  # keyword arguments

# keyword arguments is increase the readability of the code.
# When we pass numerical value through arguments most of the time we  use keyword arguments.

# if we use both, positional arguments must be in first positions
# greet_user(first_name="Amit", "Mahmud")  # ERROR!
greet_user("Amit", last_name="Mahmud")


