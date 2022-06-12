class phone:

    def __init__(self, iphone_or_Android, ios ):
        self.phoneType = iphone_or_Android
        self.ios = ios

    def identify(self):
        print(f'This is an {self.phoneType} and the ios of it is {self.ios}')
        if self.phoneType == 'Iphone':
            print('Do you know that Apple is the largest software and hardware based company!')
            print('The Latest iphones come with the latest embedded software and reinforced with cutting edge tech!')
            print('Moreover, the tech in the iphone is unparrelled due to its distinction within the os market.')
        if self.phoneType == 'Android':
            print(' The Android is the direct competitor to the Iphone and has the latest software by google!')
            print(' Android encompasses many phones from companies, furthermore, each of them improve the hardware and')
            print(' Software as much as they can, it really is impressive to know that even the top 100 companies are collabing')


List = []
while True:
    iphone_or_Android = None
    ios = None

    type = input('Do you have an iphone or android?[Iphone][Android]: \t')
    ios = input('What is the ios of the software: \t')
    Phone = phone(iphone_or_Android=type, ios=ios)
    Phone.identify()
    List.append(Phone)
    print(List)
