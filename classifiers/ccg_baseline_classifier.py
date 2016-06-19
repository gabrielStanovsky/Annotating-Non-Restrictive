from Classifier import Classifier
from Tester import Tester

class CCGBaselineClassifier(Classifier):
    def _extractFeatures(self, tree, nodeIndex, candidateType):
        indBefore = min(tree[nodeIndex].get_subtree()) - 1
        if indBefore < 1:
            return [False]
        
        return [tree[indBefore].word == ',']
    
    def _classify(self, data):
        return (1 if data[0] else 0)
    
    


   
