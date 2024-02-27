# Questions:
#1. What is the total number of CS credits required to complete the 4-year BSc Hons degree in CS?
#2. Could you provide a breakdown of CS credits ?
#3. What are the core courses ?
# 4. How many credits are allocated for non-academic activities?
# 5. What courses are suggested for the 5th semester?
# 6. How many credits are allocated for internships?
# 7. What is the structure of the academic credits, including FC credits, core CS credits, project credits, and elective credits?
# 8. Can you provide a sample course path for a student starting in the 1st semester and completing the 4-year BSc Hons degree in CS?
# 9. What courses are recommended for students interested in specializing in Information Security?
# 10. What are open credits?


import socket

hostIP = '127.0.0.1'
port=5000
serverSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind((hostIP,port))
serverSocket.listen(3)
print("Server Up!")

preRequisites = {"P&S": "Mathematics in Grades XI and XII. Alternatively, Quantitative Reasoning and Mathematical Thinking (FC 0306) + Calculus Enabler (MAT 1000)",
           "Linear Algebra": "Check with the Mathematics Department", "Calculus": "Check with the Mathematics Department", "Physics": "None", "Biology": "None",
           "Introduction to Computer Science": "Mathematics in Grades XI and XII. Alternatively, a minimum of B grade in both Quantitative Reasoning and Mathematical Thinking (FC 0306) and Calculus (MAT 1000)",
           "Discrete Mathematics": "Mathematics in Grades XI and XII. Alternatively, a minimum of B grade in both Quantitative Reasoning and Mathematical Thinking (FC 0306) and Calculus (MAT 1000)",
           "Data Structures and Algorithms": "Introduction to Computer Science; Discrete Mathematics",
           "Theory of Computation (ToC)": "Data Structures and Algorithms", "Computer Organisation and Systems": "Introduction to Computer Science",
           "Introduction to Machine Learning": "Probability and Statistics; Linear Algebra; Data Structures and Algorithms",
           "Design Practices in CS":"Data Structures and Algorithms; Computer Organisation and Systems","Computer Networks": "Introduction to Computer Science; Data Structures and Algorithms",
           "Information Security": "Data Structures and Algorithms; Probability and Statistics", "Design and Analysis of Algorithms": "Data Structure and Algorithms; Linear Algebra",
           "Data Science and Management": "Data Structures and Algorithms; Introduction to Machine Learning", "Programming Languages and Translations": "Data Structures and Algorithms; Theory of Computation",
           "Embedded Systems": "Computer Organisation and Systems"
           }

academic_credits_nums = {'FC Credits': 36, 'CS Credits': 86, 'Open Credits': 22, 'Non-academic Credits':6}
credits = {"Total Credits": 150, "Academic Credits": 
           {"FC Credits": 36, "CS Credits": {
               "Core":70, "Project":4, "Electives" : 12
           }, "Open Credits": 22},
           "Non-academic Credits": {
               "Co-curricular Credits": 4,
               "Internship Credits": 2
           }
           }

core_courses = ["P&S",
"Linear Algebra",
"Calculus",
"Physics (TBD)",
"Biology (TBD)",

"Introduction to Computer Science",
"Discrete Mathematics",
"Data Structures and Algorithms",
"Introduction to Machine Learning",
"Data Science and Management",
"Theory of Computation",
"Design and Analysis of Algorithms",
"Programming Languages and Translation",
"Information Security",

"Computer Organisation and Systems",
"Design Practices in CS",
"Computer Networks",
"Embedded Systems"]

example_path = {
    "1st Semester": "Calculus",
    "2nd Semester": "Introduction to Computer Science, Discrete Mathematics",
    "3rd Semester": "Probability and Statistics, Linear Algebra, Data Structures and Algorithms",
    "4th Semester": "Theory of Computation, Computer Organisation and Systems",
    "5th Semester": "Design Practices in CS, Introduction to Machine Learning, Computer Networks, Information Security (2 credits)",
    "6th Semester": "Design and Analysis of Algorithms, Data Science and Management, Embedded Systems",
    "7th Semester": "Capstone Project, Programming Languages and Translation",
    "8th Semester": "_",
    "Note: ": "Incorporate one Physics and one Biology course, along with 12 credits of Computer Science electives, within your four-year curriculum in addition to the mentioned courses"
}

