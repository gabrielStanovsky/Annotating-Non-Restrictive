from read_conll_trees import create_dep_trees_from_stream, create_predicted_dep_trees_from_stream


class Classifier:
    def __init__(self, treesFile, state):
        self.treesFile = treesFile
        self.setStatus(state)
        
    def setStatus(self, newStatus):
        self.state = newStatus
        if newStatus == 'GOLD':
            self.trees = [t for t in create_dep_trees_from_stream(open(self.treesFile))]
        elif newStatus == 'PREDICTED':
            self.trees = [t for t in create_predicted_dep_trees_from_stream(open(self.treesFile))]
        else:            
            raise Exception
    
    
    @staticmethod
    def parseCorpusFile(corpusFile):
        ret = []
        for line in open(corpusFile):
            data = line.strip().split('\t')
            (sentInd, nodeIndex) = map(int, data[:2])
            val = data[2]
            candidateType = data[3]
            tags = data[4:]
            ret.append((sentInd, nodeIndex, val, candidateType, tags))
        return ret
    
    def train(self, trainFile, featuresFile):
        data = []
        with open(featuresFile, 'w') as fout:
            for (sentInd, nodeIndex, val, candidateType, _) in Classifier.parseCorpusFile(trainFile):
                feats = self.extractFeatures(sentInd, nodeIndex, candidateType)
                data.append((feats, val))
                fout.write('{0}\n'.format(join_str('\t', [sentInd, nodeIndex, val, candidateType] + feats)))    
        self._train(data)
        
        
    def classify(self, testFile, outputFile):
        with open(outputFile, 'w') as fout:
            for (sentInd, nodeIndex, val, candidateType, _) in Classifier.parseCorpusFile(testFile):
                feats = self.extractFeatures(sentInd, nodeIndex, candidateType)
                predicted = self._classify(feats)
                fout.write('{0}\n'.format(join_str('\t', [sentInd, nodeIndex, val, candidateType, predicted])))
    
    
    def extractFeatures(self, sentInd, nodeIndex, candidateType):
        return self._extractFeatures(self.trees[sentInd], nodeIndex + 1, candidateType)
    
    ## Should be implemented by the inheriting class
    
    def _train(self, data):
        raise Exception()
    
    def _classify(self, data):
        raise Exception()
    
    def _extractFeatures(self, tree, nodeIndex, candidateType):
        raise Exception()
                
def join_str(s, ls):
    return s.join(map(str, ls))

    
    
