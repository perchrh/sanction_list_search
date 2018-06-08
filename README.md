Print names and reference id for entities and individuals on the EU, UN and OFAC sanction lists.

See */reader.py for a basic read method

Thoughts on algorithms for fuzzy name matching
-----
There are different strategies for achieving this task, and there seems to be a common pattern among vendors for OFAC and other sanction list software implement fuzzy name search.  

Procedure:

Pre-compute a mapping of phonetic lookup-keys from normalized names in list sources, split into names-part, to generate a map from KEY (from name-part) -> list of list entry-ids
Example of normalizing the name, and splitting it into name parts: "Jenny-Margot Åhlen" -> "jenny, margot, ahlen"
For the input name, determine phonetic lookup-keys like above.
Build a list of candidate list-entry matches using entry-ids from the phonetic lookup-key matches
Filter this list by using a string similarity algorithm, with normalized similarity ratio output. Set a user-defined minimum threshold for similarity ratio, e.g. 0.8
 

Various improvements are possible. Of special note, to check both similarity on both local level (name parts) and global level (complete name) is likely necessary for a good result.

References

- https://www.treasury.gov/resource-center/sanctions/SDN-List/Pages/fuzzy_logic.aspx -- see item 4

- https://easyofac.com/#desc –- heading "Layered fuzzy search"
