count_tickets = 0
student = 0
standard = 0
kids = 0

while True:
    film = input()
    if film == "Finish":
        break
    seats = int(input())
    current_tickets = 0

    for i in range(seats):
        ticket_tipe = input()
        if ticket_tipe == 'student':
            student += 1
        if ticket_tipe == 'standard':
            standard += 1
        if ticket_tipe == 'kid':
            kids += 1
        if ticket_tipe == 'End':
            break
        current_tickets += 1
        count_tickets += 1
    percent_all = current_tickets / seats * 100
    print(f"{film} - {(percent_all):.2f}% full.")

pers_student = student / count_tickets * 100
pers_standard = standard / count_tickets * 100
pers_kids = kids / count_tickets * 100
print(f'Total tickets: {count_tickets}')
print(f"{(pers_student):.2f}% student tickets.")
print(f"{(pers_standard):.2f}% standard tickets.")
print(f"{(pers_kids):.2f}% kids tickets.")
