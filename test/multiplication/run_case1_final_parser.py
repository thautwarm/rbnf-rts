

def mk_parser(unwrap, mul):
    from rbnf_rts.rts import AST as prim__mk__ast, Cons as prim__cons, _nil as prim__nil

    def lr_step_Mul(_slot_0, prim__state, prim__tokens):
        Mul_lhs_0 = _slot_0
        lcl_0 = prim__tokens.offset
        _off_0 = lcl_0
        lcl_0 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
        if lcl_0:
            lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
            lcl_2 = lcl_2.idint
            if (lcl_2 == 3):
                _py_local_i = prim__tokens.offset
                _py_local_t = prim__tokens.array[_py_local_i]
                prim__tokens.offset = (_py_local_i + 1)
                lcl_2 = _py_local_t
                _slot_1 = lcl_2
                lcl_2 = parse_Atom(prim__state, prim__tokens)
                _slot_2_check = lcl_2
                lcl_2 = _slot_2_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_2_check
                else:
                    lcl_3 = _slot_2_check[1]
                    lcl_3 = lcl_3
                    _slot_2 = lcl_3
                    Mul_rhs_1 = _slot_2
                    lcl_3 = mul(Mul_lhs_0, Mul_rhs_1)
                    _slot_local__1 = lcl_3
                    lcl_3 = (True, _slot_local__1)
                    lcl_2 = lcl_3
                lcl_1 = lcl_2
            elif (lcl_2 == 4):
                _py_local_i = prim__tokens.offset
                _py_local_t = prim__tokens.array[_py_local_i]
                prim__tokens.offset = (_py_local_i + 1)
                lcl_2 = _py_local_t
                _slot_1 = lcl_2
                lcl_2 = parse_Atom(prim__state, prim__tokens)
                _slot_2_check = lcl_2
                lcl_2 = _slot_2_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_2_check
                else:
                    lcl_2 = _slot_2_check[1]
                    lcl_2 = lcl_2
                    _slot_2 = lcl_2
                    Mul_rhs_1 = _slot_2
                    lcl_2 = mul(Mul_lhs_0, Mul_rhs_1)
                    _slot_local__1 = lcl_2
                    lcl_2 = (True, _slot_local__1)
                lcl_1 = lcl_2
            else:
                lcl_2 = (_off_0, 'Mul lookahead failed')
                lcl_2 = prim__cons(lcl_2, prim__nil)
                lcl_2 = lcl_2
                lcl_2 = (False, lcl_2)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        else:
            lcl_1 = (_off_0, 'Mul got EOF')
            lcl_1 = prim__cons(lcl_1, prim__nil)
            lcl_1 = lcl_1
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        return lcl_0

    def lr_loop_Mul(_slot_0, prim__state, prim__tokens):
        lr_Mul_reduce = _slot_0
        lcl_0 = prim__tokens.offset
        _off_0 = lcl_0
        lcl_0 = lr_step_Mul(lr_Mul_reduce, prim__state, prim__tokens)
        lr_Mul_try = lcl_0
        lcl_0 = lr_Mul_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_0 = prim__tokens.offset
            _off_0 = lcl_0
            lcl_0 = lr_Mul_try[1]
            lcl_0 = lcl_0
            lr_Mul_reduce = lcl_0
            lcl_0 = lr_step_Mul(lr_Mul_reduce, prim__state, prim__tokens)
            lr_Mul_try = lcl_0
            lcl_0 = lr_Mul_try[0]
            lcl_0 = (lcl_0 is not False)
        prim__tokens.offset = _off_0
        return lr_Mul_reduce

    def parse_Atom(prim__state, prim__tokens):
        lcl_0 = prim__tokens.offset
        _off_0 = lcl_0
        lcl_0 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
        if lcl_0:
            lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
            lcl_2 = lcl_2.idint
            if (lcl_2 == 6):
                _py_local_i = prim__tokens.offset
                _py_local_t = prim__tokens.array[_py_local_i]
                prim__tokens.offset = (_py_local_i + 1)
                lcl_2 = _py_local_t
                _slot_0 = lcl_2
                lcl_2 = parse_Mul(prim__state, prim__tokens)
                _slot_1_check = lcl_2
                lcl_2 = _slot_1_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_1_check
                else:
                    lcl_3 = _slot_1_check[1]
                    lcl_3 = lcl_3
                    _slot_1 = lcl_3
                    Atom_a_1 = _slot_1
                    lcl_3 = 7
                    try:
                        _py_local_tk = prim__tokens.array[prim__tokens.offset]
                        if (_py_local_tk.idint is lcl_3):
                            prim__tokens.offset += 1
                        else:
                            _py_local_tk = None
                    except IndexError:
                        _py_local_tk = None
                    lcl_3 = _py_local_tk
                    _slot_2 = lcl_3
                    lcl_3 = (_slot_2 is None)
                    if lcl_3:
                        lcl_3 = prim__tokens.offset
                        lcl_3 = (lcl_3, 'quote ) not match')
                        lcl_3 = prim__cons(lcl_3, prim__nil)
                        lcl_3 = lcl_3
                        lcl_3 = (False, lcl_3)
                    else:
                        _slot_local__1 = Atom_a_1
                        lcl_3 = (True, _slot_local__1)
                    lcl_2 = lcl_3
                lcl_1 = lcl_2
            elif (lcl_2 == 2):
                _py_local_i = prim__tokens.offset
                _py_local_t = prim__tokens.array[_py_local_i]
                prim__tokens.offset = (_py_local_i + 1)
                lcl_2 = _py_local_t
                _slot_0 = lcl_2
                Atom_a_1 = _slot_0
                lcl_2 = unwrap(Atom_a_1)
                _slot_local__1 = lcl_2
                lcl_2 = (True, _slot_local__1)
                lcl_1 = lcl_2
            else:
                lcl_2 = (_off_0, 'Atom lookahead failed')
                lcl_2 = prim__cons(lcl_2, prim__nil)
                lcl_2 = lcl_2
                lcl_2 = (False, lcl_2)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        else:
            lcl_1 = (_off_0, 'Atom got EOF')
            lcl_1 = prim__cons(lcl_1, prim__nil)
            lcl_1 = lcl_1
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        return lcl_0

    def parse_Mul(prim__state, prim__tokens):
        lcl_0 = parse_Atom(prim__state, prim__tokens)
        _slot_0_check = lcl_0
        lcl_0 = _slot_0_check[0]
        lcl_0 = (lcl_0 is False)
        if lcl_0:
            lcl_0 = _slot_0_check
        else:
            lcl_0 = _slot_0_check[1]
            lcl_0 = lcl_0
            _slot_0 = lcl_0
            Mul_a_0 = _slot_0
            _slot_local__1 = Mul_a_0
            lcl_0 = lr_loop_Mul(_slot_local__1, prim__state, prim__tokens)
            lcl_0 = (True, lcl_0)
        return lcl_0

    def parse_START(prim__state, prim__tokens):
        lcl_0 = 0
        try:
            _py_local_tk = prim__tokens.array[prim__tokens.offset]
            if (_py_local_tk.idint is lcl_0):
                prim__tokens.offset += 1
            else:
                _py_local_tk = None
        except IndexError:
            _py_local_tk = None
        lcl_0 = _py_local_tk
        _slot_0 = lcl_0
        lcl_0 = (_slot_0 is None)
        if lcl_0:
            lcl_0 = prim__tokens.offset
            lcl_0 = (lcl_0, 'BOF not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = parse_Mul(prim__state, prim__tokens)
            _slot_1_check = lcl_0
            lcl_0 = _slot_1_check[0]
            lcl_0 = (lcl_0 is False)
            if lcl_0:
                lcl_0 = _slot_1_check
            else:
                lcl_1 = _slot_1_check[1]
                lcl_1 = lcl_1
                _slot_1 = lcl_1
                START_a_1 = _slot_1
                lcl_1 = 1
                try:
                    _py_local_tk = prim__tokens.array[prim__tokens.offset]
                    if (_py_local_tk.idint is lcl_1):
                        prim__tokens.offset += 1
                    else:
                        _py_local_tk = None
                except IndexError:
                    _py_local_tk = None
                lcl_1 = _py_local_tk
                _slot_2 = lcl_1
                lcl_1 = (_slot_2 is None)
                if lcl_1:
                    lcl_1 = prim__tokens.offset
                    lcl_1 = (lcl_1, 'EOF not match')
                    lcl_1 = prim__cons(lcl_1, prim__nil)
                    lcl_1 = lcl_1
                    lcl_1 = (False, lcl_1)
                else:
                    _slot_local__1 = START_a_1
                    lcl_1 = (True, _slot_local__1)
                lcl_0 = lcl_1
        return lcl_0
    return parse_START
