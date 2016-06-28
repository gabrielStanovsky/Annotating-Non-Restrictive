# Annotating-Non-Restrictive
Code, models, and corpus of non-restrictive noun phrase modifications.  
Published in "[Annotating and Predicting Non-Restrictive Noun Phrase Modifications](https://www.cs.bgu.ac.il/~gabriels/acl_16_long.pdf)" (Stanovsky and Dagan, ACL 2016)

Generating the corpus
---------------------

To get the annotated corpus, you'll first need to obtain the CoNLL 2009 train corpus (CoNLL2009-ST-English-train.txt).

Once you get it, run:
'''generateCorpora CoNLL2009-ST-English-train.txt'''
This will generate the corpus (train, dev and test splits) in the "corpus" directory.

Corpus format
-------------
The corpus will be generated in the corpus directory.
Each CoNLL token will contain these additional two fields:   

1. Restrictiveness, which has the following possible values:
       * **RSTR**, marking that this is a restrictive modifier.
       * **NON-RESTR**, marking that this is non-restrictive modifier.
       * **-**, which marks that this token is not annotated.

2. Modifier Type, marking the type of this modifier. Has the following possible values (see paper for example and evaluation):
      * **_** -- this token is not a modifier.
      * **APPOS-MOD *-- Appositional modifier.
      * **INF-MOD** -- Infinitival modifier.
      * **POSTADJ-MOD **-- Postfix adjectival modifier.
      * **PP-MOD** -- Prepositional modifier.
      * **PREADJ-MOD **-- Prefix adjectival modifier.
      * **PREVERB-MOD **-- Prefix verbal modifier.
      * **RC-MOD** -- Relative Clause modifier.



Other files in this repo
------------------------

- classifiers: Contains the code for the classifiers described in the paper.

- diffs: The diff files which, in conjunction with the CoNLL data, generates our annotated corpus.

- features: The CRF features for each of the training instances, used to train both CRF models.

- models: pre-trained models, acheiving the results described in the paper.

