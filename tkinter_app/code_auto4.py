# AUTHOR: TEGID GOODMAN-JONES
# CREATED ON 11/05/20
# LAST-EDITED ON 11/05/20



from bs4 import BeautifulSoup as BS
import requests
from unis_class import University, a_level
from tkinter import *
# import datetime  # used for checking response times

unis =  [
	University("university-of-birmingham", "b32"), # 0
	University("university-of-bristol", "b78"),  # 1
	University("university-of-huddersfield", "h60"),  # 2
	University("university-of-leicester", "l34"),  # 3
	University("Aston-University", "a80"),  # 4
	University("Swansea-University", "s93"),  # 5
	University("University-of-Chichester", "c58"),  # 6
	University("University-of-Reading", "r12"),  # 7
	University("University-of-leeds", "l23"),  # 8
	University("University-of-Sheffield", "s18"),  # 9
	University("university-of-nottingham", "n84"),  # 10
	University("University-of-Kent", "k24"),  # 11
	University("Cardiff-University", "c15"),  # 12
	University("University-of-Manchester", "m20"),  # 13
	University("Newcastle-University", "n21"),  # 14
	University("Lancaster-university", "l14"),  # 15
	University("durham-university", "d86"),  # 16
	University("university-of-strathclyde", "s78"),  # 17
	University("university-of-stirling", "s75"),  # 18
	University("birmingham-city-university", "b25"),  # 19
	University("loughborough-university", "l79"),  # 20
	University("university-of-warwick", "w20"),  # 21
	University("university-of-bath", "b16"),  # 22
	University("university-of-edinburgh", "e56"),  # 23
	University("university-of-exeter", "e84"),  # 24
	University("university-of-glasgow", "g28"),  # 25
	University("imperial-college-london", "i50"),  # 26
	University("kings-college-london-university-of-london", "k60"),  # 27
	University("university-of-liverpool", "l41"),  # 28
	University("queen-mary-university-of-london", "q50"),  # 29
	University("university-of-york", "y50")  #30
	# queen-belfast
	# southhampton
	# collage london	
]

# if unis added change in statement in loop



results = []
root = Tk()

root.title('Entry Requirement finder')


frame = Frame(root, width=1000, height=750, padx=6, pady=4)
frame.pack(padx=10, pady=10)

def excel():
	joined = ''.join(results)  # making the list a string
	try:
		new_file = open("entry_req.csv", "x")  # creating file for user data
		new_file.close()
	except FileExistsError:
		pass
	csv_file = open("entry_req.csv", "w")
	csv_file.write(crs + "\n" + joined)  # writing in user data
	csv_file.close()
	confirm = Label(frame, text="Created csv file.")
	confirm.grid(row=6,column=1)





def submit():
	time = 7
	awnser = entry.get()  # collecting the user input
	choice = str(awnser)  # making it a string
	off_course_name = choice.replace(" ", "+").strip()  # formating the course correctly for the url

	global crs
	crs = choice.title()
	crs_label = Label(frame, text=crs) 
	crs_label.grid(row=7, column=1)

	for uni in unis:
		# getting the page
		# make url vars
		

		"https://www.theuniguide.co.uk/search/course?utf8=%E2%9C%93&c%5Bq%5D=" + str(off_course_name) + "&c%5Bacademic_years%5D=2021&c%5Binstitution_slug%5D%5B%5D=" + uni.name.lower() + "-" + uni.code + "&c%5Bsort%5D=relevance"
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

		
			course_pts = courses_pts[num]  # accessing same ucas points as the course type
		
			pts_text = str(course_pts.text)  # making sure the points are a string
		
			pts_txt = pts_text.strip()  # removing all unnessisary whitespace


			pure_pts = pts_text.replace(" ", "").strip()  # making it purely numbers
			

			# currentDT = datetime.datetime.now()
			# cur_time = currentDT.strftime("%H:%M:%S.%d")

			# add this to end of below statement to review response time  + cur_time
			result = name_txt + ",  " + type_txt + ",  " + pts_txt + ",  " + a_level(pure_pts)
			result_for_excel = name_txt + "," + type_txt + "," + pts_txt + "," + a_level(pure_pts) + "\n"
			
			results.append(result_for_excel) 

			uni_num = unis.index(uni)
			
			if (uni_num % 2) == 0:
				result_label = Label(frame, text=result)  # printing the results in two columns
				result_label.grid(row=time, column=0)	
			else:
				result_label = Label(frame, text=result)
				result_label.grid(row=time, column=2)
				time += 1


			if uni_num == 30:
				export.grid(row=5, column=1)

			

		except IndexError:
			pass



prompt = "\nEnter a course:\nMake sure you spell it correctly\n"

prompt_label = Label(frame, text=prompt)
prompt_label.grid(row=0, column=1)

entry = Entry(frame, width=20, borderwidth=3)
entry.grid(row=1, column=1)

submit = Button(frame, text="Submit", padx=15, pady=7, fg="red", command=submit)  # submit : runs the web scraping operation
submit.grid(row=2,column=1)

export = Button(frame, text="Export to excel", pady=7, padx=15, fg="#228B22", command=excel)  # runs the function to create a file





root.mainloop()








