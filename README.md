What is this
-----
Basic reader and searcher for entities and individuals on the EU, UN and OFAC sanction lists.

See */reader.py for basic read methods  
See eu_global/reader.py for a basic search method

How to run it
-----
Requires python3, and the pip-modules 
fuzzywuzzy, Fuzzy, python-Levenshtein, and lxml, installed.

    $ cd eu_global
    $ python3 searcher.py

Search method
-----
There are different strategies for achieving this task, and there seems to be a common pattern among vendors for OFAC and other sanction list software implement fuzzy name search.  

Procedure:

Pre-compute a mapping of phonetic lookup-keys from normalized names in list sources, split into names-part, to generate a map from KEY (from name-part) -> list of list entry-ids.

Example of normalizing a name, and splitting it into name parts: "Jenny-Margot Åhlen" -> "jenny, margot, ahlen".

First, determine the phonetic lookup-keys from the input name (the query). 
Then, build a list of candidate list-entry matches using entry-ids from the phonetic lookup-key matches
Filter this list by using a string similarity algorithm, with normalized similarity ratio output. 
Add or subtract to the similarity ratio depending on various properties, to rank the match up or down.
Example: if not all name parts from the query matches all name parts of the list subject, apply a penalty.   

Filter matches by applying a user-defined minimum threshold for similarity ratio, e.g. 0.80   
 


References
---- 
- https://www.treasury.gov/resource-center/sanctions/SDN-List/Pages/fuzzy_logic.aspx -- see item 4

- https://easyofac.com/#desc –- heading "Layered fuzzy search"
