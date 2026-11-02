import pickle
import os
import random
class Participant:
    def __init__(self,name,ticket_number):
        self.name = name
        self.ticket_number = ticket_number
    @staticmethod
    def generate_ticket():
        return random.randint(1000,9999)
participants = []
if os.path.exists("raffle.pkl"):
    with open("raffle.pkl","rb") as f:
        print(f"Loaded {len(participants)} participants from file.")
while True:
    choice = input("1.Add participant\n2.Show All participants\n" \
    "3.Draw a Winner!\n4.Exit & Save\nChoose one option:")
    if choice == "1":
        name = input("Enter participant name:")
        ticket = Participant.generate_ticket()
        new_person = Participant(name,ticket)
        participants.append(new_person)
        print(f"{name} added successfully with ticket number{ticket}!")
    elif choice == "2":
        if not participants:
            print("No participants yet.")
        else:
            print("\n--- Current Participants ---")
            for i,person in enumerate(participants,1):
                print(f"{i}. {person.name} - Ticket: {person.ticket_number}") 
    elif choice == "3":
        if not participants:
            print("No one to draw!")
        else:
            winner = random.choice(participants)
            print("\n --- WE HAVE A WINNER!---")
            print(f"Winner Name: {winner.name}")
            print(f"Winning Ticket: {winner.ticket_number}")
    elif choice == "4":
        with open("raffle.pkl","wb") as f:
            pickle.dump(participants,f)
        print("Participants saved successfrlly. Goodbye!")
        break
