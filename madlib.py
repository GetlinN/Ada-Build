#MadLib Assignment

# list to store parts of speech in order to fill in MadLib
PARTS_OF_SPEECH = [
                   'name',
                   'number',
                   'adjective',
                   'space of apartment/house',
                   'clothing',
                   'music style',
                   'body part',
                   'language'
                   ]

# dictionary to store user input
user_dict = {}

print("." * 145)
print("Welcome to my MadLib program. Please enter in some information below: \n")

# loop to prompt the user for input
for part in PARTS_OF_SPEECH:
    user_dict[part] = input(f'Enter {part} --> ')

# # loop to prompt the user for input
# for part in parts_of_speech:
#   word = input(f'Please enter {part}: ')
#   parts_of_speech_and_words[part] = word

print(user_dict)

text = f"""

The best way to survive the CORONA virus.

The best way to stay healthy and calm during those tough days is to repeat this mantra {user_dict['number']} times per day. 
Find the quite {user_dict['adjective']} place in your home. You might consider the {user_dict['space of apartment/house']}. 
Put on your favorite {user_dict['clothing']}.
Turn on {user_dict['music style']} music. Before starting make some warm-up and exercises.Raise your {user_dict['body part']} up.
Then spin around and shout out \"{user_dict['name']}\" {user_dict['number']} times. Now you are ready for mantra. You have to say
this mantra in {user_dict['language']}: “Dear Lord, I want me and my family to stay healthy and I want peace and
prosperity to all nations.')

"""

print(text)