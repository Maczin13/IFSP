import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]))
import pytest
from ethics_lab import DISCLAIMER,evaluate,anonymize

def test_anonymizes_email_cpf_and_phone():
 r=evaluate('Contato ana@example.com CPF 123.456.789-09 telefone (11) 99999-8888')
 assert '[REDACTED_EMAIL]' in r['text'] and '[REDACTED_CPF]' in r['text'] and '[REDACTED_PHONE]' in r['text']
 assert r['pii_types']==['cpf','email','phone']
@pytest.mark.parametrize('text,flag',[('há risco de suicídio','self_harm'),('houve ameaça','threat'),('preciso de diagnóstico','medical_diagnosis'),('há violência','violence')])
def test_risk_terms_route_to_human(text,flag):
 r=evaluate(text); assert r['route']=='human_review' and flag in r['risk_flags']
def test_safe_text_has_limited_route():
 r=evaluate('Quero aprender sobre privacidade de dados.'); assert r['route']=='limited_guidance' and not r['risk_flags']
def test_disclaimer_is_unconditional():
 assert evaluate('texto qualquer')['disclaimer']==DISCLAIMER and evaluate('suicídio')['disclaimer']==DISCLAIMER
def test_input_type_contract():
 with pytest.raises(TypeError): anonymize(None)
def test_casefold_and_multiple_flags():
 r=evaluate('SUICÍDIO e MEDICAÇÃO'); assert set(r['risk_flags'])=={'self_harm','medical_advice'}
