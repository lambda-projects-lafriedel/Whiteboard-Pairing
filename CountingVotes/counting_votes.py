def count_votes(votes):
    # Edge case: If fed an empty list -- return "None".
    #if len(votes) == 0:
        #return "No winner."
    if len(votes) == 0:
        return "No winner."
    elif len(votes) == 1:
        return votes[0]
    # Create dictionary to store key/value pairs of names and their vote count.
    vote_tally = {}

    # Loop over list, check to see if name (as a key) exists in the dictionary. If it doesn't, add it as a new key and add 1 as its starting value. If it does, increase the value by 1.

    # Edge case: If some names have uppercase and some lower case -- convert all entries to lowercase.

    for name in votes:
        if name.lower() in vote_tally:
            vote_tally[name.lower()] += 1
        else:
            vote_tally[name.lower()] = 1

    # Loop through the completed dictionary's values, and return the key with the highest number. If two names have an equal amount of votes, compare their names. Whomever's name comes last alphabetically is the winner.


    highest_count = 0
    winner = ""

    for name, count in vote_tally.items():
        if count == highest_count:
            winner = name if name > winner else winner
        elif count > highest_count:
            highest_count = count
            winner = name
    
    return winner

    # Return the name of the person with the highest number of votes

count_votes(['veronica', 'mary', 'alex', 'james', 'mary', 'michael', 'alex', 'michael'])