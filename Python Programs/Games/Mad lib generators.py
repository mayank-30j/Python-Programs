# This is a madlib game

# importing a module
from tkinter import *

# Creating a GUI window
frame = Tk()
frame.geometry('450x300')
frame.title('This is a mad lib generator game')
Label(frame, text='Have fun playing this game', font='arial 20 bold').pack()
Label(frame, text='Click any one', font='arial 10 italic').place(x=100, y=100)


# Creating a function for mad lib generator
def madlib1():
    animal = input('Enter any animal name: ')
    profession = input('Enter any profession: ')
    cloth = input('Enter any cloth name: ')
    name = input('Enter any name: ')
    place = input('Enter any name of a place: ')
    verb = input('Enter any verb: ')
    food = input('Enter any food name: ')
    thing = input('Enter any thing name (say like any dress or a watch) : ')
    print('say ' + food + ', the photographer said as the camera flashed! ' + name
     + ' and I had gone to ' + place + ' to get our photos taken on my birthday. '
    + 'The first photo we really wanted was a picture of us dressed as ' + animal + ' pretending to be a ' + profession
    + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + thing + ' wearing '
          + cloth + ' and ' + verb + ' --exactly what I had in mind')


def madlib2():
    business_name = input('Enter any animal name: ')
    cloth = input('Enter any cloth name: ')
    name = input('Enter any name: ')
    place = input('Enter any name of a place: ')
    verb = input('Enter any verb: ')
    thing = input('Enter any thing name (say like any dress or a watch) : ')
    print('Once a ' + business_name + ', co-founder ' + name + 'was going for business trip'
     + ' and I had gone to ' + place + ' to get our photos taken on my birthday. '
    + 'I remember him as a tall guy with a white beard' + ' pretending to be a ' + 'jobless man'
    + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + thing + ' wearing '
          + cloth + ' and ' + verb + ' --exactly what I had in mind')


Button(frame, text='The Photographer', font='arial 15', command=madlib1, bg='ghost white').place(x=60, y=120)
Button(frame, text='The Businessmen', font='arial 15', command=madlib2, bg='ghost white').place(x=60, y=120)
frame.mainloop()
