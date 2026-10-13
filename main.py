"""
Chaos Calculator
Calculates separate social and academic chaos scores from 10 questions.
Social life: 6 questions, maximum 60 points.
Academic life: 4 questions, maximum 40 points.
Overall chaos: maximum 100 points.
"""


def ask_number(prompt):
	"""Return a non-negative integer, repeating the question for invalid input."""
	while True:
		raw = input(prompt).strip()
		try:
			value = int(raw)
			if value < 0:
				print("Please enter 0 or a positive whole number.")
				continue
			return value
		except ValueError:
			print("Invalid input. Please enter a whole number, such as 2.")


def ask_yes_no(prompt):
	"""Return 'yes' or 'no'; accept answers regardless of case and whitespace."""
	while True:
		answer = input(prompt).strip().lower()
		if answer in ("yes", "y"):
			return "yes"
		elif answer in ("no", "n"):
			return "no"
		else:
			print("Please answer yes or no.")


def score_frequency(value, medium_limit, low_score=0, medium_score=5, high_score=10):
	"""Score a numeric answer using the shared frequency rule."""
	if value == 0:
		return low_score
	elif value <= medium_limit:
		return medium_score
	else:
		return high_score


def score_yes_no(answer):
	"""Give 10 points for yes and 0 points for no."""
	if answer == "yes":
		return 10
	else:
		return 0


def ask_social_questions():
	"""Ask six social-life questions and return the total score out of 60."""
	print("\n---- SOCIAL LIFE QUESTIONS ----")
	total = 0

	# First social question
	ans1 = ask_number(
		"1. How many classes have you missed or been late to since school started? "
	)

	if ans1 == 0:
		point = 0
	elif ans1 == 1:
		point = 2
	elif ans1 == 2:
		point = 4
	elif ans1 == 3:
		point = 6
	else:
		point = 10

	total += point

	# Second social question
	ans2 = ask_number(
		"2. How many times have you had problems on public transportation "
		"in the last month (fight, argument, etc.)? "
	)
	total += score_frequency(ans2, 3)

	# Third social question
	ans3 = ask_number(
		"3. How many hours did you spend in traffic during the past week? "
	)
	total += score_frequency(ans3, 2)

	# Fourth social question
	ans4 = ask_number(
		"4. How many plans did you join and then immediately regret joining? "
	)
	total += score_frequency(ans4, 3)

	# Fifth social question
	ans5 = ask_yes_no(
		"5. Have you ever gone somewhere for one reason and completely "
		"forgotten why? (yes/no): "
	)
	total += score_yes_no(ans5)

	# Sixth social question
	ans6 = ask_number(
		"6. Since school started, how many days have you asked yourself, "
		"'How much worse can things possibly get?' "
	)

	if ans6 == 0:
		point = 0
	elif ans6 == 1:
		point = 2
	elif ans6 == 2:
		point = 4
	elif ans6 == 3:
		point = 6
	else:
		point = 10

	total += point

	return total


def ask_academic_questions():
	"""Ask four academic-life questions and return the total score out of 40."""
	print("\n---- ACADEMIC LIFE QUESTIONS ----")
	total = 0

	# First academic question
	ans1 = ask_yes_no(
		"1. Have you been partying since school started? (yes/no): "
	)
	total += score_yes_no(ans1)

	# Second academic question
	ans2 = ask_number("2. How many times have you forgotten a deadline? ")
	total += score_frequency(ans2, 2)

	# Third academic question
	ans3 = ask_yes_no(
		"3. Have you ever arrived at an exam without studying at all? "
		"(yes/no): "
	)
	total += score_yes_no(ans3)

	# Fourth academic question
	ans4 = ask_number(
		"4. How many times have you walked into the wrong classroom "
		"since school started? "
	)
	total += score_frequency(ans4, 3)

	return total


def show_social_analysis(score):
	"""Display the social-life analysis."""
	print("\n---- SOCIAL LIFE ANALYSIS ----")

	if score <= 20:
		print("You have a pretty spontaneous social life.")
	elif score <= 40:
		print("Your social life is quite active.")
	else:
		print("My friend, your social life is chaos. Take a breath.")

	print(f"Your social chaos score: {score}/60")


def show_academic_analysis(score):
	"""Display the academic-life analysis."""
	print("\n---- ACADEMIC LIFE ANALYSIS ----")

	if score <= 10:
		print(
			"Your academic life is virtually trouble-free; "
			"everyone wants to be you."
		)
	elif score <= 20:
		print(
			"You need to be a little more careful. You are close to a "
			"chaos-free life, but you aren't quite there yet."
		)
	else:
		print(
			"You need to pay some attention to your academic life while "
			"there is still time; otherwise, things could turn out badly."
		)

	print(f"Your academic chaos score: {score}/40")


def show_total_analysis(social_score, academic_score):
	"""Calculate and display the overall chaos percentage."""
	total_points = social_score + academic_score
	total_possible_points = 100
	percentage = total_points / total_possible_points * 100

	print("\n---- TOTAL CHAOS PERCENTAGE ----")
	print(f"Social points: {social_score}/60")
	print(f"Academic points: {academic_score}/40")
	print(f"Total chaos points: {total_points}/100")
	print(f"Your total chaos percentage is: {percentage:.0f}%")

	if percentage <= 30:
		print(
			"Low chaos level. My grandmother's life is more chaotic than yours."
		)
	elif percentage <= 60:
		print(
			"Average chaos level. I hope you're having fun and that your "
			"life isn't overly chaotic or boring."
		)
	else:
		print(
			"High chaos level. Buddy, follow the rules. "
			"You can't enjoy life like this."
		)


def main():
	"""Run the Chaos Calculator."""
	print("Welcome! It's your Chaos Calculator.")
	print(
		"I will help you calculate the chaos in your social and academic "
		"life and classify it into different levels."
	)

	name = input(
		"How should I address you? Please enter your name or nickname: "
	).strip()

	if not name:
		name = "friend"

	print(f"Nice to meet you, {name}! Let's get started.")
	print("-" * 75)

	total_social_points = ask_social_questions()
	total_academic_points = ask_academic_questions()

	show_social_analysis(total_social_points)
	show_academic_analysis(total_academic_points)
	show_total_analysis(total_social_points, total_academic_points)


if __name__ == "__main__":
	main()
