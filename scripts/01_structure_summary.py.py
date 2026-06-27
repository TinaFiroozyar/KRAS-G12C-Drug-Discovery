import os
from Bio.PDB import MMCIFParser

def analyze_structure(file_path, pdb_id):
    parser = MMCIFParser(QUIET=True)
    try:
        structure = parser.get_structure(pdb_id, file_path)
        model = structure[0]
        
        residues = [r for r in model.get_residues() if r.id[0] == ' ']
        n_residues = len(residues)
        
        ligands = set()
        for residue in model.get_residues():
            res_type = residue.id[0]
            if res_type.startswith('H_') and res_type != 'W':
                ligands.add(residue.resname)
                
        return n_residues, list(ligands)
    except Exception as e:
        print(f"Error reading {pdb_id}: {e}")
        return None, None

# folder_path = r"C:\Users\MICRO SYSTEM\OneDrive\Desktop\kras.project\data"
folder_path = r"C:\Users\MICRO SYSTEM\OneDrive\Desktop\kras.project\data"
cif_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.cif')]

if not cif_files:
    print(f"No .cif files found in: {folder_path}")
else:
    print(f"{'PDB ID':<10} | {'Residues':<10} | {'Ligands'}")
    print("-" * 50)
    
    for filename in cif_files:
        pdb_id = os.path.splitext(filename)[0]
        full_path = os.path.join(folder_path, filename)
        
        n_res, ligs = analyze_structure(full_path, pdb_id)
        if n_res is not None:
            ligs_str = ", ".join(ligs) if ligs else "None"
            print(f"{pdb_id.upper():<10} | {n_res:<10} | {ligs_str}")
