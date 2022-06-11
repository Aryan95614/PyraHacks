import PySimpleGUI as sg
import sys


class Window():

    def c(self, elems):
        return (sg.Stretch(), *elems, sg.Stretch())

    def __init__(self):

        self.changing = lambda x, y: y if self.events[x] else 0
        self.events = None
        sg.theme('DarkGrey3')
        self.disease = "Acquired brain injury"
        self.layout = [

            [self.c([sg.Text(f"Disease: {self.disease}")])],

            [self.c([sg.MLine(default_text='', size=(35, 5)), sg.Text(f"What do you know about {self.disease}")])],
            self.c([sg.Frame("Basic Information", [[
                sg.Text("Acquired brain injuries are due to damage that happens to the brain after birth.\n They can be caused through a wide range of factors including a blow to the head, stroke, alcohol or drugs, infection, disease such as AIDs or cancer, or a lack\n of oxygen.\
It is common for many people with a brain injury to have trouble \n processing information, planning, and solving problems. They may also experience changes to their behaviour and personality, physical and sensory abilities, or thinking \nand learning.")
            ]])]),
            self.c([sg.Frame(layout=[
                [sg.CBox(f"Weakness", size=(10, 1)),
                 sg.CBox(f"Shakeness", default=False)],
                [sg.CBox(f"Stiffness", size=(10, 1)),
                 sg.CBox(f"Poor Balence", default=False)]],
                title=f'Symptoms of {self.disease}',
                title_color='orange',
                relief=sg.RELIEF_SUNKEN),
                sg.Frame(layout=[[
                    sg.Text("https://www.healthdirect.gov.au/acquired-brain-injury-abi")]],
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

            if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Ok':  # if user closes window or clicks cancel
                sys.exit()

window= Window()
window.play()

