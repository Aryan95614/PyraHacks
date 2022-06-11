import PySimpleGUI as sg
import sys


class Window():

    def c(self, elems):
        return (sg.Stretch(), *elems, sg.Stretch())

    def __init__(self):

        self.changing = lambda x, y: y if self.events[x] else 0
        self.events = None
        sg.theme('DarkGrey3')
        self.disease = "Spina bifida"

        self.layout = [

            [self.c([sg.Text(f"Disease: {self.disease}")])],

            [self.c([sg.MLine(default_text='', size=(35, 5)), sg.Text(f"What do you know about {self.disease}")])],
            self.c([sg.Frame("Basic Information", [[
                sg.Text("Spina bifida is the incomplete formation of \n the spine and spinal cord in utero. It can cause the spinal cord and nerves to be exposed on the surface of the back, \n instead of being inside a canal \nof bone surrounded by muscle.\
People with spina bifida experience a range of mild to severe\n physical disabilities including paralysis or weakness in the legs, bowel and bladder incontinence, \n hydrocephalus (too much fluid in the brain cavities),\n deformities of the spine, and learning difficulties.\
The cause of spina bifida is not well understood, \nbut it is likely caused by genetic and environmental factors. Adequate intake of folate by the mother\n in early pregnancy has been found to be a significant factor in preventing a child \ndeveloping spina bifida."
                        ),
            ]])]),
            self.c([sg.Frame(layout=[
                [sg.CBox(f"Weakness", size=(10, 1)),
                 sg.CBox(f"Paralysis of the Lungs", default=False)],
                [sg.CBox(f"Loss of Skin Sensation", size=(10, 1)),
                 sg.CBox(f"Can't feel the temp", default=False)]],
                title=f'Symptoms of {self.disease}',
                title_color='orange',
                relief=sg.RELIEF_SUNKEN),
                sg.Frame(layout=[[
                    sg.Text("https://www.nhs.uk/conditions/spina-bifida/")]],
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
