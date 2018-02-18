class Statistics:
    def __init__(self, p_count, tb_count, f_count, b_count):
        self.poring_count = p_count
        self.thief_bug_count = tb_count
        self.familiar_count = f_count
        self.butylka_count = b_count

    def show_statistics(self):
        print("Poring killed:" + str(self.poring_count))
        print("Thief bugs killed: " + str(self.thief_bug_count))
        print("Familiar killed: " + str(self.familiar_count))
        print("Butylka found: " + str(self.butylka_count))

    def increase_poring(self, c):
        self.poring_count += c

    def increase_thiefbug(self, c):
        self.thief_bug_count += c

    def increase_familiar(self, c):
        self.familiar_count += c

    def increase_butylka(self, c):
        self.butylka_count += c

    def save(self):
        pass
