
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLTGTleftPLUSMINUSleftTIMESDIVIDECOMMA DIVIDE ELSE EQUALS FLOAT FOR GT ID IF INT LBRACE LBRACKET LPAREN LT MINUS NUMBER PLUS RBRACE RBRACKET RPAREN SEMICOLON STRING STRING_LITERAL TIMES WHILEprogram : statementsstatements : statements statement\n                  | statementstatement : INT ID SEMICOLON\n                 | FLOAT ID SEMICOLON\n                 | STRING ID SEMICOLONstatement : ID EQUALS expression SEMICOLON\n                 | ID EQUALS STRING_LITERAL SEMICOLONstatement : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statementstatement : WHILE LPAREN expression RPAREN statementstatement : LBRACE statements RBRACEstatement : IF LPAREN expression RPAREN statement\n                 | IF LPAREN expression RPAREN statement ELSE statementstatement : expression SEMICOLONexpression : expression PLUS term\n                  | expression MINUS termexpression : expression LT expression\n                  | expression GT expressionexpression : termterm : term TIMES factor\n            | term DIVIDE factorterm : factorfactor : NUMBER\n              | FLOATfactor : STRING_LITERALfactor : IDfactor : LPAREN expression RPARENexpression : ID EQUALS expressionexpression : LBRACKET elements RBRACKETelements : elements COMMA expressionelements : expressionelements : '
    
