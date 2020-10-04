# Speech recognition analysis

```
A MacBook Pro with 2.7 GHz Dual-Core Intel Core i5 and 8 GB 1867 MHz DDR3 (2015) was used.
```

## Informations

- - -

### word analyzed 
 - "bed" 
 
Quantity : 495 items.
> It's a difficult word for the recognizer, because there is similarity with "bad".

### phrases analyzed 
 - "find the function called ABC"
 - "write a function called square with parameter number"

### Problems
Depending on the pronunciation and intonation, the recognizer makes serious mistakes like: "bad","bat, even "ted" but, using:
```python
recognizer.recognize_google(audio, show_all = True) 
```
It's possible to verify all the words that the recognizer considered to be, being able to correct this recognition error.

#### Exceptions
"WDU" means - "we don't understand". I used try/except for treat some errors.


## Analysis

- - -

1. USING GOOGLE RECOGNIZER:

#### Words test

infos            | first test                 | second test
-----------------|----------------------------|------------------------
Runtime in min   | 5.8215179721514385 minutes | 5.638539000352224 minutes
"WDU" percentage | 53.333333333333336 %       | 53.333333333333336 %
"bed" percentage | 39.595959595959596 %       | 39.5959595959596 %

#### Phrases test: 
>>>> RECOGNIZE ALL PHRASES PERFECTLY!!

### Conclusion
This recognizer, in the free version, has a limit of 50 calls per day, despite having a so good efficiency, this version does not cover for large jobs. But still, it would be a good option if we wanted to buy your services.

- - -

2. USING SPHINX RECOGNIZER:

#### Words test

infos            | first test                 | second test
-----------------|----------------------------|------------------------
Runtime in min   | 5.83098038037618  minutes  | 5.7492130001386  minutes
"WDU" percentage | 88.08080808080808  %       | 88.08080808080808  %
"bed" percentage | 7.6767676767676765 %       | 7.6767676767676765 %

#### Phrases test: 
SERIOUS PROBLEMS FOR RECOGNIZING PHRASES


### Conclusion
This recognizer presents problems in recognizing words and phrases because it's offline. The identified words didn't  have good results with what was expected. For example, the word "bed" has been recognized as "ted" in several situations, even the phrases have brought these results:
 - "i'm not function called the beast" 
 - "i can function columns where we store owner and no"


3. USING WIT.AI RECOGNIZER:

infos            | first test                 | second test
-----------------|----------------------------|------------------------
Runtime in min   | 13.939008700847626 minutes | 13.848593048586970 minutes
"WDU" percentage | 46.041666666666664         | 46.041666666666664
"bed" percentage | 15.625 %                   | 15.625 %

#### Phases test: 
SHOW A SMALL ERROR AT THE END OF THE SECOND SENTENCE

### Conclusion
 This recognizer, although it takes longer time to access a server,
brings good results. It had more satisfactory results when analyzing words than the google recognizer, which until now was the winner in percentages, and presents a version totally free - which can be associated with github, even from several people -. However, some phrases can contain little problems in recognition. For example, the phrases were recognized as:
 - 'find a function called ABC',
 - 'write a function called square with jeremy random but

The first was totally successful, but the second one wasn't.