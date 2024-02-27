import socket

host = '127.0.0.1'
port = 5000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host, port))

try:
    while True:  # Loop until the user presses 'X'
        print(clientSocket.recv(3000).decode())
        clientSocket.send('Working!'.encode())


        while True:
            print("""
Enter the Question Number to get answer for that question!
1. What is the total number of CS credits required to complete the 4-year BSc Hons degree in CS?
2. Could you provide a breakdown of CS credits ?
3. What are the core courses ?
4. How many credits are allocated for non-academic activities?
5. What courses are suggested for the 5th semester?
6. How many credits are allocated for internships?
7. What is the structure of the academic credits, including FC credits, core CS credits, project credits, and elective credits?
8. Can you provide a sample course path for a student starting in the 1st semester and completing the 4-year BSc Hons degree in CS?
9. What courses are recommended for students interested in specializing in Information Security?
10. What are open credits?
11. Request prerequisites for a course.
Or Press X to exit!
What would you like to view? (1-11/X): """, end='')
            choice = input()
            clientSocket.send(choice.encode())
            print()

            if choice == 'X':
                break

            elif choice == '11':
                print("Here are all the courses for which prerequisite information is available:")
                course_names = clientSocket.recv(3000).decode()
                print(course_names)

                print("Enter the course name for which you want to know the prerequisites: ", end='')
                course_name = input()
                clientSocket.send(course_name.encode())
                response = clientSocket.recv(3000).decode()
                print()
                print(response)

            elif choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
                response = clientSocket.recv(3000).decode()
                print(response)

            else:
                response = clientSocket.recv(3000).decode()
                print(response)

        if choice == 'X':
            break

except OSError:
    print("Connection closed")

clientSocket.close()