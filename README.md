# Annotating-Non-Restrictive
Code and models and corpus of non-restrictive noun phrase modifications.  
Published in "[Annotating and Predicting Non-Restrictive Noun Phrase Modifications](https://www.cs.bgu.ac.il/~gabriels/acl_16_long.pdf)" (Stanovsky and Dagan, ACL 2016)

Generating the corpus
---------------------

To get the annotated corpus, you'll first need to obtain the CoNLL 2009 train corpus (CoNLL2009-ST-English-train.txt).
Then, from the project's main directory, run:
'''generateCorpora CoNLL2009-ST-English-train.txt'''
This will generate the corpus (train, dev and test splits) in the "corpus" directory.

Other files in this repo
------------------------

- classifiers: Contains the code for the classifiers described in the paper.

- diffs: The diff files which, in conjunction with the CoNLL data, generates our annotated corpus.

- features: The CRF features for each of the training instances, used to train both CRF models.

- models: pre-trained models, acheiving the results described in the paper.

