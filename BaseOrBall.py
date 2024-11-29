import random 

print("This is a program play Base Or Ball\n")

global batsman, bowler

while True:
    batsmen_score = 0
    bowler_score = 0

    fun1  = input("Enter 'Enter' to round 1 :  ")

    if fun1 == "":
        while True :
            print ("\n Getting Ready ...\n")
            batsman = random.randint(0,6)
            bowler = random.randint(0,6)
            
            # out
            if batsman == bowler + 1 or batsman ==  bowler - 1:
                print ("\nThe batsmans1 showed : ",batsman)
                print ("The bowler2 showed : ",bowler)
                
                # Duck Out
                if batsmen_score == 0: 
                    print("\nThe batsman1 is duck out!!\n")
                    break 
                else:
                    print("The batsman1 is out & scored : ",batsmen_score)
                    break
                
            # not out 
            else:
                if batsman == bowler :
                    batsmen_score += batsman*2

                elif batsman == 0:
                    batsmen_score += bowler

                
                else :
                    batsmen_score += batsman


                print ("The batsman1 showed is : ",batsman)
                print ("The bowler1 showed is : ",bowler)
                print("Score : ", batsmen_score)


            dicision = input ("\nPress Enter to go again :   ")
            if dicision == '' :
                continue
            

    batsman, bowler = bowler, batsman


    fun2  = input("\nEnter enter to round 2 :  ")

    if fun2 == "":
        while True :
            print ("\n Getting Ready ...\n")
            batsman = random.randint(0,6)
            bowler = random.randint(0,6)
            
            # out
            if batsman == bowler + 1 or batsman ==  bowler - 1:
                print ("The batsmans1 showed : ",batsman)
                print ("The bowler2 showed : ",bowler)
                
                # Duck Out
                if batsmen_score == 0: 
                    print("\n The batsman1 is duck out!!\n")
                    break 
                else:
                    print("The batsman1 is out & scored : ",bowler_score)
                    break
                
            # not out 
            else:
                if batsman == bowler :
                    bowler_score += batsman*2

                elif batsman == 0:
                    batsman = bowler
                    bowler_score += batsman

                
                else :
                    bowler_score += batsman


                print ("\nThe batsman1 showed is : ",batsman)
                print ("\nThe bowler1 showed is : ",bowler)
                print("score : ", bowler_score)


            dicision = input ("\nPress Enter to go again :   ")
            if dicision == '' :
                continue
            

    if batsmen_score > bowler_score :
        print ("\nBatsmen1 : ", batsmen_score)
        print ("\nBatsmen2 : ", bowler_score)
        print ("\nBatsmen1 won by : {} score(s)".format(batsmen_score - bowler_score))
        break

    elif  bowler_score > batsmen_score :
        print ("\nBatsmen1 : ", batsmen_score)
        print ("\nBatsmen2 : ", bowler_score)
        print ("\nBatsmen2 won by : {} score(s)".format(batsmen_score - bowler_score))
        break

    else:
        print("!!Its a tie !!")
        print("!!GETTING READY FOR THE NEXT MATCH!!")
        continue
