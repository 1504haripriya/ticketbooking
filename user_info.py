import re


class user_info:
    global dict_info
    list_booked_seats = []

    def user(self, book_row, book_column):
        dict_info = {"Name": "", "emailid": "",  "Phone_no": int}

        name = input("Enter the Name: ")
        emailid = input("Enter your emailid: ")

        phone_no = input("Enter your Phone number: ")

        for i in range(10):
            mat = re.fullmatch("[89][0-9]{9}", phone_no)
            if mat != None:

                dict_info["Name"] = name
                dict_info["emailid"] =emailid
                dict_info["Phone_no"] = phone_no

                list1 = [book_row, book_column, dict_info]
                user_info.list_booked_seats.append(list1)
                print("CONGRATS!!! Booked Successfully")
                break
            else:
                print("Invalid Phone Number!!!")
                phone_no = input("Please Enter Valid Mobile Number: ")

    def booked_tickets_user_info(self, row_c, column_c, current_income):

        if len(user_info.list_booked_seats) > 0:
            for i in range(len(user_info.list_booked_seats)):
                if (user_info.list_booked_seats[i][0] == row_c and user_info.list_booked_seats[i][1] == column_c):
                    print("Name: ", user_info.list_booked_seats[i][2].get("Name"))
                    print("emailid: ", user_info.list_booked_seats[i][2].get("emailid"))
                    print("Phone Number: ", user_info.list_booked_seats[i][2].get("Phone_no"))
                    print("Ticket Price :", current_income, '$')
                    break
            else:
                print("Seat is vacant")

        else:
            print("Auditorium is Empty")
