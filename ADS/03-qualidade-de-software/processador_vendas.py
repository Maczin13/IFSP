"""Processador de vendas: valida pedidos, aplica cupons e calcula totais monetários."""
from __future__ import annotations
import argparse, json
from dataclasses import dataclass, asdict
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Any

CENT=Decimal('0.01')
class ValidationError(ValueError): pass
class CouponError(ValueError): pass
class StockError(ValueError): pass

@dataclass(frozen=True)
class Item:
    sku: str
    description: str
    unit_price: Decimal
    quantity: int
    stock: int
    def subtotal(self) -> Decimal: return (self.unit_price * self.quantity).quantize(CENT)

@dataclass(frozen=True)
class Coupon:
    code: str
    percent: Decimal
    minimum_subtotal: Decimal
    active: bool=True

@dataclass(frozen=True)
class SaleResult:
    subtotal: Decimal
    discount: Decimal
    total: Decimal
    coupon: str|None
    items: int

def money(value: Any, field: str) -> Decimal:
    if isinstance(value,bool): raise ValidationError(f'{field}: boolean não é valor monetário')
    try: d=Decimal(str(value))
    except (InvalidOperation,ValueError): raise ValidationError(f'{field}: valor inválido')
    if not d.is_finite() or d<0: raise ValidationError(f'{field}: deve ser finito e não negativo')
    return d.quantize(CENT,rounding=ROUND_HALF_UP)

def make_item(raw: dict[str,Any]) -> Item:
    required={'sku','description','unit_price','quantity','stock'}
    missing=required-set(raw)
    if missing: raise ValidationError(f'item sem campos: {sorted(missing)}')
    if not isinstance(raw['sku'],str) or not raw['sku'].strip(): raise ValidationError('sku inválido')
    if not isinstance(raw['description'],str) or not raw['description'].strip(): raise ValidationError('description inválida')
    if isinstance(raw['quantity'],bool) or not isinstance(raw['quantity'],int) or raw['quantity']<=0: raise ValidationError('quantity deve ser inteiro positivo')
    if isinstance(raw['stock'],bool) or not isinstance(raw['stock'],int) or raw['stock']<0: raise ValidationError('stock deve ser inteiro não negativo')
    if raw['quantity']>raw['stock']: raise StockError(f'estoque insuficiente para {raw["sku"]}')
    return Item(raw['sku'].strip(),raw['description'].strip(),money(raw['unit_price'],'unit_price'),raw['quantity'],raw['stock'])

def make_coupon(raw: dict[str,Any]|None) -> Coupon|None:
    if raw is None:return None
    code=raw.get('code')
    if not isinstance(code,str) or not code.strip(): raise CouponError('código de cupom inválido')
    try:
        percent=money(raw.get('percent'), 'percent')
    except ValidationError as exc:
        raise CouponError(str(exc)) from exc
    if percent<=0 or percent>100: raise CouponError('percentual deve estar entre 0 e 100')
    try:
        minimum=money(raw.get('minimum_subtotal',0),'minimum_subtotal')
    except ValidationError as exc:
        raise CouponError(str(exc)) from exc
    return Coupon(code.strip().upper(),percent,minimum,bool(raw.get('active',True)))

def process_sale(raw_items:list[dict[str,Any]], raw_coupon:dict[str,Any]|None=None) -> SaleResult:
    if not isinstance(raw_items,list) or not raw_items: raise ValidationError('a venda precisa de itens')
    items=[make_item(x) for x in raw_items]
    subtotal=sum((x.subtotal() for x in items),Decimal('0.00')).quantize(CENT)
    coupon=make_coupon(raw_coupon)
    discount=Decimal('0.00')
    if coupon:
        if not coupon.active: raise CouponError('cupom inativo')
        if subtotal<coupon.minimum_subtotal: raise CouponError('subtotal abaixo do mínimo do cupom')
        discount=(subtotal*coupon.percent/Decimal('100')).quantize(CENT,rounding=ROUND_HALF_UP)
    return SaleResult(subtotal,discount,(subtotal-discount).quantize(CENT),coupon.code if coupon else None,sum(x.quantity for x in items))

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('input',type=str); a=ap.parse_args()
 payload=json.loads(open(a.input,encoding='utf8').read()); result=process_sale(payload['items'],payload.get('coupon'))
 print(json.dumps({k:str(v) for k,v in asdict(result).items()},ensure_ascii=False,indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
