from CanvasCourse import CanvasCourse

class CanvasList:
    def __init__(self):
        self.cDict = {}

    def addCourse(self, inst=None, auth=None, classCode=None):
        if str(classCode) not in self.cDict:
            self.cDict[str(classCode)] = CanvasCourse(str(inst), str(auth), str(classCode))
            return True
        else:
            return False

    def delCourse(self, classCode):
        if str(classCode) in self.cDict:
            del self.cDictstr[(classCode)]
            return True
        else:
            return False

    def getCourseList(self):
        return cDict

    def getCourse(self, classCode):
        if str(classCode) in self.cDict:
            return self.cDict[str(classCode)]
        else:
            return None
