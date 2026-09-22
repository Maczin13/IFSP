from pathlib import Path
root=Path(__file__).parent.parent
for d in sorted(p for p in root.iterdir() if p.is_dir() and p.name[:2].isdigit()):
 files=[p.name for p in d.iterdir() if p.is_file()]
 print(f'{d.name}: {len(files)} arquivos | '+', '.join(sorted(files)))
