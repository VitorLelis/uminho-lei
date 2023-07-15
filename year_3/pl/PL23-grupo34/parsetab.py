
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "BIN BOOL DATETIME FLOAT HEX INFINITY INT LITERALMULT LITERALS NAN OCT QUOTEMULT STRING TIME WORDroot : tomltoml : tabletoml : arraytabletoml : emptytoml : toml attributestoml : toml tabletoml : toml arraytabletable : header attributesarraytable : '[' header ']' attributestable : header emptyarraytable : '[' header ']' emptyattributes : attributes attributeattributes : attributeattribute : key '=' valuekey : key '.' simplekeykey : simplekeysimplekey    : WORD\n                    | STRINGheader   : '[' key ']'value : term\n             | array\n             | inlinetableterm : INT\n            | LITERALMULT\n            | QUOTEMULT\n            | STRING\n            | LITERALS\n            | FLOAT\n            | DATETIME\n            | TIME\n            | BOOL\n            | OCT\n            | BIN\n            | HEX\n            | INFINITY\n            | NANarray : '[' array_elements ']'inlinetable : '{' inline_attributes '}'inline_attributes : inline_attributes ',' attribute inline_attributes : attributeinline_attributes : emptyarray_elements : array_elements ',' value array_elements : valuearray_elements : emptyempty :"
    
