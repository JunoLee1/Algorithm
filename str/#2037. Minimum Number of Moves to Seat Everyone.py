def minMovesToSeat(seats_list, students_list):
    moved_seat = []
    sorted_students = sorted(students_list)
    sorted_seats = sorted(seats_list)
    for i in range(len(sorted_students)):
        moved_seat.append(abs(sorted_students[i]-sorted_seats[i]))
    return sum(moved_seat)

seats = [3,1,5]
students = [2,7,4]
print(minMovesToSeat(seats,students))