# Wordle Solver

This is a solver of wordle.

It solves with in average 3.9 attemps.

The word with the highest entropy is selected each guess.

The calculation of the average information content is based on the following article by xcloche.
https://xcloche.hateblo.jp/entry/2022/01/24/212558

As a solver, I take a greedy approach, submitting as an answer the word with the highest average information content from the set of words that would satisfy the hints obtained so far for each answer.

Note that this does not automate Wordle responses.

The vocabulary has been extracted directly from Wordle, but I will not disclose it just in case.

## Best words for start TOP 30

|word|entropy|
|-|-|
|tares|6.194052544375447|
|lares|6.149918742453126|
|rales|6.114343099454228|
|rates|6.096242642514601|
|teras|6.076619177276175|
|nares|6.066830765753896|
|soare|6.06139539909626|
|tales|6.0549877614011915|
|reais|6.049777632888326|
|tears|6.032338670239807|
|arles|6.029656532378517|
|tores|6.018294372182982|
|salet|6.016842875398263|
|aeros|6.013480318472078|
|dares|6.010334729949005|
|saner|5.999263329266238|
|reals|5.999162055397663|
|lears|5.98878209988576|
|lores|5.9769685645714645|
|serai|5.9736171680399535|
|lanes|5.971303767248142|
|laers|5.968985947815137|
|pares|5.9673459921147165|
|cares|5.966406181817172|
|tires|5.963365144184274|
|saine|5.9626492880845205|
|seral|5.953595576828302|
|mares|5.951777451541269|
|reans|5.950810301312467|
|aloes|5.9447087524871405|

## Best pokemons for start POKEMON WORDLE

https://wordle.mega-yadoran.jp/

|ポケモン|エントロピー|
|-|-|
|ジーランス|3.833357807876867|
|ネンドール|3.8055146262573065|
|ランクルス|3.765614591060905|
|ルナトーン|3.7110582164124875|
|ムーランド|3.6886931751565712|
|グラードン|3.684719044565323|
|レントラー|3.6519727405726994|
|ドータクン|3.6197563396616097|
|エルフーン|3.6052426653523555|
|ヒードラン|3.572299697169144|