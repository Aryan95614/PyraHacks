import PySimpleGUI as sg
import sys


class Window():

    def c(self, elems):
        return (sg.Stretch(), *elems, sg.Stretch())

    def __init__(self):

        self.changing = lambda x, y: y if self.events[x] else 0
        self.events = None
        sg.theme('DarkGrey3')
        self.disease = "Spinal cord injury"
        self.layout = [

            [self.c([sg.Text(f"Disease: {self.disease}")])],

            [self.c([sg.MLine(default_text='', size=(35, 5)), sg.Text(f"What do you know about {self.disease}")])],
            self.c([sg.Frame("Basic Information", [[
                sg.Text("The spinal cord can become injured if too much pressure is applied and/or \n if the blood and oxygen supply to the spinal cord is cut. When the spinal cord has been damaged, \nit leads to a loss of function such as mobility or feeling.\
For some people, a spinal cord injury results in paraplegia \n(loss of function below the chest), for others it leads to quadriplegia \n(loss of function below the neck).\
Accidents account for 79% of spinal cord injuries in \nAustralia – mostly caused by motor vehicle accidents and falls. Other causes include cancer, arthritis, infections, \nblood clots, and degenerative spinal conditions.")
            ]])]),
            self.c([sg.Frame(layout=[
                [sg.CBox(f"Loss of Function", size=(10, 1)),
                 sg.CBox(f"Trauma", default=False)],
                [sg.CBox(f"Mobility", size=(10, 1)),
                 sg.CBox(f"Teritary issues", default=False)]],
                title=f'Symptoms of {self.disease}',
                title_color='orange',
                relief=sg.RELIEF_SUNKEN),
                sg.Frame(layout=[[
                    sg.Text("https://www.shepherd.org/patient-programs/\nspinal-cord-injury/about#:~:text=A%20spinal%20cord%20injury%20(SCI,Friedreich's%20ataxia%2C%20etc.).")]],
                    title='Learn more from these links ',
                    title_color='orange',
                    relief=sg.RELIEF_SUNKEN)]),

            [self.c([sg.Button('Ok')])]]

        self.window = sg.Window(f'Learn about {self.disease}', self.layout, size=(800, 400), resizable=True, finalize=True)

    def play(self):
        true = True
        while True:

            event, values = self.window.read()
            if values != None:
                self.events = list(values.values())

            if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
                break

window= Window()
window.play()

