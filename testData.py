
class TestData(object):
    def __init__(self):
        f = open('anatomy_questions.csv','rt')
        reader = csv.reader(f)
        self.keys = []
        self.queDict = {}
        self.optADict = {}
        self.optBDict = {}
        self.optCDict = {}
        self.optDDict = {}
        for row in reader:
            key = row[0]
            self.keys.append(key)
            self.queDict[str(key)] = row[1]
            self.optADict[str(key)] = row[2]
            self.optBDict[str(key)] = row[3]
            self.optCDict[str(key)] = row[4]
            self.optDDict[str(key)] = row[5]
        f.close()
        
if __name__ == "__main__":
    import csv,re
    data = TestData()
    print "no of Questions"
    print len(data.keys)
    
