from Bio.PDB import MMCIFParser, PDBIO, Select

class ProteinOnly(Select):
    def accept_residue(self, residue):
        # we will only keep aminoacids, and eliminate water, ions, ... 
        return residue.id[0] == ' '
    
    def accept_chain(self, chain):
        # we will only keep the chain A, as one chain is enough 
        return chain.id == 'A'

parser = MMCIFParser(QUIET=True)
structure = parser.get_structure('KRAS', r'C:\Users\MICRO SYSTEM\OneDrive\Desktop\kras.project\data\6oim.cif')

import os
os.makedirs(r'C:\Users\MICRO SYSTEM\OneDrive\Desktop\kras.project\data\processed', exist_ok=True)

io = PDBIO()
io.set_structure(structure)
io.save(r'C:\Users\MICRO SYSTEM\OneDrive\Desktop\kras.project\data\processed\6oim_clean.pdb', ProteinOnly())

print("file is ready: data/processed/6oim_clean.pdb")
