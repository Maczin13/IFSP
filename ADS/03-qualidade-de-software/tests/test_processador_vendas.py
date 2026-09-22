import pytest
from decimal import Decimal
from processador_vendas import process_sale,ValidationError,CouponError,StockError,make_item

def test_sale_with_coupon(valid_items,coupon_10):
    result=process_sale(valid_items,coupon_10)
    assert result.subtotal==Decimal('25.50')
    assert result.discount==Decimal('2.55')
    assert result.total==Decimal('22.95')
    assert result.items==3

@pytest.mark.parametrize('value', [0,-1,True,1.5,'abc'])
def test_quantity_contract_rejects_invalid_types_or_values(valid_items,value):
    bad=dict(valid_items[0]); bad['quantity']=value
    with pytest.raises(ValidationError): make_item(bad)

@pytest.mark.parametrize('percent', ['0','100.01','-5',True,'abc'])
def test_coupon_percent_contract(percent,valid_items):
    with pytest.raises(CouponError): process_sale(valid_items,{'code':'X','percent':percent})

def test_stock_is_business_exception(valid_items):
    bad=dict(valid_items[0]); bad['quantity']=11
    with pytest.raises(StockError,match='estoque insuficiente'): process_sale([bad])

def test_inactive_coupon_is_rejected(valid_items):
    with pytest.raises(CouponError,match='inativo'): process_sale(valid_items,{'code':'OLD','percent':'10','active':False})

def test_minimum_subtotal(valid_items):
    with pytest.raises(CouponError,match='mínimo'): process_sale(valid_items,{'code':'VIP','percent':'10','minimum_subtotal':'100'})

def test_empty_sale_is_invalid():
    with pytest.raises(ValidationError,match='itens'): process_sale([])

def test_rounding_is_half_up():
    item={'sku':'X','description':'x','unit_price':'10.05','quantity':1,'stock':1}
    result=process_sale([item],{'code':'T','percent':'33.333','minimum_subtotal':'0'})
    assert result.discount==Decimal('3.35')

def test_input_is_not_mutated(valid_items):
    original=[dict(x) for x in valid_items]; process_sale(valid_items); assert valid_items==original
