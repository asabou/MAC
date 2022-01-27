from HEUtils import HEUtils

def main():
    heutils = HEUtils(10)
    bins = heutils.generateBINS()
    user1 = heutils.createUser("alex", "password", bins)
    user2 = heutils.createUser("nadal", "rafael", bins)
    users = [user1, user2]
    print(user1)
    print(user2)
    run = True
    while(run):
        print("Username: ")
        username = input()
        print("Password: ")
        password = input()
        userFound = False
        for user in users:
            if (user.getUsername() == username and user.getPassword() == password):
                heutils.printCards(user.getCards())
                userFound = True
                break
        if not userFound:
            print("Intruder found!!!")
            heutils.printCards(heutils.generateCards(bins))
        print("Would you like another test? y/n")
        run = input() == "y"

main()