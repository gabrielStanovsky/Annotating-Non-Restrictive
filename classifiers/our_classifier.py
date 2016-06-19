from coling_baseline import ColingBaselineClassifier
from classifier import Classifier
from Tester import Tester
from parsers.spacy_parser import SpacyParserWrapper


def loadEmbs():
    d = {}
    with open('/home/gabis//host/deps.words') as fin:
        for line in fin:
            line = line.strip()
            data = line.split(' ')
            d[data[0]] = data[1:]
    return d
        

class OurClassifer(ColingBaselineClassifier):
    
    embs = loadEmbs()
    
#     parser = SpacyParserWrapper()
    
    
    def featCommaBefore(self, tree, nodeIndex):
        indBefore = min(tree[nodeIndex].get_subtree()) - 1
        ret = 'commaBefore='
        if indBefore < 1:
            return ret + '0'
        
        return ret + '1' if [tree[indBefore].word == ','] else ret + '0'
    
    
    def prefixFeats(self, prefix, feats):
        return [prefix + feat for feat in feats] 
    
    def _extractFeatures(self, tree, nodeIndex, candidateType):
        word = tree[nodeIndex].word.lower()
        baseFeats = ColingBaselineClassifier._extractFeatures(self, tree, nodeIndex, candidateType)
        parentInd = tree[nodeIndex].parent_id
        
        sent = ' '.join([tree[tok].word for tok in sorted(tree)[1:]])
        
        
        # parent feats
        parentFeats = self.prefixFeats('parent:',  
                                       ColingBaselineClassifier._extractFeatures(self, tree, parentInd, candidateType))
        
        
#         #ner
#         OurClassifer.parser.parse(sent)
#         nerLabel = OurClassifer.parser.getNERLabel(parentInd)
#         if nerLabel:
#             print 'added ner {0}'.format(nerLabel)
#             parentFeats.append('parent:ner=NER'.format(nerLabel))
        
        # type and comma
        newFeats = ['type=' + candidateType,
                    self.featCommaBefore(tree, nodeIndex),
                    ]
        
        # pobj
        for i,child in enumerate([child for child in tree[nodeIndex].children if child.parent_relation == 'PMOD']):
            newFeats.extend(self.prefixFeats('pobj{0}:'.format(i), 
                                             ColingBaselineClassifier._extractFeatures(self, tree, child.id, candidateType)))
            
         
#         for i, child in enumerate(tree):
#             nerLabel = OurClassifer.parser.getNERLabel(i-1)
#             if nerLabel in ['PERSON', 'ORG']:
#                 print 'added ner {0}'.format(nerLabel)
#                 newFeats.append('{0}:ner={1}'.format(nodeIndex - (i-1), nerLabel))
         
         
#         for i, child in enumerate(tree[nodeIndex].children):
#             nerLabel = OurClassifer.parser.getNERLabel(i)
#             if nerLabel:
#                 print 'added ner {0}'.format(nerLabel)
#                 newFeats.append('{0}:ner=NER'.format(i)) 
        
        
        feats =  baseFeats + parentFeats + newFeats
        
        feats += ['{0}|{1}={2}|{3}'.format('type', feat.split('=')[0], candidateType, feat.split('=')[1])
                                                 for feat in feats]
        
        
        if candidateType == 'Prepositive adjectival modifiers':
            if word.lower() in OurClassifer.embs:  
                feats += ['emb{0}={1}'.format(i, emb) for (i, emb) in enumerate(OurClassifer.embs[word.lower()])]
         
        
        return feats
    


    

    
    
    
    
