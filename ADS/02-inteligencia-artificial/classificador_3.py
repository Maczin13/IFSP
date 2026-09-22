"""Classificador supervisionado didático para triagem de textos sintéticos.
Não realiza diagnóstico: a classe sinal significa apenas necessidade de revisão humana.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Iterable
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

DEFAULT_DATA = [
 ("sinto ansiedade antes das provas", "sinal"), ("tenho crises de panico", "sinal"),
 ("estou muito triste e sem energia", "sinal"), ("preciso conversar porque estou angustiado", "sinal"),
 ("minha preocupação não passa", "sinal"), ("tenho medo constante", "sinal"),
 ("não consigo dormir por causa da ansiedade", "sinal"), ("estou desanimado há semanas", "sinal"),
 ("o conteúdo da aula é sobre bancos", "sem_sinal"), ("configurei o servidor local", "sem_sinal"),
 ("estudei redes de computadores", "sem_sinal"), ("o programa passou nos testes", "sem_sinal"),
 ("estou lendo sobre inteligência artificial", "sem_sinal"), ("a reunião foi remarcada", "sem_sinal"),
 ("terminei o exercício de python", "sem_sinal"), ("o aplicativo foi publicado", "sem_sinal"),
]

def build_model() -> Pipeline:
    return Pipeline([("vectorizer", CountVectorizer(lowercase=True, strip_accents="unicode", ngram_range=(1,2))),
                     ("classifier", MultinomialNB(alpha=1.0))])

def evaluate(samples: Iterable[tuple[str,str]], seed: int = 42) -> dict:
    samples=list(samples); texts=[x[0] for x in samples]; labels=[x[1] for x in samples]
    xtr,xte,ytr,yte=train_test_split(texts,labels,test_size=0.25,random_state=seed,stratify=labels)
    model=build_model(); model.fit(xtr,ytr); pred=model.predict(xte)
    report=classification_report(yte,pred,output_dict=True,zero_division=0)
    return {"seed":seed,"train_size":len(xtr),"test_size":len(xte),"labels":sorted(set(labels)),
            "classification_report":report,"confusion_matrix":confusion_matrix(yte,pred,labels=sorted(set(labels))).tolist(),
            "test_examples":[{"text":t,"expected":e,"predicted":p} for t,e,p in zip(xte,yte,pred)]}

def load_json(path: Path):
 data=json.loads(path.read_text(encoding='utf8')); return [(x["text"],x["label"]) for x in data]

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--data',type=Path); ap.add_argument('--out',type=Path,default=Path('results/metrics.json')); a=ap.parse_args()
 samples=load_json(a.data) if a.data else DEFAULT_DATA
 result=evaluate(samples); a.out.parent.mkdir(parents=True,exist_ok=True); a.out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8'); print(json.dumps(result,ensure_ascii=False,indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
