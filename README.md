# NLP Preprocess Tools
This is a curated list of samples on NLP preprocessing. You are welcome to make a pull request to contribute!

## Tools
### Extraction
#### In Between Two Characters
* [Extract Text In Between](https://github.com/yhuag/NLP-preprocess-tools/tree/master/basics/01_extract_text_in_between)
#### Single Deletion Pairs
* [Extract Word Pair](https://github.com/yhuag/NLP-preprocess-tools/tree/master/single-deletion/extract-word-pair)
: Extract special word pairs from a group of word pairs (e.g. French, Italian, Portuguese, Spanish, Turkish). The word pair should match the following requirements:
    1. Single deletion distance
    2. Deletion at the exact center of the word
    > Example. `(bloccare, blocare) and (fellah, felah)` \
    Incorrect example. `(vitamină, vitamin) and (maxi, maksi)`

* [Extract Word Pair (Cognate)](https://github.com/yhuag/NLP-preprocess-tools/tree/master/single-deletion/extract-word-pair-cognate) : Extract special word pairs from a group of word pairs (e.g. French, Italian, Portuguese, Spanish). The word pair should match the following requirements:
    1. Being a cognate pair
    2. Single deletion distance
    > Example. `(veni, venir) and (rosmarin, romarin)` \
    Incorrect example. `(hanorac, anorak) and (msingur, singolo)`
