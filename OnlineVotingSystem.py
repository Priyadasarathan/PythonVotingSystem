leader_1 = "PRIYA"
leader_2 = "HARSHA"
voters_id = list(range(1001,1020))
lead_1 = 0
lead_2 = 0
no_of_voters = len(voters_id)
print("Number of voters:")
voted = []


while True:
    if voters_id == []:
        print("VOTING IS OVER!!!!!!!!")
        if lead_1>lead_2:
            print(f"{leader_1}won the election with {lead_1}")
        elif lead_2>lead_1:
            print(f"{leader_1}won the election with{lead_2}")
        elif lead_1==lead_2:
            print("Tied!!!")
        break

    else:
        voter = int(input("Enter your voter_id:"))
        if voter in voted:
            print("You are already voted!!!!")
        else:
            if voter in voters_id:
                print(f"1.{leader_1}\n2.{leader_2}")
                choice = int(input("choose your leader:"))
                if choice == 1:
                    lead_1 += 1
                    print(f"your supported for:{leader_1}")
                elif choice == 2:
                    lead_2 += 1
                    print(f"your supported for: {leader_2}")
                
                voters_id.remove(voter)
                voted.append(voter)

            else:
                print("you are not allowed for voting")


