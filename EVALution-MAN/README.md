# EVALution-Man

EVALution-MAN consists of two datasets containing word-relation-word: (i) (one)[http://] including the word-pairs extracted from the Chinese Wordnet (CWN); (ii) the (other)[http://] containing the word-pairs extracted from the elicitation task.

Details about the dataset can be found in the following papers:

* Liu, Hongchao, Karl Neergaard, Enrico Santus and Chu-Ren Huang. "EVALution-MAN: A Chinese Dataset for the Training and Evaluation of DSMs". LREC 2016.

* Liu, Hongchao and Chu-Ren Huang. "Mandarin Relata: A Dataset of Word Relations and Their Semantic Types". 2017. 第十八届汉语词汇语义学国际研讨会, 2017. 05.18-20, 乐山师范学院。



## Getting Started

Word-pairs extracted from CWN represent Taiwan Mandarin, while word-pairs captured through elicitation task represents Mainland Mandarin (all subject involved in the task were from Mainland China).

All the word-pairs are validated by human raters. The volunteers were told to rate the word relation according to five options: “totally agree”, “agree”, “don’t know”, “disagree”, “totally disagree”. If the participants did not know either of the target vocabulary they were given the choice of, “don’t know X” and “don’t know Y” respectively.



## Development

1. Relations extracted from CWN (Taiwan Mandarin) are saved in (FromCWN_TaiwanMandarin.txt)[https://github.com/esantus/EVALution/blob/master/EVALution-MAN/FromCWN_TaiwanMandarin.txt]. Three human raters were involved in the judgement of their reliability. Only pairs that received at least two "agree" (or “totally agree”) votes are considered in the dataset. They are formatted in 14 columns:
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


2. Relations from the elicitation task (Mainland Mandarin) are saved in (FromElicitation_MainlandMandarin.txt)[https://github.com/esantus/EVALution/blob/master/EVALution-MAN/FromElicitation_MainlandMandarin.txt]. Each pair is validated by five subjects: only pairs that received three or more “agree” (or “totally agree”) votes are considered in the dataset. They are formatted in 12 columns, as part of speech is not present for this dataset:
*	ID
*	Target word
*	Relation
*	Related word
*	Explanation of the relation
**	totally agree
**	agree
**	don’t know
**	disagree
**	totally disagree
**	don’t know X
**	don’t know Y

For word relations extracted from elicitation task, each pair is validated by five subjects (not three any more). Only ones received three or more votes from “agree” or “totally agree” can be treated as positive pairs and put into the dataset.


## Note

We strongly suggest not to merge the two datasets, as they come from different sources and represent different types of Mandarin.






 




## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc