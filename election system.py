nominee_1 = input('')
nominee_2 = input('')  #names of nominee

nom_1_votes = 0
nom_2_votes = 0   #initial votes of nominees are zero

voter_id = [1,2,3,4,5,6]   #these are voter_id number of common people

#num_of_voters = len(voter_id)

while True:
    voter = int(input('enter the voter id number: '))
    if voter in voter_id:
        print ('you are an elligible voter')
        voter_id.remove(voter)
#while True is infinite statement which will keep running as long as list is not empty
#once the voter id is recorded his number will be removed from list so that his number is not repeated
        vote = int(input('enter your vote 1 or 2: '))
        if vote == 1:
            nom_1_votes +=1
        else:
            nom_2_votes +=1
            
    else:
        print('you are not an elligible voter')

     
    if voter_id == []:
          print('voting completed successfully')
          break
#if list gets empty means voting completed
        

if nom_1_votes > nom_2_votes:
    print('nominee', nominee_1 ,'is winner')
elif nom_2_votes > nom_1_votes:
    
    print('nominee', nominee_2 ,'is winner')
else:
    print('equal votes')
