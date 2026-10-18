import unittest,tempfile,json,sys,subprocess
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import comercial
class Generator(unittest.TestCase):
 def test_all_designs_and_private_boundary(self):
  with tempfile.TemporaryDirectory() as tmp:
   for design in ['wtg','ujo','audidat','suderow']:
    d=json.loads((comercial.ROOT/'ejemplos/expediente-demo.json').read_text());d['public']['design']=design;d['internal']={'secret':'PRIVATE_SENTINEL_8472'};d['public']['company']='<script>alert(1)</script>'
    f=Path(tmp)/'input.json';f.write_text(json.dumps(d));out=Path(tmp)/design;comercial.build(f,out)
    self.assertNotIn('PRIVATE_SENTINEL_8472',''.join(p.read_text() for p in out.rglob('*') if p.is_file() and p.suffix in ['.html','.json','.mjs']))
    self.assertIn('&lt;script&gt;', (out/'index.html').read_text());self.assertIn('1.210,00 €',(out/'presupuesto.html').read_text())
    self.assertEqual(json.loads((out/'cuestionario/schema.json').read_text())['prefill'],{})
    self.assertTrue((out/'admin/index.html').exists())
    for p in out.rglob('*.mjs'):subprocess.run(['node','--check',str(p)],check=True,capture_output=True)
 def test_reject_invalid_url(self):
  with self.assertRaises(ValueError):comercial.url('javascript:alert(1)')
 def test_reject_overwrite(self):
  with tempfile.TemporaryDirectory() as tmp:
   out=Path(tmp);(out/'existing').write_text('preserve')
   with self.assertRaises(ValueError):comercial.build(comercial.ROOT/'ejemplos/expediente-demo.json',out)
   self.assertEqual((out/'existing').read_text(),'preserve')
if __name__=='__main__':unittest.main()
