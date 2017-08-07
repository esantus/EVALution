# EVALution-Man

EVALution-MAN consists of two datasets containing word-relation-word: (i) [one](https://github.com/esantus/EVALution/blob/master/EVALution-MAN/FromCWN_TaiwanMandarin.txt) including the word-pairs extracted from the Chinese Wordnet (CWN); (ii) the [other](https://github.com/esantus/EVALution/blob/master/EVALution-MAN/FromElicitation_MainlandMandarin.txt) containing the word-pairs extracted from the elicitation task.

Details about the dataset can be found in the following papers:

* Liu, Hongchao, Karl Neergaard, Enrico Santus and Chu-Ren Huang. "EVALution-MAN: A Chinese Dataset for the Training and Evaluation of DSMs". LREC 2016.

* Liu, Hongchao and Chu-Ren Huang. "Mandarin Relata: A Dataset of Word Relations and Their Semantic Types". 2017. 第十八届汉语词汇语义学国际研讨会, 2017. 05.18-20, 乐山师范学院。



## Getting Started

Word-pairs extracted from CWN represent Taiwan Mandarin, while word-pairs captured through elicitation task represents Mainland Mandarin (all subject involved in the task were from Mainland China).

All the word-pairs are validated by human raters. The volunteers were told to rate the word relation according to five options: “totally agree”, “agree”, “don’t know”, “disagree”, “totally disagree”. If the participants did not know either of the target vocabulary they were given the choice of, “don’t know X” and “don’t know Y” respectively.



## Development

1. Relations extracted from CWN (Taiwan Mandarin) are saved in [FromCWN_TaiwanMandarin.txt](https://github.com/esantus/EVALution/blob/master/EVALution-MAN/FromCWN_TaiwanMandarin.txt). Three human raters were involved in the judgement of their reliability. Only pairs that received at least two "agree" (or “totally agree”) votes are considered in the dataset. They are formatted in 14 columns:
*	ID
*	Relation
*	Target word
*	Part of speech of the target word
*	Related word
*	Part of speech of the related word
*	Explanation of the relation
*	totally agree
*	agree
*	don’t know
*	disagree
*	totally disagree
*	don’t know X
*	don’t know Y


2. Relations from the elicitation task (Mainland Mandarin) are saved in [FromElicitation_MainlandMandarin.txt](https://github.com/esantus/EVALution/blob/master/EVALution-MAN/FromElicitation_MainlandMandarin.txt). Each pair is validated by five subjects: only pairs that received three or more “agree” (or “totally agree”) votes are considered in the dataset. They are formatted in 12 columns, as part of speech is not present for this dataset:
*	ID
*	Target word
*	Relation
*	Related word
*	Explanation of the relation
*	totally agree
*	agree
*	don’t know
*	disagree
*	totally disagree
*	don’t know X
*	don’t know Y


## Note

We strongly suggest not to merge the two datasets, as they come from different sources and represent different types of Mandarin.
