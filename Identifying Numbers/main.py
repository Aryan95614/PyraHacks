class phone:

    def __init__(self, iphone_or_Android, ios ):
        self.phoneType = iphone_or_Android
        self.ios = ios

    def identify(self):
        print(f'This is an {self.phoneType} and the ios of it is {self.ios}')



while True:
    iphone_or_Android = None
    ios = None

    type = input('Do you have an iphone or android?[Iphone][Android]: \t')
    ios = input('What is the ios of the software: \t')
    Phone = phone(iphone_or_Android=iphone_or_Android, ios=ios)
    Phone.identify()