stop_server = False
is_client_disc = False
def client_response(clientSocket, Address):
    global stop_server
    global is_client_disc
    while True:
        try:
            checkIfWorking = clientSocket.recv(3000).decode()
            if checkIfWorking == 'Working!':
                while True:
                    choice = clientSocket.recv(3000).decode()

                    if choice == 'X':
                        stop_server = True
                        return
            
                    elif choice == '1':
                        cs_credits_info = academic_credits_nums.get('CS Credits', 'Course not found')
                        cs_credits_info = str(cs_credits_info)
                        clientSocket.send(cs_credits_info.encode())
                    
                    elif choice == '2':
                        cs_credits_info = credits.get("Academic Credits", {}).get("CS Credits", None)

                        if cs_credits_info:
                            cs_credits_message = ""
                            for key, value in cs_credits_info.items():
                                cs_credits_message += f"{key}: {value}\n"
                            clientSocket.send(cs_credits_message.encode())
                        else:
                            clientSocket.send("CS Credits information not found".encode())

                    elif choice == '3':
                        core_courses_message = ", ".join(core_courses)

                        clientSocket.send(core_courses_message.encode())

                    elif choice == '4':
                        non_academic_credits_info = academic_credits_nums.get('Non-academic Credits', 'Non-academic credits not found')
                        non_academic_credits_info = str(non_academic_credits_info)
                        clientSocket.send(non_academic_credits_info.encode())

                    elif choice == '5':
                        fifth_semester_info = example_path.get('5th Semester', 'Information for the 5th Semester not found')
                        clientSocket.send(fifth_semester_info.encode())

                    elif choice == '6':
                        non_academic_credits = credits.get("Non-academic Credits", {})
                        internship_credits = non_academic_credits.get("Internship Credits", 'Internship Credits not found')
                        internship_credits = str(internship_credits)
                        clientSocket.send(internship_credits.encode())

                    elif choice == '7':
                        academic_credits = credits.get("Academic Credits", {})

                        academic_credits_message = ""
                        for key, value in academic_credits.items():
                            academic_credits_message += f"{key}: {value}\n"

                        clientSocket.send(academic_credits_message.encode())

                    elif choice == '8':
                        example_path_message = ""
                        for key, value in example_path.items():
                            example_path_message += f"{key}: {value}\n"

                        clientSocket.send(example_path_message.encode())

                    elif choice == '9':
                        information_security_value = preRequisites.get("Information Security", "Information Security prerequisite information not found")

                        clientSocket.send(information_security_value.encode())

                    elif choice == '10':
                        open_credits = 'These are 22 academic credits can be earned by taking courses from any department within the university, including the Computer Science Department.'
                        clientSocket.send(open_credits.encode())


                    elif choice == '11':
                        course_names = ', '.join(preRequisites.keys())
                        clientSocket.send(course_names.encode())
                        course_name = clientSocket.recv(3000).decode()
                        preRequisites_value = preRequisites.get(course_name, f"Prerequisite information not found for {course_name}")
                        clientSocket.send(preRequisites_value.encode())

                    else:
                        clientSocket.send("Invalid choice! Rewrite/Press X to exit...".encode())
                        
        except OSError:
            is_client_disc = True
            return
            

while True:
    (clientSocket, Address) = serverSocket.accept()
    print("Client Up!")
    intro = "\nUnderstand the new curriculum structure of the 4 year CS major!\n"
    clientSocket.send(intro.encode())
    client_response(clientSocket, Address)

print("Client Down!")
clientSocket.close()
serverSocket.close()