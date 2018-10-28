from random import randint
 
class student:
    def __init__(self, l):
        names = ["Corentin","Erwin","Nils","Benjamin","Baptiste","Léo","Maxence","Minh Khieu"]
        self.name = names[randint(0,len(names)-1)]
        self.laps = [0]*l
    def getName(self):
        return self.name
    def setLapTime(self, lap, time):
        self.laps[lap] = time
    def getLapTime(self, lap):
        return self.laps[lap]
    def getTotalTime(self):
        self.totalTime = 0
        for l in self.laps:
            self.totalTime += l
        return self.totalTime
 
 
def timerForm():
    nbStudents = int(input("Combien d'eleves ?: "))
    nbLaps = int(input("Combien de tours ?: "))
    Students = []
    for i in range(nbStudents):
        Students.append(student(nbLaps))
    for lap in range(nbLaps):
        print("Tour #{}".format(lap+1))
        for stu in Students:
            t = float(input("Quel temps a fait {} au tour #{}: ".format(stu.getName(), lap)))
            stu.setLapTime(lap,t)
    for s in Students:
        print("Temps total de {} en {} tours: {}".format(s.getName(), nbLaps, s.getTotalTime()))
timerForm()
