from pathlib import Path
from datetime import datetime
import shutil
root=Path(__file__).resolve().parents[1]
for name in ['preauditoria-web','propuestas-presupuestos']:
 dest=Path.home()/'.codex/skills'/name
 if dest.exists() or dest.is_symlink():dest.rename(dest.with_name(name+'.backup-'+datetime.now().strftime('%Y%m%d%H%M%S')))
 dest.parent.mkdir(parents=True,exist_ok=True);dest.symlink_to(root/'skills'/name,target_is_directory=True)
 print('Instalada:',name)
