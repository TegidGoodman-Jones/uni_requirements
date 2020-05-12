# AUTHOR: TEGID GOODMAN-JONES
# CREATED ON 04/05/20
# LAST-EDITED ON 12/05/20




from bs4 import BeautifulSoup as BS
import requests
from unis_class import University, a_level


unis =  [
	University("university-of-birmingham", "b32"),
	University("university-of-bristol", "b78"),
	University("university-of-huddersfield", "h60"),
	University("university-of-leicester", "l34"),
	University("Aston-University", "a80"),
	University("Swansea-University", "s93"),
	University("University-of-Chichester", "c58"),
	University("University-of-Reading", "r12"),
	University("University-of-leeds", "l23"),
	University("University-of-Sheffield", "s18"),
	University("university-of-nottingham", "n84"),
	University("University-of-Kent", "k24"),
	University("Cardiff-University", "c15"),
	University("University-of-Manchester", "m20"),
	University("Newcastle-University", "n21"),
	University("Lancaster-university", "l14"),
	University("durham-university", "d86"),
	University("university-of-strathclyde", "s78"),
	University("university-of-stirling", "s75"),
	University("birmingham-city-university", "b25"),
	University("loughborough-university", "l79"),
	University("university-of-warwick", "w20"),
	University("university-of-bath", "b16"),
	University("university-of-edinburgh", "e56"),
	University("university-of-exeter", "e84"),
	University("university-of-glasgow", "g28"),
	University("imperial-college-london", "i50"),
	University("kings-college-london-university-of-london", "k60"),
	University("university-of-liverpool", "l41"),
	University("queen-mary-university-of-london", "q50")
	# queen-belfast
	# york
	# southhampton
	# collage london	
]


prompt = "\nEnter a course\nMake sure you spell it correctly, otherwise no courses will be found\n: "

choice = input(prompt)

off_course_name = choice.replace(" ", "+").strip()  # formating the course correctly for the url


print("\n")
print(off_course_name.replace("+", " ").title() + "\n")


for uni in unis:
	
	# getting the page
	# make url vars
	link_p = "https://www.theuniguide.co.uk/search/course?utf8=%E2%9C%93&c%5Bq%5D=" + str(off_course_name) + "&c%5Bacademic_years%5D=2020&c%5Binstitution_slug%5D%5B%5D=" + uni.name.lower() + "-" + uni.code + "&c%5Bsort%5D=relevance"
	link = str(link_p)

	url = requests.get(link)

	src = url.content # getting the html of page
	
	soup = BS(src, "lxml")  # making the html parsable
	
	# extracting info

	name = uni.name.title()
	name_txt = name.replace("-", " ")

	try:	
		courses_type = soup.find_all("div", {"class" : "course-snippets"})

		# selecting a Bachelors degree

		if "B" in courses_type[0].text:
			course_text = courses_type[0].text
			num = 0
		
		elif "B"in courses_type[1].text:
			course_text = courses_type[1].text
			num = 3  # jumping to next instance of ucas pts
		
		elif "B" in courses_type[2].text:
			course_text = courses_type[2]  
			num = 6
		
		elif "B" in courses_type[3].text:
			course_text = courses_type[3].text
			num = 9
		else:
			pass
		# print(num) # use this to check alignment of courses and grade
		type_txt = course_text.strip()  # removing unnesisary spaces
		

		courses_pts = soup.find_all("div", {"class" : "stat-number"})
		headers = soup.find_all("dt", {"class" : "result-card-stats__heading"})

		header = headers[0]
		
		course_pts = courses_pts[num]  # accessing same ucas points as the course type
		
		header_txt = header.text  # printing the ucas pts title
		pts_text = str(course_pts.text)  # making sure the points are a string
		
		pts_txt = header_txt.strip() + ": " + pts_text.strip()  # removing all unnessisary whitespace


		pure_pts = pts_text.replace(" ", "").strip()  # making it purely numbers
	
	

		print(name_txt + "      " + type_txt + "      " + pts_txt + "      A levels: " + a_level(pure_pts))
		# add "+ str(num)" to end of this print statement to check alignment of courses and grades

	except IndexError:
		print(name_txt + "      " + "no courses found here" )
		pass
	








