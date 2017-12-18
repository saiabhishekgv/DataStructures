class Allergies(object):
    d = {}

    def __init__(self, score):
        self.d = {}
        score = score%256
        list_of_allergies = ['eggs', 'peanuts', 'shellfish', 'strawberries' ,'tomatoes' ,'chocolate' ,'pollen' ,'cats']
        counter = 0
        while score>0 :
            if score%2 == 1:
                self.d[list_of_allergies[counter]] = True
            counter += 1
            score = score/2

    def is_allergic_to(self, item):
        return self.d[item] if item in self.d else False

    @property
    def lst(self):
        return [i for i in self.d.keys() if self.d[i]==True ]
