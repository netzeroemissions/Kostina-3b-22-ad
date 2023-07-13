class Pupil:
    def __init__(self, name, school_class):
        self.name = name
        self.school_class = school_class

    def study(self):
        print('Школьник ', self.name, ' учится')

pupil = Pupil('Илья', 9)
pupil.study()