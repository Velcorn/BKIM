from Bio import SeqIO
file = 'sample.gb'
content = SeqIO.read(file, 'genbank')

# 1. Print identifier, name and description of the sequence
print(content.id)
print(content.name)
print(content.description)

# 2. Print the first 100 characters of the sequence
print(content.seq[:100])

# 3. Print number of external references (dbxrefs) and ids of the external references.
print(len(content.dbxrefs))

# 4. Print the name of the organism (hint: check the annotations dictionary at the key “organism”)
print(content.annotations['organism'])

# 5. Retrieve and print all (if any) associated publications (hint: annotation dictionary, key:”references”)
for ref in content.annotations['references']:
    print(ref)

# 6. Retrieve and print all the locations of “CDS” features of the sequence (hint: check the features)
for feature in content.features:
    if feature.type == 'CDS':
        print(feature.location)
