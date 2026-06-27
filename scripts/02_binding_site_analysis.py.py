from Bio.PDB import MMCIFParser
import csv
import os

parser = MMCIFParser(QUIET=True)
structure = parser.get_structure('KRAS', 
    r'C:\Users\MICRO SYSTEM\OneDrive\Desktop\kras.project\data\6oim.cif')

model = structure[0]
chain_A = model['A']

# finding MOV ligand 
ligand = None
for residue in chain_A:
    if residue.resname == 'MOV':
        ligand = residue
        break

if ligand is None:
    print("ligand not found!")
else:
    print(f"ligand found: {ligand.resname}")

# we want to find residues near to the ligand
contact_residues = []
for residue in chain_A:
    if residue.id[0] != ' ':
        continue
    for atom in residue:
        for lig_atom in ligand:
            distance = atom - lig_atom
            if distance < 4.0:
                contact_residues.append({
                    'residue_name': residue.resname,
                    'residue_number': residue.id[1],
                    'distance': round(distance, 2)
                })
                break
        else:
            continue
        break

# we should delete repeated ones
seen = set()
unique_contacts = []
for r in contact_residues:
    key = (r['residue_name'], r['residue_number'])
    if key not in seen:
        seen.add(key)
        unique_contacts.append(r)

unique_contacts.sort(key=lambda x: x['distance'])

print(f"\nnumber of contact residues: {len(unique_contacts)}")
print(f"\n{'Residue':<10} {'Number':<10} {'Distance':<10}")
print("-" * 30)
for r in unique_contacts:
    print(f"{r['residue_name']:<10} {r['residue_number']:<10} {r['distance']:<10}")

output_path = r'C:\Users\MICRO SYSTEM\OneDrive\Desktop\kras.project\results\binding_site_contacts.csv'
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['residue_name', 'residue_number', 'distance'])
    writer.writeheader()
    writer.writerows(unique_contacts)

print(f"\nresults are saved!")