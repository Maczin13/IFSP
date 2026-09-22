from __future__ import annotations
import argparse,json,re
from dataclasses import dataclass,asdict
from pathlib import Path
DISCLAIMER='Este laboratório não realiza diagnóstico, não substitui atendimento profissional e não deve orientar decisões de alto impacto.'
@dataclass(frozen=True)
class EthicalResult:
 text:str; pii_types:list[str]; risk_flags:list[str]; route:str; disclaimer:str
EMAIL=re.compile(r'(?<![\w.-])[\w.+-]+@[\w-]+(?:\.[\w-]+)+(?![\w.-])')
CPF=re.compile(r'(?<!\d)\d{3}[. ]?\d{3}[. ]?\d{3}[- ]?\d{2}(?!\d)')
PHONE=re.compile(r'(?<!\d)(?:\+?55[ -]?)?(?:\(?\d{2}\)?[ -]?)?9?\d{4}[ -]?\d{4}(?!\d)')
RISK_TERMS={'suicídio':'self_harm','suicidio':'self_harm','autoagressão':'self_harm','ameaça':'threat','violência':'violence','diagnóstico':'medical_diagnosis','medicação':'medical_advice','urgência':'urgent_context'}
def anonymize(text:str):
 if not isinstance(text,str): raise TypeError('text deve ser string')
 found=[]
 def sub(pattern,label,value):
  nonlocal text
  if pattern.search(text): found.append(label); text=pattern.sub(value,text)
 sub(EMAIL,'email','[REDACTED_EMAIL]'); sub(CPF,'cpf','[REDACTED_CPF]'); sub(PHONE,'phone','[REDACTED_PHONE]')
 return text,sorted(set(found))
def evaluate(text:str)->dict:
 clean,pii=anonymize(text); low=clean.casefold(); flags=sorted({tag for term,tag in RISK_TERMS.items() if term in low})
 route='human_review' if flags else 'limited_guidance'
 return asdict(EthicalResult(clean,pii,flags,route,DISCLAIMER))
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--input',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args(); result=evaluate(a.input.read_text(encoding='utf8')); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8'); print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__': main()