_lr_action_items = {'[':([0,2,3,4,5,6,7,8,9,10,11,16,17,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,47,48,55,56,57,],[7,7,-2,-3,-4,-45,18,-5,-6,-7,-13,-8,-10,-12,44,-45,-19,-14,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,44,-9,-11,-37,44,-38,]),'WORD':([0,2,3,4,5,6,7,8,9,10,11,16,17,18,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,47,48,55,57,58,],[-45,14,-2,-3,-4,14,14,14,-6,-7,-13,14,-10,14,-12,14,14,-19,-14,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,14,14,-11,-37,-38,14,]),'STRING':([0,2,3,4,5,6,7,8,9,10,11,16,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,55,56,57,58,],[-45,15,-2,-3,-4,15,15,15,-6,-7,-13,15,-10,15,-12,33,15,15,-19,-14,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,33,15,15,-11,-37,33,-38,15,]),'$end':([0,1,2,3,4,5,6,8,9,10,11,16,17,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,47,48,55,57,],[-45,0,-1,-2,-3,-4,-45,-5,-6,-7,-13,-8,-10,-12,-45,-19,-14,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-9,-11,-37,-38,]),'=':([12,13,14,15,46,],[22,-16,-17,-18,-15,]),'.':([12,13,14,15,20,46,],[23,-16,-17,-18,23,-15,]),']':([13,14,15,19,20,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,49,50,51,55,57,59,],[-16,-17,-18,24,25,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-45,-15,55,-43,-44,-37,-38,-42,]),'INT':([22,44,56,],[30,30,30,]),'LITERALMULT':([22,44,56,],[31,31,31,]),'QUOTEMULT':([22,44,56,],[32,32,32,]),'LITERALS':([22,44,56,],[34,34,34,]),'FLOAT':([22,44,56,],[35,35,35,]),'DATETIME':([22,44,56,],[36,36,36,]),'TIME':([22,44,56,],[37,37,37,]),'BOOL':([22,44,56,],[38,38,38,]),'OCT':([22,44,56,],[39,39,39,]),'BIN':([22,44,56,],[40,40,40,]),'HEX':([22,44,56,],[41,41,41,]),'INFINITY':([22,44,56,],[42,42,42,]),'NAN':([22,44,56,],[43,43,43,]),'{':([22,44,56,],[45,45,45,]),'}':([26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,52,53,54,55,57,60,],[-14,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-45,57,-40,-41,-37,-38,-39,]),',':([26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,49,50,51,52,53,54,55,57,59,60,],[-14,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-45,-45,56,-43,-44,58,-40,-41,-37,-38,-42,-39,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,],[1,]),'toml':([0,],[2,]),'table':([0,2,],[3,9,]),'arraytable':([0,2,],[4,10,]),'empty':([0,6,24,44,45,],[5,17,48,51,54,]),'header':([0,2,7,],[6,6,19,]),'attributes':([2,6,24,],[8,16,47,]),'attribute':([2,6,8,16,24,45,47,58,],[11,11,21,21,11,53,21,60,]),'key':([2,6,7,8,16,18,24,45,47,58,],[12,12,20,12,12,20,12,12,12,12,]),'simplekey':([2,6,7,8,16,18,23,24,45,47,58,],[13,13,13,13,13,13,46,13,13,13,13,]),'value':([22,44,56,],[26,50,59,]),'term':([22,44,56,],[27,27,27,]),'array':([22,44,56,],[28,28,28,]),'inlinetable':([22,44,56,],[29,29,29,]),'array_elements':([44,],[49,]),'inline_attributes':([45,],[52,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> toml','root',1,'p_root','grammar.py',8),
  ('toml -> table','toml',1,'p_toml_table','grammar.py',21),
  ('toml -> arraytable','toml',1,'p_toml_arraytable','grammar.py',25),
  ('toml -> empty','toml',1,'p_toml_empty','grammar.py',31),
  ('toml -> toml attributes','toml',2,'p_toml_toml_attributes','grammar.py',35),
  ('toml -> toml table','toml',2,'p_toml_toml_table','grammar.py',39),
  ('toml -> toml arraytable','toml',2,'p_toml_toml_arraytable','grammar.py',43),
  ('table -> header attributes','table',2,'p_table','grammar.py',47),
  ('arraytable -> [ header ] attributes','arraytable',4,'p_arraytable','grammar.py',65),
  ('table -> header empty','table',2,'p_table_empty','grammar.py',83),
  ('arraytable -> [ header ] empty','arraytable',4,'p_arraytable_empty','grammar.py',87),
  ('attributes -> attributes attribute','attributes',2,'p_attributes','grammar.py',92),
  ('attributes -> attribute','attributes',1,'p_attributes_single','grammar.py',99),
  ('attribute -> key = value','attribute',3,'p_attribute','grammar.py',103),
  ('key -> key . simplekey','key',3,'p_key','grammar.py',114),
  ('key -> simplekey','key',1,'p_key_simplekey','grammar.py',121),
  ('simplekey -> WORD','simplekey',1,'p_simplekey','grammar.py',125),
  ('simplekey -> STRING','simplekey',1,'p_simplekey','grammar.py',126),
  ('header -> [ key ]','header',3,'p_header','grammar.py',130),
  ('value -> term','value',1,'p_value','grammar.py',134),
  ('value -> array','value',1,'p_value','grammar.py',135),
  ('value -> inlinetable','value',1,'p_value','grammar.py',136),
  ('term -> INT','term',1,'p_term','grammar.py',140),
  ('term -> LITERALMULT','term',1,'p_term','grammar.py',141),
  ('term -> QUOTEMULT','term',1,'p_term','grammar.py',142),
  ('term -> STRING','term',1,'p_term','grammar.py',143),
  ('term -> LITERALS','term',1,'p_term','grammar.py',144),
  ('term -> FLOAT','term',1,'p_term','grammar.py',145),
  ('term -> DATETIME','term',1,'p_term','grammar.py',146),
  ('term -> TIME','term',1,'p_term','grammar.py',147),
  ('term -> BOOL','term',1,'p_term','grammar.py',148),
  ('term -> OCT','term',1,'p_term','grammar.py',149),
  ('term -> BIN','term',1,'p_term','grammar.py',150),
  ('term -> HEX','term',1,'p_term','grammar.py',151),
  ('term -> INFINITY','term',1,'p_term','grammar.py',152),
  ('term -> NAN','term',1,'p_term','grammar.py',153),
  ('array -> [ array_elements ]','array',3,'p_array','grammar.py',157),
  ('inlinetable -> { inline_attributes }','inlinetable',3,'p_inlinetable','grammar.py',163),
  ('inline_attributes -> inline_attributes , attribute','inline_attributes',3,'p_inline_attributes','grammar.py',170),
  ('inline_attributes -> attribute','inline_attributes',1,'p_inline_attributes_single','grammar.py',177),
  ('inline_attributes -> empty','inline_attributes',1,'p_inline_attributes_empty','grammar.py',181),
  ('array_elements -> array_elements , value','array_elements',3,'p_array_elements','grammar.py',185),
  ('array_elements -> value','array_elements',1,'p_array_elements_single','grammar.py',192),
  ('array_elements -> empty','array_elements',1,'p_array_elements_empty','grammar.py',196),
  ('empty -> <empty>','empty',0,'p_empty','grammar.py',200),
]
