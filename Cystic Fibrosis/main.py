import PySimpleGUI as sg
import sys


class Window():

    def c(self, elems):
        return (sg.Stretch(), *elems, sg.Stretch())

    def __init__(self):

        self.changing = lambda x, y: y if self.events[x] else 0
        self.events = None
        sg.theme('DarkGrey3')
        self.disease = "Cystic Fibrosis"
        self.layout = [

            [self.c([sg.Text(f"Disease: {self.disease}")])],

            [self.c([sg.MLine(default_text='', size=(35, 5)), sg.Text(f"What do you know about {self.disease}")])],
            self.c([sg.Frame("Basic Information", [[
                sg.Text("Cystic fibrosis (CF) is an inherited genetic \n condition, which affects the body’s respiratory, digestive, \nand reproductive systems. \
It specifically affects\n the mucus and sweat\n glands in the body, causing mucus to be thick and sticky. In the case of the lungs, this can clog the air passages\n and trap bacteria causing lung damage and recurrent infections. \
                        A range of other symptoms are \ncaused by the effects of CF on other parts of the body, including sinus infections, liver damage, \ndiabetes, poor growth, diarrhoea, and infertility."),

            ]])]),
            self.c([sg.Frame(layout=[
                [sg.CBox(f"Persistent cough ", size=(10, 1)),
                 sg.CBox(f"Inflamed nasal passage", default=False)],
                [sg.CBox(f"Repeated lung infections", size=(10, 1)),
                 sg.CBox(f"Recurrent sinusitis", default=False)]],
                title=f'Symptoms of {self.disease}',
                title_color='orange',
                relief=sg.RELIEF_SUNKEN),
                sg.Frame(layout=[[
                    sg.Text("https://www.mayoclinic.org/diseases-conditions/cystic-fibrosis/symptoms-causes/syc-20353700")]],
                    title='Learn more from these links ',
                    title_color='orange',
                    relief=sg.RELIEF_SUNKEN)]),

            [self.c([sg.Button('Ok')])]]

        self.window = sg.Window(f'Learn about {self.disease}', self.layout, size=(800, 400), resizable=True,
                                finalize=True)

    def play(self):
        true = True
        while True:

            event, values = self.window.read()
            if values != None:
                self.events = list(values.values())

            if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
                break


window = Window()
window.play()