_lr_action_items = {'INT':([0,2,3,13,19,24,34,40,43,44,54,60,61,64,65,68,69,71,73,74,75,],[4,4,-3,4,-2,-14,4,-4,-5,-6,-11,-7,-8,4,4,-10,-12,4,-13,4,-9,]),'FLOAT':([0,2,3,11,13,16,19,21,24,25,26,27,28,29,33,34,35,36,37,40,43,44,52,54,59,60,61,62,64,65,68,69,70,71,73,74,75,],[6,6,-3,32,6,32,-2,32,-14,32,32,32,32,32,32,6,32,32,32,-4,-5,-6,32,-11,32,-7,-8,32,6,6,-10,-12,32,6,-13,6,-9,]),'STRING':([0,2,3,13,19,24,34,40,43,44,54,60,61,64,65,68,69,71,73,74,75,],[7,7,-3,7,-2,-14,7,-4,-5,-6,-11,-7,-8,7,7,-10,-12,7,-13,7,-9,]),'ID':([0,2,3,4,6,7,11,13,16,19,21,24,25,26,27,28,29,33,34,35,36,37,40,43,44,52,54,59,60,61,62,64,65,68,69,70,71,73,74,75,],[5,5,-3,20,22,23,31,5,31,-2,31,-14,46,46,31,31,31,31,5,31,46,46,-4,-5,-6,31,-11,31,-7,-8,31,5,5,-10,-12,31,5,-13,5,-9,]),'FOR':([0,2,3,13,19,24,34,40,43,44,54,60,61,64,65,68,69,71,73,74,75,],[10,10,-3,10,-2,-14,10,-4,-5,-6,-11,-7,-8,10,10,-10,-12,10,-13,10,-9,]),'WHILE':([0,2,3,13,19,24,34,40,43,44,54,60,61,64,65,68,69,71,73,74,75,],[12,12,-3,12,-2,-14,12,-4,-5,-6,-11,-7,-8,12,12,-10,-12,12,-13,12,-9,]),'LBRACE':([0,2,3,13,19,24,34,40,43,44,54,60,61,64,65,68,69,71,73,74,75,],[13,13,-3,13,-2,-14,13,-4,-5,-6,-11,-7,-8,13,13,-10,-12,13,-13,13,-9,]),'IF':([0,2,3,13,19,24,34,40,43,44,54,60,61,64,65,68,69,71,73,74,75,],[14,14,-3,14,-2,-14,14,-4,-5,-6,-11,-7,-8,14,14,-10,-12,14,-13,14,-9,]),'LBRACKET':([0,2,3,11,13,16,19,21,24,27,28,29,33,34,35,40,43,44,52,54,59,60,61,62,64,65,68,69,70,71,73,74,75,],[16,16,-3,16,16,16,-2,16,-14,16,16,16,16,16,16,-4,-5,-6,16,-11,16,-7,-8,16,16,16,-10,-12,16,16,-13,16,-9,]),'NUMBER':([0,2,3,11,13,16,19,21,24,25,26,27,28,29,33,34,35,36,37,40,43,44,52,54,59,60,61,62,64,65,68,69,70,71,73,74,75,],[18,18,-3,18,18,18,-2,18,-14,18,18,18,18,18,18,18,18,18,18,-4,-5,-6,18,-11,18,-7,-8,18,18,18,-10,-12,18,18,-13,18,-9,]),'STRING_LITERAL':([0,2,3,11,13,16,19,21,24,25,26,27,28,29,33,34,35,36,37,40,43,44,52,54,59,60,61,62,64,65,68,69,70,71,73,74,75,],[9,9,-3,9,9,9,-2,42,-14,9,9,9,9,9,9,9,9,9,9,-4,-5,-6,9,-11,9,-7,-8,9,9,9,-10,-12,9,9,-13,9,-9,]),'LPAREN':([0,2,3,10,11,12,13,14,16,19,21,24,25,26,27,28,29,33,34,35,36,37,40,43,44,52,54,59,60,61,62,64,65,68,69,70,71,73,74,75,],[11,11,-3,29,11,33,11,35,11,-2,11,-14,11,11,11,11,11,11,11,11,11,11,-4,-5,-6,11,-11,11,-7,-8,11,11,11,-10,-12,11,11,-13,11,-9,]),'$end':([1,2,3,19,24,40,43,44,54,60,61,68,69,73,75,],[0,-1,-3,-2,-14,-4,-5,-6,-11,-7,-8,-10,-12,-13,-9,]),'RBRACE':([3,19,24,34,40,43,44,54,60,61,68,69,73,75,],[-3,-2,-14,54,-4,-5,-6,-11,-7,-8,-10,-12,-13,-9,]),'EQUALS':([5,31,],[21,52,]),'TIMES':([5,6,9,15,17,18,31,32,42,45,46,47,51,56,57,],[-26,-24,-25,36,-22,-23,-26,-24,-25,36,-26,36,-27,-20,-21,]),'DIVIDE':([5,6,9,15,17,18,31,32,42,45,46,47,51,56,57,],[-26,-24,-25,37,-22,-23,-26,-24,-25,37,-26,37,-27,-20,-21,]),'SEMICOLON':([5,6,8,9,15,17,18,20,22,23,31,32,41,42,45,46,47,48,49,50,51,56,57,58,63,67,],[-26,-24,24,-25,-19,-22,-23,40,43,44,-26,-24,60,61,-15,-26,-16,-17,-18,62,-27,-20,-21,-29,-28,70,]),'PLUS':([5,6,8,9,15,17,18,30,31,32,39,41,42,45,46,47,48,49,50,51,53,55,56,57,58,63,66,67,72,],[-26,-24,25,-25,-19,-22,-23,25,-26,-24,25,25,-25,-15,-26,-16,25,25,25,-27,25,25,-20,-21,-29,25,25,25,25,]),'MINUS':([5,6,8,9,15,17,18,30,31,32,39,41,42,45,46,47,48,49,50,51,53,55,56,57,58,63,66,67,72,],[-26,-24,26,-25,-19,-22,-23,26,-26,-24,26,26,-25,-15,-26,-16,26,26,26,-27,26,26,-20,-21,-29,26,26,26,26,]),'LT':([5,6,8,9,15,17,18,30,31,32,39,41,42,45,46,47,48,49,50,51,53,55,56,57,58,63,66,67,72,],[-26,-24,27,-25,-19,-22,-23,27,-26,-24,27,27,-25,-15,-26,-16,-17,-18,27,-27,27,27,-20,-21,-29,27,27,27,27,]),'GT':([5,6,8,9,15,17,18,30,31,32,39,41,42,45,46,47,48,49,50,51,53,55,56,57,58,63,66,67,72,],[-26,-24,28,-25,-19,-22,-23,28,-26,-24,28,28,-25,-15,-26,-16,-17,-18,28,-27,28,28,-20,-21,-29,28,28,28,28,]),'RPAREN':([9,15,17,18,30,31,32,45,46,47,48,49,51,53,55,56,57,58,63,72,],[-25,-19,-22,-23,51,-26,-24,-15,-26,-16,-17,-18,-27,64,65,-20,-21,-29,-28,74,]),'RBRACKET':([9,15,16,17,18,31,32,38,39,45,46,47,48,49,51,56,57,58,63,66,],[-25,-19,-32,-22,-23,-26,-24,58,-31,-15,-26,-16,-17,-18,-27,-20,-21,-29,-28,-30,]),'COMMA':([9,15,16,17,18,31,32,38,39,45,46,47,48,49,51,56,57,58,63,66,],[-25,-19,-32,-22,-23,-26,-24,59,-31,-15,-26,-16,-17,-18,-27,-20,-21,-29,-28,-30,]),'ELSE':([24,40,43,44,54,60,61,68,69,73,75,],[-14,-4,-5,-6,-11,-7,-8,-10,71,-13,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,13,],[2,34,]),'statement':([0,2,13,34,64,65,71,74,],[3,19,3,19,68,69,73,75,]),'expression':([0,2,11,13,16,21,27,28,29,33,34,35,52,59,62,64,65,70,71,74,],[8,8,30,8,39,41,48,49,50,53,8,55,63,66,67,8,8,72,8,8,]),'term':([0,2,11,13,16,21,25,26,27,28,29,33,34,35,52,59,62,64,65,70,71,74,],[15,15,15,15,15,15,45,47,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'factor':([0,2,11,13,16,21,25,26,27,28,29,33,34,35,36,37,52,59,62,64,65,70,71,74,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,56,57,17,17,17,17,17,17,17,17,]),'elements':([16,],[38,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','sintactico.py',13),
  ('statements -> statements statement','statements',2,'p_statements','sintactico.py',17),
  ('statements -> statement','statements',1,'p_statements','sintactico.py',18),
  ('statement -> INT ID SEMICOLON','statement',3,'p_statement_declaration','sintactico.py',25),
  ('statement -> FLOAT ID SEMICOLON','statement',3,'p_statement_declaration','sintactico.py',26),
  ('statement -> STRING ID SEMICOLON','statement',3,'p_statement_declaration','sintactico.py',27),
  ('statement -> ID EQUALS expression SEMICOLON','statement',4,'p_statement_assignment','sintactico.py',31),
  ('statement -> ID EQUALS STRING_LITERAL SEMICOLON','statement',4,'p_statement_assignment','sintactico.py',32),
  ('statement -> FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statement','statement',9,'p_statement_for','sintactico.py',36),
  ('statement -> WHILE LPAREN expression RPAREN statement','statement',5,'p_statement_while','sintactico.py',40),
  ('statement -> LBRACE statements RBRACE','statement',3,'p_statement_block','sintactico.py',44),
  ('statement -> IF LPAREN expression RPAREN statement','statement',5,'p_statement_if','sintactico.py',48),
  ('statement -> IF LPAREN expression RPAREN statement ELSE statement','statement',7,'p_statement_if','sintactico.py',49),
  ('statement -> expression SEMICOLON','statement',2,'p_statement_expression','sintactico.py',56),
  ('expression -> expression PLUS term','expression',3,'p_expression_binop','sintactico.py',60),
  ('expression -> expression MINUS term','expression',3,'p_expression_binop','sintactico.py',61),
  ('expression -> expression LT expression','expression',3,'p_expression_comparison','sintactico.py',65),
  ('expression -> expression GT expression','expression',3,'p_expression_comparison','sintactico.py',66),
  ('expression -> term','expression',1,'p_expression_term','sintactico.py',70),
  ('term -> term TIMES factor','term',3,'p_term_binop','sintactico.py',74),
  ('term -> term DIVIDE factor','term',3,'p_term_binop','sintactico.py',75),
  ('term -> factor','term',1,'p_term_factor','sintactico.py',79),
  ('factor -> NUMBER','factor',1,'p_factor_num','sintactico.py',83),
  ('factor -> FLOAT','factor',1,'p_factor_num','sintactico.py',84),
  ('factor -> STRING_LITERAL','factor',1,'p_factor_string','sintactico.py',88),
  ('factor -> ID','factor',1,'p_factor_id','sintactico.py',92),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','sintactico.py',96),
  ('expression -> ID EQUALS expression','expression',3,'p_expression_equals','sintactico.py',100),
  ('expression -> LBRACKET elements RBRACKET','expression',3,'p_expression_list','sintactico.py',104),
  ('elements -> elements COMMA expression','elements',3,'p_elements_multiple','sintactico.py',108),
  ('elements -> expression','elements',1,'p_elements_single','sintactico.py',112),
  ('elements -> <empty>','elements',0,'p_elements_empty','sintactico.py',116),
]
