from classifier import Classifier  
from sklearn.metrics import precision_recall_fscore_support
import numpy as np
from match_pb_with_qasrl import dictAppendRec
import csv

class Tester:
    def __init__(self):
        pass
    
    def reportAnnots(self, candidateType, gold, predicted, convertLabel = int):
        gold = map(convertLabel, gold)
        predicted = map(convertLabel, predicted)
        assert len(gold) == len(predicted) 
        return [candidateType] + map(str, [len(gold)] + list(precision_recall_fscore_support(np.array(gold), np.array(predicted), average = 'binary'))[:-1])

    def evaluate(self, predicted, outputFile, gold = None):
        
        if gold is None:
            self.predicted = Classifier.parseCorpusFile(predicted)
            goldAnnots = [ls[2] for ls in self.predicted]
            predictedAnnots = [ls[4][0] for ls in self.predicted]
            candidateTypes = [ls[3] for ls in self.predicted]
            
            d = {}
            
            with open(outputFile, 'wb') as fout:
                writer = csv.writer(fout, delimiter = ',')
                writer.writerow(['Modifier type', '#instances', 'P', 'R', 'F1'])
            
                for (candidateType, (goldAnnot, predicatedAnnot)) in zip(candidateTypes, zip(goldAnnots, predictedAnnots)):
                    if candidateType not in d:
                        d[candidateType] = [[],[]]
                    d[candidateType][0].append(goldAnnot)
                    d[candidateType][1].append(predicatedAnnot)
                    
                
                for row in sorted([self.reportAnnots(candidateType, annots[0], annots[1]) for (candidateType, annots) in d.items()], key = lambda row: int(row[1]), reverse = True):
                    writer.writerow(row)
            
                finalRow = self.reportAnnots('total', goldAnnots, predictedAnnots)
                print finalRow
                writer.writerow(finalRow)
        else:
            self.predicted = Classifier.parseCorpusFile(predicted)
            self.gold = Classifier.parseCorpusFile(gold)
            goldAnnotsDic = dict([('{0}_{1}'.format(ls[0], ls[1]), ls[2]) for ls in self.gold])
            predictedAnnotsDic = dict([('{0}_{1}'.format(ls[0], ls[1]), ls[4][0]) for ls in self.predicted])
        
            goldAnnots = []
            predictedAnnots = []      
            for k, v in goldAnnotsDic.items():
                goldAnnots.append(v)
                if k in predictedAnnotsDic:
                    predictedAnnots.append(predictedAnnotsDic[k])
                else:
                    predictedAnnots.append('0')
            
            for k,v in [(k, v) for (k, v) in  predictedAnnotsDic.items() if (k not in goldAnnotsDic)]:
                predictedAnnots.append(v)
                goldAnnots.append('0')
            
            print self.reportAnnots('total', goldAnnots, predictedAnnots)
        
        
        
        
        
    
        
if __name__ == '__main__':
    t = Tester()
    t.evaluate('../predicted/test')