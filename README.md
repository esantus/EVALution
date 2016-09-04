# EVALution
Dataset containing Semantic Relations and Metadata, for Training and Evaluating Distributional Semantic Models


WHERE TO FIND IT
Please explore the branches. Every version will be saved in a new branch, accordingly named.
- Version 1.0: https://github.com/esantus/EVALution/tree/EVALution_v1.0


Cite Us

The resource is freely available. If you use it, please cite the description paper:

- Enrico Santus, Frances Yung, Alessandro Lenci, and Chu-Ren Huang. 2015. EVALution 1.0: An Evolving Semantic Dataset for Training and Evaluation of Distributional Semantic Models. Proceedings of the 4th Workshop on Linked Data in Linguistics, Beijing.



Abstract

In this paper, we introduce EVALution 1.0, a dataset designed for the training and the evaluation of Distributional Semantic Models (DSMs). This version consists of almost 7.5K tuples, instantiating several semantic relations between word pairs (including hypernymy, synonymy, antonymy, meronymy). The dataset is enriched with a large amount of additional information (i.e. relation domain, word frequency, word POS, word semantic field, etc.) that can be used for either filtering the pairs or perform an in-depth analysis of the results. The tuples are initially extracted from a combination of ConceptNet 5.0 and WordNet 4.0, and subsequently filtered through automatic methods and crowdsourcing in order to ensure their quality. The dataset is freely downloadable1 .



Format of the Dataset

EVALution 1.0 is composed of two files:
  (1) RELATA.txt provides all the information about the relata (terms and multiword expressions); and
  (2) RELATIONS.txt provides all the information about the relations.
Both of them are structured in a column format, where subfields are separated by either commas or slashes.



RELATA.txt

This file contains the following fields:
  - relatum: this field is an uncapitalized lemma or a multiword expression (spaces in multiword expressions are represented with an underscore: e.g. north_carolina).
  - tags: this field contains a comma separated list of tags, with their frequency among the total number of annotators (e.g. "SUPERORDINATE_4/26,PLANT_1/26" stays for SUPERORDINATE was tagged by 4 subjects on 26, while PLANT by 1 on 26). NOTE: The reliability of the tags is low: we suggest you to rely only on tags that were judged at least twice.
  - frequency: this is an integer representing the frequency of the term in a combination of ukWac and Wackypedia (see the section CORPORA below for more information).
  - term-dominatPOS: this field contains the term with attached the dominant POS (the most frequent one in the abovementioned corpora). The POS tag is attached with an hyphen and it is represented by one of the following letters: j for adjective, n for noun and v for verb.
  - distribution of POS: every POS is provided with the number of occurrences in the abovementioned corpora (POS tagset is available here: http://wacky.sslmit.unibo.it/lib/exe/fetch.php?media=tagsets:ukwac_tagset.txt). POS are slash separated.
  - distribution of forms: we have also collected the inflections and the different capitalizations with their frequencies. Forms are slash separated.
  - distribution of POS and morphological information: a more detailed distribution of POS and morphological information (tagset is available here: http://wacky.sslmit.unibo.it/lib/exe/fetch.php?media=tagsets:ukwac_tagset.txt). Tags are slash separated.



RELATION.txt

This file contains the following fields:

 - first relatum: it is one of the relata in the file RELATA.txt
 - relation: it can be one of the following relations: Antonym, Synonym, IsA (hypernymy), PartOf (meronymy), MemberOf (meronymy), MadeOf (meronymy), Entailment, HasA (possession), HasProperty (attribute). For the definition of these relations, please refer to: https://github.com/commonsense/conceptnet5/wiki/Relations.
 - second relatum: it is one of the relata in the file RELATA.txt
 - tags: this field contains a comma separated list of tags, with their frequency among the total number of annotators (e.g. "CULTURE_1/5,EVENT_4/5" stays for CULTURE was tagged by 1 subject on 5, while PLANT by 4 on 5). NOTE: The reliability of the tags is low, as some subjects have tried to cheat; we suggest you to rely on tags that were judged at least twice.
 - sentence: this field contains a sentence that paraphrases the relation; this sentence was used in the crowdsourcing task to assess the quality of the relation.
 - distribution of votes: the next five columns are integers that represent the number of votes for each value, with reference to the sentence in the previous field: "strong disagreement" (the first one, value=1), "disagreement", "neutral", "agreement" and "strong agreement" (the last one, value=5).
 - agreement between subjects as reported by Crowdflower.
 - number of subjects who voted the agreement with the sentence.
 - average agreement of the subjects (in the range between 1="strongly disagree" and 5="strongly agree").
 - variance among the votes.
 - average agreement minus the variance.
 - source from which the pair was extracted.
 - score in the source, if available.



CORPORA USED FOR THE ANALYSIS

- ukWaC: a 2 billion word corpus constructed from the Web limiting the crawl to the .uk domain and using medium-frequency words from the BNC as seeds. The corpus was POS-tagged and lemmatized with the TreeTagger. The tagset is available here, more information can be found in this paper.
- WaCkypedia_EN: a 2009 dump of the English Wikipedia (about 800 million tokens), in the same format as PukWaC, including POS/lemma information, as well as a full dependency parse (parsing performed with the MaltParser). The texts were extracted from the dump and cleaned using the Wikipedia extractor.

You can find more information about the corpora in the following papers:
- M. Baroni, S. Bernardini, A. Ferraresi and E. Zanchetta. 2009. The WaCky Wide Web: A Collection of Very Large Linguistically Processed Web-Crawled Corpora. Language Resources and Evaluation 43(3): 209-226 (PDF).
- M. Baroni and S. Bernardini (eds.). 2006. Wacky! Working papers on the Web as Corpus. Bologna: GEDIT. (Webpage)
- A. Ferraresi. 2007. Building a very large corpus of English obtained by Web crawling: ukWaC. Master Thesis, University of Bologna (PDF)
- A. Ferraresi, E. Zanchetta, M. Baroni and S. Bernardini. 2008. Introducing and evaluating ukWaC, a very large web-derived corpus of English. In S. Evert, A. Kilgarriff and S. Sharoff (eds.) Proceedings of the 4th Web as Corpus Workshop (WAC-4) – Can we beat Google?, Marrakech, 1 June 2008. (PDF) (Webpage)
