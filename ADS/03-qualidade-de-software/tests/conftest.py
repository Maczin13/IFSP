import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]))
import pytest
from processador_vendas import Item
@pytest.fixture
def valid_items():
    return [{'sku':'A','description':'Produto A','unit_price':'10.00','quantity':2,'stock':10},{'sku':'B','description':'Produto B','unit_price':'5.50','quantity':1,'stock':4}]
@pytest.fixture
def coupon_10():
    return {'code':'PROMO10','percent':'10','minimum_subtotal':'0','active':True}
