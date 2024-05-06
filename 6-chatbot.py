from datetime import datetime
routes = {
		"Delhi": ["Mumbai", "Bangalore", "Jaipur"],
		"Mumbai": ["Delhi", "Chennai", "Goa"],
		"Bangalore": ["Delhi", "Hyderabad", "Kerala"],
}
def greet():
	print("Hi! Welcome to the Bus Ticket Booking Chatbot.")
	print("I can help you find and book bus tickets.")
def get_starting_city():
	while True:
		starting_city = input("Enter your starting city (or 'exit' to quit): ")
		if starting_city.lower() == "exit":
			print("Thank you for using the chatbot!")
			exit()
		if starting_city in routes:
			return starting_city.title()
		else:
			print("Invalid city. Please enter a valid starting city or 'exit'.")
def show_destinations(starting_city):
	print(f"Available destinations from {starting_city}:")
	for destination in routes[starting_city]:
		print(f"- {destination}")
def get_destination(starting_city):
	while True:
		destination = input(f"Enter your destination city from {starting_city} (or 'back' to go back): ")
		if destination.lower() == "back":
			return None
		if destination.title() in routes[starting_city]:
			return destination.title()
		else:
			print("Invalid destination. Please enter a valid destination city or 'back'.")
def get_travel_date():
	while True:
		try:
			travel_date = input("Enter your desired travel date (YYYY-MM-DD format): ")
			datetime.strptime(travel_date, "%Y-%m-%d")
			return travel_date
		except ValueError:
			print("Invalid date format. Please enter date in YYYY-MM-DD format.")
def confirm_booking(starting_city, destination, travel_date):
	print(f"You are booking a bus ticket from {starting_city} to {destination} on {travel_date}.")
	print("** (This is a simulated confirmation. Integration with booking system required) **")
	print("Would you like to confirm this booking? (yes/no)")
	confirmation = input("> ").lower()
	if confirmation == "yes":
		print("Your bus ticket has been booked!")
	else:
		print("Booking cancelled.")
greet()
starting_city = get_starting_city()
show_destinations(starting_city)
destination = get_destination(starting_city)
if destination:
	travel_date = get_travel_date()
	confirm_booking(starting_city, destination, travel_date)
