import PySimpleGUI as sg
import sys


class Window():

    def c(self, elems):
        return (sg.Stretch(), *elems, sg.Stretch())

    def __init__(self):

        self.changing = lambda x, y: y if self.events[x] else 0
        self.events = None
        sg.theme('DarkGrey3')
        self.disease = "Cerebral palsy"
        self.layout = [

            [self.c([sg.Text(f"Disease: {self.disease}")])],

            [self.c([sg.MLine(default_text='', size=(35, 5)), sg.Text(f"What do you know about {self.disease}")])],
            self.c([sg.Frame("Basic Information", [[
                sg.Text("Cerebral palsy is typically due to an injury\n to the developing brain before or during birth, caused by a reduced \nblood supply and lack of oxygen to the brain.\
Illnesses \nduring pregnancy such as rubella (the German measles), accidental injury to the brain, meningitis in young children, and premature birth can all be causes.In Australia, over 90% of cerebral \n \
palsy was due to a brain injury while the mother was pregnant, or before one month of age, \nhowever, 10% of people develop the disability later in life, usually as a result of \
infections\n such as meningitis or encephalitis, stroke, or a severe head\n injury (Cerebral Palsy Alliance).")
            ]])]),
            self.c([sg.Frame(layout=[
                [sg.CBox(f"Stiff Muscles", size=(10, 1)),
                 sg.CBox(f"Variations in muscle tone", default=False)],
                [sg.CBox(f"Lack of balance", size=(10, 1)),
                 sg.CBox(f"Tremors or jerky involuntary movements", default=False)]],
                title=f'Symptoms of {self.disease}',
                title_color='orange',
                relief=sg.RELIEF_SUNKEN),
                sg.Frame(layout=[[
                    sg.Text("https://www.mayoclinic.org/diseases-conditions/cerebral-palsy/symptoms-causes/syc-20353999")]],
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

