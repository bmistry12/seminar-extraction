## Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition

* Key Terms and FSA's
    
    Phonetics and Phonology – The study of linguistic sounds.
    
    Morphology – The study of the meaningful components of words. 
    
    Syntax – The study of the structural relationships between words.
    
    Semantics – The study of meaning.
    
    Pragmatics – The study of how language is used to accomplish goals.
    
    Discourse – The study of linguistic units larger than a single utterance
    
    Parsing means taking an input and producing some sort of structure for it
    
    We can use POS Tagging to resolve ambiguities in meaning 
    
    Finite State Automata (FSA's) are useful to represent acceptable string
                   
                    regular expr
                         /\
                        /  \        
                       /    \        
                      /______\ 
                 finite     regular 
                 automata   languages
                 
    We can also represent an automaton with a state-transition table.  0 indicates illegal/missing transition
    Finite Automation can be defined formally as: 
    
        -  Q: a finite set of N states q0 ; q1 ; : : : qN
        -  Σ: a finite input alphabet of symbols
        -  q0: the start state
        -  F: the set of final states, F a subset of Q
        -  δ(q; i): the transition function or transition matrix between states. Given a state q 2 Q and an input symbol i 2 Σ, δ(q; i) returns a new state q 0 2 Q. δ is thus a relation from Q  Σ to Q
    
* Morphology and FSTs
    
    Morphology is the study of the way words are built up from smaller units (morphemes)
    
    There are two classes of morphemes -> Affixes and Stems
    
    Affixes = prefixes, suffixes, infixes, and circumfixes.
              Prefixes precede the stem, suffixes follow the stem, circumfixes do both, and infixes are inserted inside the stem
    
    Morphemes can be categorised as either inflection (same class/meaning) or derivation ones (different class/meaning)
    
    * Inflection Morphology
        Morphological Form Classes Regularly Inflected Verbs
        stem walk merge try map
        -s form walks merges tries maps
        -ing participle walking merging trying mapping
        Past form or -ed participle walked merged tried mapped
    * Stemming (going from Foxes to Fox)  
    



