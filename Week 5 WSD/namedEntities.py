import nltk
import re
from nltk.corpus import ieer
from nltk.sem import relextract
#names entities
'''docs = ieer.parsed_docs('NYT_19980315')
tree = docs[1].text
print(tree)

#relation extraction
pairs = relextract.tree2semi_rel(tree)
for s, tree in pairs[18:22]:
    print('("...%s", %s)' % (" ".join(s[-5:]),tree))

'''
'''
The function relextract() allows us
to filter the reldicts according to the classes of the subject and object named entities.
'''
'''
reldicts = relextract.semi_rel2reldict(pairs)
for k, v in sorted(reldicts[0].items()):
    print(k, '=>', v)

for r in reldicts[18:20]:
    print('=' * 20)
    print(r['subjtext'])
    print(r['filler'])
    print(r['objtext'])   '''

#IN has signature <ORG, LOC>.
import re
IN = re.compile(r'.*\bin\b(?!\b.+ing\b)')
for fileid in ieer.fileids():
    for doc in ieer.parsed_docs(fileid):
        for rel in relextract.extract_rels('ORG', 'LOC', doc, corpus='ieer', pattern = IN):
            print(relextract.rtuple(rel))
