

def mk_parser():
    from rbnf_rts.rts import AST as prim__mk__ast, Cons as prim__cons, _nil as prim__nil

    def lr_step_CaseExps(_slot_0, prim__state, prim__tokens):
        lcl_0 = parse_CaseExp(prim__state, prim__tokens)
        _slot_1_check = lcl_0
        lcl_0 = _slot_1_check[0]
        lcl_0 = (lcl_0 is False)
        if lcl_0:
            lcl_0 = _slot_1_check
        else:
            lcl_0 = _slot_1_check[1]
            lcl_0 = lcl_0
            _slot_1 = lcl_0
            lcl_0 = (_slot_0, _slot_1)
            lcl_0 = prim__mk__ast('CaseExps', lcl_0)
            _slot_local__1 = lcl_0
            lcl_0 = (True, _slot_local__1)
        return lcl_0

    def lr_loop_CaseExps(_slot_0, prim__state, prim__tokens):
        lr_CaseExps_reduce = _slot_0
        lcl_0 = prim__tokens.offset
        _off_0 = lcl_0
        lcl_0 = lr_step_CaseExps(lr_CaseExps_reduce, prim__state, prim__tokens)
        lr_CaseExps_try = lcl_0
        lcl_0 = lr_CaseExps_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_0 = prim__tokens.offset
            _off_0 = lcl_0
            lcl_0 = lr_CaseExps_try[1]
            lcl_0 = lcl_0
            lr_CaseExps_reduce = lcl_0
            lcl_0 = lr_step_CaseExps(lr_CaseExps_reduce, prim__state, prim__tokens)
            lr_CaseExps_try = lcl_0
            lcl_0 = lr_CaseExps_try[0]
            lcl_0 = (lcl_0 is not False)
        prim__tokens.offset = _off_0
        return lr_CaseExps_reduce

    def lr_step_CommaCases(_slot_0, prim__state, prim__tokens):
        lcl_0 = 7
        try:
            _py_local_tk = prim__tokens.array[prim__tokens.offset]
            if (_py_local_tk.idint is lcl_0):
                prim__tokens.offset += 1
            else:
                _py_local_tk = None
        except IndexError:
            _py_local_tk = None
        lcl_0 = _py_local_tk
        _slot_1 = lcl_0
        lcl_0 = (_slot_1 is None)
        if lcl_0:
            lcl_0 = prim__tokens.offset
            lcl_0 = (lcl_0, 'quote , not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = (_slot_0, _slot_1)
            _slot_local__1 = lcl_0
            lcl_0 = parse_Case(prim__state, prim__tokens)
            _slot_2_check = lcl_0
            lcl_0 = _slot_2_check[0]
            lcl_0 = (lcl_0 is False)
            if lcl_0:
                lcl_0 = _slot_2_check
            else:
                lcl_0 = _slot_2_check[1]
                lcl_0 = lcl_0
                _slot_2 = lcl_0
                lcl_0 = (_slot_local__1, _slot_2)
                lcl_0 = prim__mk__ast('CommaCases', lcl_0)
                _slot_local__2 = lcl_0
                lcl_0 = (True, _slot_local__2)
        return lcl_0

    def lr_loop_CommaCases(_slot_0, prim__state, prim__tokens):
        lr_CommaCases_reduce = _slot_0
        lcl_0 = prim__tokens.offset
        _off_0 = lcl_0
        lcl_0 = lr_step_CommaCases(lr_CommaCases_reduce, prim__state, prim__tokens)
        lr_CommaCases_try = lcl_0
        lcl_0 = lr_CommaCases_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_0 = prim__tokens.offset
            _off_0 = lcl_0
            lcl_0 = lr_CommaCases_try[1]
            lcl_0 = lcl_0
            lr_CommaCases_reduce = lcl_0
            lcl_0 = lr_step_CommaCases(lr_CommaCases_reduce, prim__state, prim__tokens)
            lr_CommaCases_try = lcl_0
            lcl_0 = lr_CommaCases_try[0]
            lcl_0 = (lcl_0 is not False)
        prim__tokens.offset = _off_0
        return lr_CommaCases_reduce

    def lr_step_CommaExps(_slot_0, prim__state, prim__tokens):
        lcl_0 = 7
        try:
            _py_local_tk = prim__tokens.array[prim__tokens.offset]
            if (_py_local_tk.idint is lcl_0):
                prim__tokens.offset += 1
            else:
                _py_local_tk = None
        except IndexError:
            _py_local_tk = None
        lcl_0 = _py_local_tk
        _slot_1 = lcl_0
        lcl_0 = (_slot_1 is None)
        if lcl_0:
            lcl_0 = prim__tokens.offset
            lcl_0 = (lcl_0, 'quote , not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = (_slot_0, _slot_1)
            _slot_local__1 = lcl_0
            lcl_0 = parse_Exp(prim__state, prim__tokens)
            _slot_2_check = lcl_0
            lcl_0 = _slot_2_check[0]
            lcl_0 = (lcl_0 is False)
            if lcl_0:
                lcl_0 = _slot_2_check
            else:
                lcl_0 = _slot_2_check[1]
                lcl_0 = lcl_0
                _slot_2 = lcl_0
                lcl_0 = (_slot_local__1, _slot_2)
                lcl_0 = prim__mk__ast('CommaExps', lcl_0)
                _slot_local__2 = lcl_0
                lcl_0 = (True, _slot_local__2)
        return lcl_0

    def lr_loop_CommaExps(_slot_0, prim__state, prim__tokens):
        lr_CommaExps_reduce = _slot_0
        lcl_0 = prim__tokens.offset
        _off_0 = lcl_0
        lcl_0 = lr_step_CommaExps(lr_CommaExps_reduce, prim__state, prim__tokens)
        lr_CommaExps_try = lcl_0
        lcl_0 = lr_CommaExps_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_0 = prim__tokens.offset
            _off_0 = lcl_0
            lcl_0 = lr_CommaExps_try[1]
            lcl_0 = lcl_0
            lr_CommaExps_reduce = lcl_0
            lcl_0 = lr_step_CommaExps(lr_CommaExps_reduce, prim__state, prim__tokens)
            lr_CommaExps_try = lcl_0
            lcl_0 = lr_CommaExps_try[0]
            lcl_0 = (lcl_0 is not False)
        prim__tokens.offset = _off_0
        return lr_CommaExps_reduce

    def lr_step_DotId(_slot_0, prim__state, prim__tokens):
        lcl_0 = 12
        try:
            _py_local_tk = prim__tokens.array[prim__tokens.offset]
            if (_py_local_tk.idint is lcl_0):
                prim__tokens.offset += 1
            else:
                _py_local_tk = None
        except IndexError:
            _py_local_tk = None
        lcl_0 = _py_local_tk
        _slot_1 = lcl_0
        lcl_0 = (_slot_1 is None)
        if lcl_0:
            lcl_0 = prim__tokens.offset
            lcl_0 = (lcl_0, 'quote . not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = (_slot_0, _slot_1)
            _slot_local__1 = lcl_0
            lcl_0 = parse_Id(prim__state, prim__tokens)
            _slot_2_check = lcl_0
            lcl_0 = _slot_2_check[0]
            lcl_0 = (lcl_0 is False)
            if lcl_0:
                lcl_0 = _slot_2_check
            else:
                lcl_0 = _slot_2_check[1]
                lcl_0 = lcl_0
                _slot_2 = lcl_0
                lcl_0 = (_slot_local__1, _slot_2)
                lcl_0 = prim__mk__ast('DotId', lcl_0)
                _slot_local__2 = lcl_0
                lcl_0 = (True, _slot_local__2)
        return lcl_0

    def lr_loop_DotId(_slot_0, prim__state, prim__tokens):
        lr_DotId_reduce = _slot_0
        lcl_0 = prim__tokens.offset
        _off_0 = lcl_0
        lcl_0 = lr_step_DotId(lr_DotId_reduce, prim__state, prim__tokens)
        lr_DotId_try = lcl_0
        lcl_0 = lr_DotId_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_0 = prim__tokens.offset
            _off_0 = lcl_0
            lcl_0 = lr_DotId_try[1]
            lcl_0 = lcl_0
            lr_DotId_reduce = lcl_0
            lcl_0 = lr_step_DotId(lr_DotId_reduce, prim__state, prim__tokens)
            lr_DotId_try = lcl_0
            lcl_0 = lr_DotId_try[0]
            lcl_0 = (lcl_0 is not False)
        prim__tokens.offset = _off_0
        return lr_DotId_reduce

    def lr_step_Exp(_slot_0, prim__state, prim__tokens):
        lcl_0 = 10
        try:
            _py_local_tk = prim__tokens.array[prim__tokens.offset]
            if (_py_local_tk.idint is lcl_0):
                prim__tokens.offset += 1
            else:
                _py_local_tk = None
        except IndexError:
            _py_local_tk = None
        lcl_0 = _py_local_tk
        _slot_1 = lcl_0
        lcl_0 = (_slot_1 is None)
        if lcl_0:
            lcl_0 = prim__tokens.offset
            lcl_0 = (lcl_0, 'quote ( not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = parse_CommaExps(prim__state, prim__tokens)
            _slot_2_check = lcl_0
            lcl_0 = _slot_2_check[0]
            lcl_0 = (lcl_0 is False)
            if lcl_0:
                lcl_0 = _slot_2_check
            else:
                lcl_1 = _slot_2_check[1]
                lcl_1 = lcl_1
                _slot_2 = lcl_1
                lcl_1 = 11
                try:
                    _py_local_tk = prim__tokens.array[prim__tokens.offset]
                    if (_py_local_tk.idint is lcl_1):
                        prim__tokens.offset += 1
                    else:
                        _py_local_tk = None
                except IndexError:
                    _py_local_tk = None
                lcl_1 = _py_local_tk
                _slot_3 = lcl_1
                lcl_1 = (_slot_3 is None)
                if lcl_1:
                    lcl_1 = prim__tokens.offset
                    lcl_1 = (lcl_1, 'quote ) not match')
                    lcl_1 = prim__cons(lcl_1, prim__nil)
                    lcl_1 = lcl_1
                    lcl_1 = (False, lcl_1)
                else:
                    lcl_1 = prim__tokens.offset
                    _off_2 = lcl_1
                    lcl_1 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                    if lcl_1:
                        lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
                        lcl_2 = lcl_2.idint
                        if (lcl_2 == 25):
                            _py_local_i = prim__tokens.offset
                            _py_local_t = prim__tokens.array[_py_local_i]
                            prim__tokens.offset = (_py_local_i + 1)
                            lcl_2 = _py_local_t
                            _slot_4 = lcl_2
                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                            lcl_2 = prim__mk__ast('App', lcl_2)
                            _slot_local__1 = lcl_2
                            lcl_2 = (_slot_local__1,)
                            lcl_2 = prim__mk__ast('AtomExp', lcl_2)
                            _slot_local__2 = lcl_2
                            lcl_2 = (_slot_local__2,)
                            lcl_2 = prim__mk__ast('Exp', lcl_2)
                            _slot_local__3 = lcl_2
                            lcl_2 = (True, _slot_local__3)
                            lcl_1 = lcl_2
                        elif (lcl_2 == 10):
                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3)
                            lcl_2 = prim__mk__ast('App', lcl_2)
                            _slot_local__1 = lcl_2
                            lcl_2 = (_slot_local__1,)
                            lcl_2 = prim__mk__ast('AtomExp', lcl_2)
                            _slot_local__2 = lcl_2
                            lcl_2 = (_slot_local__2,)
                            lcl_2 = prim__mk__ast('Exp', lcl_2)
                            _slot_local__3 = lcl_2
                            lcl_2 = (True, _slot_local__3)
                            lcl_1 = lcl_2
                        else:
                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3)
                            lcl_2 = prim__mk__ast('App', lcl_2)
                            _slot_local__1 = lcl_2
                            lcl_2 = (_slot_local__1,)
                            lcl_2 = prim__mk__ast('AtomExp', lcl_2)
                            _slot_local__2 = lcl_2
                            lcl_2 = (_slot_local__2,)
                            lcl_2 = prim__mk__ast('Exp', lcl_2)
                            _slot_local__3 = lcl_2
                            lcl_2 = (True, _slot_local__3)
                            lcl_1 = lcl_2
                    else:
                        lcl_1 = (_off_2, 'Exp got EOF')
                        lcl_1 = prim__cons(lcl_1, prim__nil)
                        lcl_1 = lcl_1
                        lcl_1 = (False, lcl_1)
                lcl_0 = lcl_1
        return lcl_0

    def lr_loop_Exp(_slot_0, prim__state, prim__tokens):
        lr_Exp_reduce = _slot_0
        lcl_0 = prim__tokens.offset
        _off_0 = lcl_0
        lcl_0 = lr_step_Exp(lr_Exp_reduce, prim__state, prim__tokens)
        lr_Exp_try = lcl_0
        lcl_0 = lr_Exp_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_0 = prim__tokens.offset
            _off_0 = lcl_0
            lcl_0 = lr_Exp_try[1]
            lcl_0 = lcl_0
            lr_Exp_reduce = lcl_0
            lcl_0 = lr_step_Exp(lr_Exp_reduce, prim__state, prim__tokens)
            lr_Exp_try = lcl_0
            lcl_0 = lr_Exp_try[0]
            lcl_0 = (lcl_0 is not False)
        prim__tokens.offset = _off_0
        return lr_Exp_reduce

    def lr_step_Ids(_slot_0, prim__state, prim__tokens):
        lcl_0 = parse_Id(prim__state, prim__tokens)
        _slot_1_check = lcl_0
        lcl_0 = _slot_1_check[0]
        lcl_0 = (lcl_0 is False)
        if lcl_0:
            lcl_0 = _slot_1_check
        else:
            lcl_0 = _slot_1_check[1]
            lcl_0 = lcl_0
            _slot_1 = lcl_0
            lcl_0 = (_slot_0, _slot_1)
            lcl_0 = prim__mk__ast('Ids', lcl_0)
            _slot_local__1 = lcl_0
            lcl_0 = (True, _slot_local__1)
        return lcl_0

    def lr_loop_Ids(_slot_0, prim__state, prim__tokens):
        lr_Ids_reduce = _slot_0
        lcl_0 = prim__tokens.offset
        _off_0 = lcl_0
        lcl_0 = lr_step_Ids(lr_Ids_reduce, prim__state, prim__tokens)
        lr_Ids_try = lcl_0
        lcl_0 = lr_Ids_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_0 = prim__tokens.offset
            _off_0 = lcl_0
            lcl_0 = lr_Ids_try[1]
            lcl_0 = lcl_0
            lr_Ids_reduce = lcl_0
            lcl_0 = lr_step_Ids(lr_Ids_reduce, prim__state, prim__tokens)
            lr_Ids_try = lcl_0
            lcl_0 = lr_Ids_try[0]
            lcl_0 = (lcl_0 is not False)
        prim__tokens.offset = _off_0
        return lr_Ids_reduce

    def lr_step_Stmts(_slot_0, prim__state, prim__tokens):
        lcl_0 = parse_Stmt(prim__state, prim__tokens)
        _slot_1_check = lcl_0
        lcl_0 = _slot_1_check[0]
        lcl_0 = (lcl_0 is False)
        if lcl_0:
            lcl_0 = _slot_1_check
        else:
            lcl_0 = _slot_1_check[1]
            lcl_0 = lcl_0
            _slot_1 = lcl_0
            lcl_0 = (_slot_0, _slot_1)
            lcl_0 = prim__mk__ast('Stmts', lcl_0)
            _slot_local__1 = lcl_0
            lcl_0 = (True, _slot_local__1)
        return lcl_0

    def lr_loop_Stmts(_slot_0, prim__state, prim__tokens):
        lr_Stmts_reduce = _slot_0
        lcl_0 = prim__tokens.offset
        _off_0 = lcl_0
        lcl_0 = lr_step_Stmts(lr_Stmts_reduce, prim__state, prim__tokens)
        lr_Stmts_try = lcl_0
        lcl_0 = lr_Stmts_try[0]
        lcl_0 = (lcl_0 is not False)
        while lcl_0:
            lcl_0 = prim__tokens.offset
            _off_0 = lcl_0
            lcl_0 = lr_Stmts_try[1]
            lcl_0 = lcl_0
            lr_Stmts_reduce = lcl_0
            lcl_0 = lr_step_Stmts(lr_Stmts_reduce, prim__state, prim__tokens)
            lr_Stmts_try = lcl_0
            lcl_0 = lr_Stmts_try[0]
            lcl_0 = (lcl_0 is not False)
        prim__tokens.offset = _off_0
        return lr_Stmts_reduce

    def parse_Case(prim__state, prim__tokens):
        lcl_0 = prim__tokens.offset
        _off_0 = lcl_0
        lcl_0 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
        if lcl_0:
            lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
            lcl_2 = lcl_2.idint
            if (lcl_2 == 5):
                lcl_2 = parse_LitCase(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('Case', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (True, _slot_local__1)
                lcl_1 = lcl_2
            elif (lcl_2 == 15):
                lcl_2 = parse_LitCase(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_3 = _slot_0_check[1]
                    lcl_3 = lcl_3
                    _slot_0 = lcl_3
                    lcl_3 = (_slot_0,)
                    lcl_3 = prim__mk__ast('Case', lcl_3)
                    _slot_local__1 = lcl_3
                    lcl_3 = (True, _slot_local__1)
                    lcl_2 = lcl_3
                lcl_1 = lcl_2
            elif (lcl_2 == 26):
                lcl_2 = parse_LitCase(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_3 = _slot_0_check[0]
                lcl_2 = (lcl_3 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('Case', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (True, _slot_local__1)
                lcl_1 = lcl_2
            elif (lcl_2 == 10):
                lcl_2 = parse_LitCase(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_3 = _slot_0_check[1]
                    lcl_3 = lcl_3
                    _slot_0 = lcl_3
                    lcl_3 = (_slot_0,)
                    lcl_3 = prim__mk__ast('Case', lcl_3)
                    _slot_local__1 = lcl_3
                    lcl_3 = (True, _slot_local__1)
                    lcl_2 = lcl_3
                lcl_1 = lcl_2
            elif (lcl_2 == 2):
                lcl_2 = parse_LitCase(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_3 = _slot_0_check[0]
                lcl_2 = (lcl_3 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('Case', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (True, _slot_local__1)
                lcl_1 = lcl_2
            elif (lcl_2 == 4):
                lcl_2 = parse_Recogniser(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_3 = _slot_0_check[1]
                    lcl_3 = lcl_3
                    _slot_0 = lcl_3
                    lcl_3 = (_slot_0,)
                    lcl_3 = prim__mk__ast('Case', lcl_3)
                    _slot_local__1 = lcl_3
                    lcl_3 = (True, _slot_local__1)
                    lcl_2 = lcl_3
                lcl_1 = lcl_2
            else:
                lcl_2 = (_off_0, 'Case lookahead failed')
                lcl_3 = prim__cons(lcl_2, prim__nil)
                lcl_2 = lcl_3
                lcl_2 = (False, lcl_2)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        else:
            lcl_1 = (_off_0, 'Case got EOF')
            lcl_1 = prim__cons(lcl_1, prim__nil)
            lcl_1 = lcl_1
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        return lcl_0

    def parse_CaseExp(prim__state, prim__tokens):
        lcl_0 = 14
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
            lcl_0 = (lcl_0, 'quote | not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = parse_Case(prim__state, prim__tokens)
            _slot_1_check = lcl_0
            lcl_0 = _slot_1_check[0]
            lcl_0 = (lcl_0 is False)
            if lcl_0:
                lcl_0 = _slot_1_check
            else:
                lcl_1 = _slot_1_check[1]
                lcl_1 = lcl_1
                _slot_1 = lcl_1
                lcl_1 = 6
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
                    lcl_1 = (lcl_1, 'quote -> not match')
                    lcl_1 = prim__cons(lcl_1, prim__nil)
                    lcl_1 = lcl_1
                    lcl_1 = (False, lcl_1)
                else:
                    lcl_1 = parse_Exp(prim__state, prim__tokens)
                    _slot_3_check = lcl_1
                    lcl_1 = _slot_3_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_3_check
                    else:
                        lcl_2 = _slot_3_check[1]
                        lcl_2 = lcl_2
                        _slot_3 = lcl_2
                        lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3)
                        lcl_2 = prim__mk__ast('CaseExp', lcl_2)
                        _slot_local__1 = lcl_2
                        lcl_2 = (True, _slot_local__1)
                        lcl_1 = lcl_2
                lcl_0 = lcl_1
        return lcl_0

    def parse_CaseExps(prim__state, prim__tokens):
        lcl_0 = parse_CaseExp(prim__state, prim__tokens)
        _slot_0_check = lcl_0
        lcl_0 = _slot_0_check[0]
        lcl_0 = (lcl_0 is False)
        if lcl_0:
            lcl_0 = _slot_0_check
        else:
            lcl_0 = _slot_0_check[1]
            lcl_0 = lcl_0
            _slot_0 = lcl_0
            lcl_0 = (_slot_0,)
            lcl_0 = prim__mk__ast('CaseExps', lcl_0)
            _slot_local__1 = lcl_0
            lcl_0 = lr_loop_CaseExps(_slot_local__1, prim__state, prim__tokens)
            lcl_0 = (True, lcl_0)
        return lcl_0

    def parse_CommaCases(prim__state, prim__tokens):
        lcl_0 = parse_Case(prim__state, prim__tokens)
        _slot_0_check = lcl_0
        lcl_0 = _slot_0_check[0]
        lcl_0 = (lcl_0 is False)
        if lcl_0:
            lcl_0 = _slot_0_check
        else:
            lcl_0 = _slot_0_check[1]
            lcl_0 = lcl_0
            _slot_0 = lcl_0
            lcl_0 = (_slot_0,)
            lcl_0 = prim__mk__ast('CommaCases', lcl_0)
            _slot_local__1 = lcl_0
            lcl_0 = lr_loop_CommaCases(_slot_local__1, prim__state, prim__tokens)
            lcl_0 = (True, lcl_0)
        return lcl_0

    def parse_CommaExps(prim__state, prim__tokens):
        lcl_0 = parse_Exp(prim__state, prim__tokens)
        _slot_0_check = lcl_0
        lcl_0 = _slot_0_check[0]
        lcl_0 = (lcl_0 is False)
        if lcl_0:
            lcl_0 = _slot_0_check
        else:
            lcl_0 = _slot_0_check[1]
            lcl_0 = lcl_0
            _slot_0 = lcl_0
            lcl_0 = (_slot_0,)
            lcl_0 = prim__mk__ast('CommaExps', lcl_0)
            _slot_local__1 = lcl_0
            lcl_0 = lr_loop_CommaExps(_slot_local__1, prim__state, prim__tokens)
            lcl_0 = (True, lcl_0)
        return lcl_0

    def parse_DotId(prim__state, prim__tokens):
        lcl_0 = parse_Id(prim__state, prim__tokens)
        _slot_0_check = lcl_0
        lcl_0 = _slot_0_check[0]
        lcl_0 = (lcl_0 is False)
        if lcl_0:
            lcl_0 = _slot_0_check
        else:
            lcl_0 = _slot_0_check[1]
            lcl_0 = lcl_0
            _slot_0 = lcl_0
            lcl_0 = (_slot_0,)
            lcl_0 = prim__mk__ast('DotId', lcl_0)
            _slot_local__1 = lcl_0
            lcl_0 = lr_loop_DotId(_slot_local__1, prim__state, prim__tokens)
            lcl_0 = (True, lcl_0)
        return lcl_0

    def parse_Exp(prim__state, prim__tokens):
        lcl_0 = prim__tokens.offset
        _off_0 = lcl_0
        lcl_0 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
        if lcl_0:
            lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
            lcl_2 = lcl_2.idint
            if (lcl_2 == 5):
                lcl_2 = parse_Lit(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('AtomExp', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (_slot_local__1,)
                    lcl_2 = prim__mk__ast('Exp', lcl_2)
                    _slot_local__2 = lcl_2
                    lcl_2 = lr_loop_Exp(_slot_local__2, prim__state, prim__tokens)
                    lcl_2 = (True, lcl_2)
                lcl_1 = lcl_2
            elif (lcl_2 == 18):
                lcl_2 = parse_InExp(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('AtomExp', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (_slot_local__1,)
                    lcl_2 = prim__mk__ast('Exp', lcl_2)
                    _slot_local__2 = lcl_2
                    lcl_2 = lr_loop_Exp(_slot_local__2, prim__state, prim__tokens)
                    lcl_2 = (True, lcl_2)
                lcl_1 = lcl_2
            elif (lcl_2 == 28):
                lcl_2 = parse_Match(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('AtomExp', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (_slot_local__1,)
                    lcl_2 = prim__mk__ast('Exp', lcl_2)
                    _slot_local__2 = lcl_2
                    lcl_2 = lr_loop_Exp(_slot_local__2, prim__state, prim__tokens)
                    lcl_2 = (True, lcl_2)
                lcl_1 = lcl_2
            elif (lcl_2 == 17):
                lcl_2 = parse_InExp(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('AtomExp', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (_slot_local__1,)
                    lcl_2 = prim__mk__ast('Exp', lcl_2)
                    _slot_local__2 = lcl_2
                    lcl_2 = lr_loop_Exp(_slot_local__2, prim__state, prim__tokens)
                    lcl_2 = (True, lcl_2)
                lcl_1 = lcl_2
            elif (lcl_2 == 20):
                lcl_2 = parse_If(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('AtomExp', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (_slot_local__1,)
                    lcl_2 = prim__mk__ast('Exp', lcl_2)
                    _slot_local__2 = lcl_2
                    lcl_2 = lr_loop_Exp(_slot_local__2, prim__state, prim__tokens)
                    lcl_2 = (True, lcl_2)
                lcl_1 = lcl_2
            elif (lcl_2 == 24):
                lcl_2 = parse_Lam(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('AtomExp', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (_slot_local__1,)
                    lcl_2 = prim__mk__ast('Exp', lcl_2)
                    _slot_local__2 = lcl_2
                    lcl_2 = lr_loop_Exp(_slot_local__2, prim__state, prim__tokens)
                    lcl_2 = (True, lcl_2)
                lcl_1 = lcl_2
            elif (lcl_2 == 26):
                lcl_2 = parse_Lit(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('AtomExp', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (_slot_local__1,)
                    lcl_2 = prim__mk__ast('Exp', lcl_2)
                    _slot_local__2 = lcl_2
                    lcl_2 = lr_loop_Exp(_slot_local__2, prim__state, prim__tokens)
                    lcl_2 = (True, lcl_2)
                lcl_1 = lcl_2
            elif (lcl_2 == 10):
                lcl_2 = prim__tokens.offset
                _off_1 = lcl_2
                lcl_2 = prim__tokens.offset
                _off_2 = lcl_2
                _py_local_i = prim__tokens.offset
                _py_local_t = prim__tokens.array[_py_local_i]
                prim__tokens.offset = (_py_local_i + 1)
                lcl_2 = _py_local_t
                _slot_0 = lcl_2
                lcl_2 = parse_Exp(prim__state, prim__tokens)
                _slot_1_check = lcl_2
                lcl_2 = _slot_1_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_1_check
                else:
                    lcl_3 = _slot_1_check[1]
                    lcl_3 = lcl_3
                    _slot_1 = lcl_3
                    lcl_3 = 11
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
                        lcl_3 = (_slot_0, _slot_1, _slot_2)
                        lcl_3 = prim__mk__ast('AtomExp', lcl_3)
                        _slot_local__1 = lcl_3
                        lcl_3 = (_slot_local__1,)
                        lcl_3 = prim__mk__ast('Exp', lcl_3)
                        _slot_local__2 = lcl_3
                        lcl_3 = lr_loop_Exp(_slot_local__2, prim__state, prim__tokens)
                        lcl_3 = (True, lcl_3)
                    lcl_2 = lcl_3
                lcl_1 = lcl_2
            elif (lcl_2 == 2):
                lcl_2 = parse_Lit(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_3 = _slot_0_check[0]
                lcl_2 = (lcl_3 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('AtomExp', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (_slot_local__1,)
                    lcl_2 = prim__mk__ast('Exp', lcl_2)
                    _slot_local__2 = lcl_2
                    lcl_2 = lr_loop_Exp(_slot_local__2, prim__state, prim__tokens)
                    lcl_2 = (True, lcl_2)
                lcl_1 = lcl_2
            elif (lcl_2 == 4):
                lcl_2 = parse_Lit(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('AtomExp', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (_slot_local__1,)
                    lcl_2 = prim__mk__ast('Exp', lcl_2)
                    _slot_local__2 = lcl_2
                    lcl_2 = lr_loop_Exp(_slot_local__2, prim__state, prim__tokens)
                    lcl_2 = (True, lcl_2)
                lcl_1 = lcl_2
            else:
                lcl_2 = (_off_0, 'Exp lookahead failed')
                lcl_2 = prim__cons(lcl_2, prim__nil)
                lcl_2 = lcl_2
                lcl_2 = (False, lcl_2)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        else:
            lcl_1 = (_off_0, 'Exp got EOF')
            lcl_1 = prim__cons(lcl_1, prim__nil)
            lcl_1 = lcl_1
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        return lcl_0

    def parse_Id(prim__state, prim__tokens):
        lcl_0 = 4
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
            lcl_0 = (lcl_0, 'identifier not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = (_slot_0,)
            lcl_0 = prim__mk__ast('Id', lcl_0)
            _slot_local__1 = lcl_0
            lcl_0 = (True, _slot_local__1)
        return lcl_0

    def parse_Ids(prim__state, prim__tokens):
        lcl_0 = parse_Id(prim__state, prim__tokens)
        _slot_0_check = lcl_0
        lcl_0 = _slot_0_check[0]
        lcl_0 = (lcl_0 is False)
        if lcl_0:
            lcl_0 = _slot_0_check
        else:
            lcl_0 = _slot_0_check[1]
            lcl_0 = lcl_0
            _slot_0 = lcl_0
            lcl_0 = (_slot_0,)
            lcl_0 = prim__mk__ast('Ids', lcl_0)
            _slot_local__1 = lcl_0
            lcl_0 = lr_loop_Ids(_slot_local__1, prim__state, prim__tokens)
            lcl_0 = (True, lcl_0)
        return lcl_0

    def parse_If(prim__state, prim__tokens):
        lcl_0 = 20
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
            lcl_0 = (lcl_0, 'quote if not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = parse_Exp(prim__state, prim__tokens)
            _slot_1_check = lcl_0
            lcl_0 = _slot_1_check[0]
            lcl_0 = (lcl_0 is False)
            if lcl_0:
                lcl_0 = _slot_1_check
            else:
                lcl_1 = _slot_1_check[1]
                lcl_1 = lcl_1
                _slot_1 = lcl_1
                lcl_1 = 21
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
                    lcl_1 = (lcl_1, 'quote then not match')
                    lcl_1 = prim__cons(lcl_1, prim__nil)
                    lcl_1 = lcl_1
                    lcl_1 = (False, lcl_1)
                else:
                    lcl_1 = parse_Exp(prim__state, prim__tokens)
                    _slot_3_check = lcl_1
                    lcl_1 = _slot_3_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_3_check
                    else:
                        lcl_2 = _slot_3_check[1]
                        lcl_2 = lcl_2
                        _slot_3 = lcl_2
                        lcl_2 = 22
                        try:
                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                            if (_py_local_tk.idint is lcl_2):
                                prim__tokens.offset += 1
                            else:
                                _py_local_tk = None
                        except IndexError:
                            _py_local_tk = None
                        lcl_2 = _py_local_tk
                        _slot_4 = lcl_2
                        lcl_2 = (_slot_4 is None)
                        if lcl_2:
                            lcl_2 = prim__tokens.offset
                            lcl_2 = (lcl_2, 'quote else not match')
                            lcl_2 = prim__cons(lcl_2, prim__nil)
                            lcl_2 = lcl_2
                            lcl_2 = (False, lcl_2)
                        else:
                            lcl_2 = parse_Exp(prim__state, prim__tokens)
                            _slot_5_check = lcl_2
                            lcl_2 = _slot_5_check[0]
                            lcl_2 = (lcl_2 is False)
                            if lcl_2:
                                lcl_2 = _slot_5_check
                            else:
                                lcl_3 = _slot_5_check[1]
                                lcl_3 = lcl_3
                                _slot_5 = lcl_3
                                lcl_3 = prim__tokens.offset
                                _off_3 = lcl_3
                                lcl_3 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                                if lcl_3:
                                    lcl_5 = prim__tokens.array[(prim__tokens.offset + 0)]
                                    lcl_5 = lcl_5.idint
                                    if (lcl_5 == 23):
                                        _py_local_i = prim__tokens.offset
                                        _py_local_t = prim__tokens.array[_py_local_i]
                                        prim__tokens.offset = (_py_local_i + 1)
                                        lcl_5 = _py_local_t
                                        _slot_6 = lcl_5
                                        lcl_5 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4, _slot_5, _slot_6)
                                        lcl_5 = prim__mk__ast('If', lcl_5)
                                        _slot_local__1 = lcl_5
                                        lcl_5 = (True, _slot_local__1)
                                        lcl_4 = lcl_5
                                    else:
                                        lcl_5 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4, _slot_5)
                                        lcl_5 = prim__mk__ast('If', lcl_5)
                                        _slot_local__1 = lcl_5
                                        lcl_5 = (True, _slot_local__1)
                                        lcl_4 = lcl_5
                                    lcl_3 = lcl_4
                                else:
                                    lcl_4 = (_off_3, 'If got EOF')
                                    lcl_5 = prim__cons(lcl_4, prim__nil)
                                    lcl_4 = lcl_5
                                    lcl_4 = (False, lcl_4)
                                    lcl_3 = lcl_4
                                lcl_2 = lcl_3
                        lcl_1 = lcl_2
                lcl_0 = lcl_1
        return lcl_0

    def parse_InExp(prim__state, prim__tokens):
        lcl_0 = parse_Stmt(prim__state, prim__tokens)
        _slot_0_check = lcl_0
        lcl_0 = _slot_0_check[0]
        lcl_0 = (lcl_0 is False)
        if lcl_0:
            lcl_0 = _slot_0_check
        else:
            lcl_0 = _slot_0_check[1]
            lcl_0 = lcl_0
            _slot_0 = lcl_0
            lcl_0 = 16
            try:
                _py_local_tk = prim__tokens.array[prim__tokens.offset]
                if (_py_local_tk.idint is lcl_0):
                    prim__tokens.offset += 1
                else:
                    _py_local_tk = None
            except IndexError:
                _py_local_tk = None
            lcl_0 = _py_local_tk
            _slot_1 = lcl_0
            lcl_0 = (_slot_1 is None)
            if lcl_0:
                lcl_0 = prim__tokens.offset
                lcl_0 = (lcl_0, 'quote in not match')
                lcl_0 = prim__cons(lcl_0, prim__nil)
                lcl_0 = lcl_0
                lcl_0 = (False, lcl_0)
            else:
                lcl_0 = parse_Exp(prim__state, prim__tokens)
                _slot_2_check = lcl_0
                lcl_0 = _slot_2_check[0]
                lcl_0 = (lcl_0 is False)
                if lcl_0:
                    lcl_0 = _slot_2_check
                else:
                    lcl_1 = _slot_2_check[1]
                    lcl_1 = lcl_1
                    _slot_2 = lcl_1
                    lcl_1 = (_slot_0, _slot_1, _slot_2)
                    lcl_1 = prim__mk__ast('InExp', lcl_1)
                    _slot_local__1 = lcl_1
                    lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
        return lcl_0

    def parse_Lam(prim__state, prim__tokens):
        lcl_0 = 24
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
            lcl_0 = (lcl_0, 'quote fun not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = prim__tokens.offset
            _off_1 = lcl_0
            lcl_0 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
            if lcl_0:
                lcl_1 = prim__tokens.array[(prim__tokens.offset + 0)]
                lcl_1 = lcl_1.idint
                if (lcl_1 == 6):
                    _py_local_i = prim__tokens.offset
                    _py_local_t = prim__tokens.array[_py_local_i]
                    prim__tokens.offset = (_py_local_i + 1)
                    lcl_1 = _py_local_t
                    _slot_1 = lcl_1
                    lcl_1 = parse_Exp(prim__state, prim__tokens)
                    _slot_2_check = lcl_1
                    lcl_1 = _slot_2_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_2_check
                    else:
                        lcl_2 = _slot_2_check[1]
                        lcl_2 = lcl_2
                        _slot_2 = lcl_2
                        lcl_2 = prim__tokens.offset
                        _off_2 = lcl_2
                        lcl_2 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                        if lcl_2:
                            lcl_4 = prim__tokens.array[(prim__tokens.offset + 0)]
                            lcl_4 = lcl_4.idint
                            if (lcl_4 == 23):
                                _py_local_i = prim__tokens.offset
                                _py_local_t = prim__tokens.array[_py_local_i]
                                prim__tokens.offset = (_py_local_i + 1)
                                lcl_4 = _py_local_t
                                _slot_3 = lcl_4
                                lcl_4 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                lcl_4 = prim__mk__ast('Lam', lcl_4)
                                _slot_local__1 = lcl_4
                                lcl_4 = (True, _slot_local__1)
                                lcl_3 = lcl_4
                            else:
                                lcl_4 = (_slot_0, _slot_1, _slot_2)
                                lcl_4 = prim__mk__ast('Lam', lcl_4)
                                _slot_local__1 = lcl_4
                                lcl_4 = (True, _slot_local__1)
                                lcl_3 = lcl_4
                            lcl_2 = lcl_3
                        else:
                            lcl_3 = (_off_2, 'Lam got EOF')
                            lcl_4 = prim__cons(lcl_3, prim__nil)
                            lcl_3 = lcl_4
                            lcl_3 = (False, lcl_3)
                            lcl_2 = lcl_3
                        lcl_1 = lcl_2
                    lcl_0 = lcl_1
                elif (lcl_1 == 4):
                    lcl_1 = parse_Ids(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_2 = _slot_1_check[0]
                    lcl_1 = (lcl_2 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 6
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
                            lcl_1 = (lcl_1, 'quote -> not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = parse_Exp(prim__state, prim__tokens)
                            _slot_3_check = lcl_1
                            lcl_1 = _slot_3_check[0]
                            lcl_1 = (lcl_1 is False)
                            if lcl_1:
                                lcl_1 = _slot_3_check
                            else:
                                lcl_2 = _slot_3_check[1]
                                lcl_2 = lcl_2
                                _slot_3 = lcl_2
                                lcl_2 = prim__tokens.offset
                                _off_3 = lcl_2
                                lcl_2 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                                if lcl_2:
                                    lcl_4 = prim__tokens.array[(prim__tokens.offset + 0)]
                                    lcl_4 = lcl_4.idint
                                    if (lcl_4 == 23):
                                        _py_local_i = prim__tokens.offset
                                        _py_local_t = prim__tokens.array[_py_local_i]
                                        prim__tokens.offset = (_py_local_i + 1)
                                        lcl_4 = _py_local_t
                                        _slot_4 = lcl_4
                                        lcl_4 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                        lcl_4 = prim__mk__ast('Lam', lcl_4)
                                        _slot_local__1 = lcl_4
                                        lcl_4 = (True, _slot_local__1)
                                        lcl_3 = lcl_4
                                    else:
                                        lcl_4 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                        lcl_4 = prim__mk__ast('Lam', lcl_4)
                                        _slot_local__1 = lcl_4
                                        lcl_4 = (True, _slot_local__1)
                                        lcl_3 = lcl_4
                                    lcl_2 = lcl_3
                                else:
                                    lcl_3 = (_off_3, 'Lam got EOF')
                                    lcl_4 = prim__cons(lcl_3, prim__nil)
                                    lcl_3 = lcl_4
                                    lcl_3 = (False, lcl_3)
                                    lcl_2 = lcl_3
                                lcl_1 = lcl_2
                    lcl_0 = lcl_1
                else:
                    lcl_1 = (_off_1, 'Lam lookahead failed')
                    lcl_2 = prim__cons(lcl_1, prim__nil)
                    lcl_1 = lcl_2
                    lcl_1 = (False, lcl_1)
                    lcl_0 = lcl_1
            else:
                lcl_0 = (_off_1, 'Lam got EOF')
                lcl_0 = prim__cons(lcl_0, prim__nil)
                lcl_0 = lcl_0
                lcl_0 = (False, lcl_0)
        return lcl_0

    def parse_Let(prim__state, prim__tokens):
        lcl_0 = 17
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
            lcl_0 = (lcl_0, 'quote let not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = parse_Id(prim__state, prim__tokens)
            _slot_1_check = lcl_0
            lcl_0 = _slot_1_check[0]
            lcl_0 = (lcl_0 is False)
            if lcl_0:
                lcl_0 = _slot_1_check
            else:
                lcl_1 = _slot_1_check[1]
                lcl_1 = lcl_1
                _slot_1 = lcl_1
                lcl_1 = 13
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
                    lcl_1 = (lcl_1, 'quote = not match')
                    lcl_1 = prim__cons(lcl_1, prim__nil)
                    lcl_1 = lcl_1
                    lcl_1 = (False, lcl_1)
                else:
                    lcl_1 = parse_Exp(prim__state, prim__tokens)
                    _slot_3_check = lcl_1
                    lcl_1 = _slot_3_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_3_check
                    else:
                        lcl_2 = _slot_3_check[1]
                        lcl_2 = lcl_2
                        _slot_3 = lcl_2
                        lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3)
                        lcl_2 = prim__mk__ast('Let', lcl_2)
                        _slot_local__1 = lcl_2
                        lcl_2 = (True, _slot_local__1)
                        lcl_1 = lcl_2
                lcl_0 = lcl_1
        return lcl_0

    def parse_List(prim__state, prim__tokens):
        lcl_0 = 26
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
            lcl_0 = (lcl_0, 'quote [ not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = prim__tokens.offset
            _off_1 = lcl_0
            lcl_0 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
            if lcl_0:
                lcl_1 = prim__tokens.array[(prim__tokens.offset + 0)]
                lcl_1 = lcl_1.idint
                if (lcl_1 == 5):
                    lcl_1 = parse_CommaExps(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 27
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
                            lcl_1 = (lcl_1, 'quote ] not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = (_slot_0, _slot_1, _slot_2)
                            lcl_1 = prim__mk__ast('List', lcl_1)
                            _slot_local__1 = lcl_1
                            lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 18):
                    lcl_1 = parse_CommaExps(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 27
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
                            lcl_1 = (lcl_1, 'quote ] not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = (_slot_0, _slot_1, _slot_2)
                            lcl_1 = prim__mk__ast('List', lcl_1)
                            _slot_local__1 = lcl_1
                            lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 28):
                    lcl_1 = parse_CommaExps(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 27
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
                            lcl_1 = (lcl_1, 'quote ] not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = (_slot_0, _slot_1, _slot_2)
                            lcl_1 = prim__mk__ast('List', lcl_1)
                            _slot_local__1 = lcl_1
                            lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 17):
                    lcl_1 = parse_CommaExps(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 27
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
                            lcl_1 = (lcl_1, 'quote ] not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = (_slot_0, _slot_1, _slot_2)
                            lcl_1 = prim__mk__ast('List', lcl_1)
                            _slot_local__1 = lcl_1
                            lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 20):
                    lcl_1 = parse_CommaExps(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 27
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
                            lcl_1 = (lcl_1, 'quote ] not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = (_slot_0, _slot_1, _slot_2)
                            lcl_1 = prim__mk__ast('List', lcl_1)
                            _slot_local__1 = lcl_1
                            lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 24):
                    lcl_1 = parse_CommaExps(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 27
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
                            lcl_1 = (lcl_1, 'quote ] not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = (_slot_0, _slot_1, _slot_2)
                            lcl_1 = prim__mk__ast('List', lcl_1)
                            _slot_local__1 = lcl_1
                            lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 27):
                    _py_local_i = prim__tokens.offset
                    _py_local_t = prim__tokens.array[_py_local_i]
                    prim__tokens.offset = (_py_local_i + 1)
                    lcl_1 = _py_local_t
                    _slot_1 = lcl_1
                    lcl_1 = (_slot_0, _slot_1)
                    lcl_1 = prim__mk__ast('List', lcl_1)
                    _slot_local__1 = lcl_1
                    lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 26):
                    lcl_1 = parse_CommaExps(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 27
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
                            lcl_1 = (lcl_1, 'quote ] not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = (_slot_0, _slot_1, _slot_2)
                            lcl_1 = prim__mk__ast('List', lcl_1)
                            _slot_local__1 = lcl_1
                            lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 10):
                    lcl_1 = parse_CommaExps(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 27
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
                            lcl_1 = (lcl_1, 'quote ] not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = (_slot_0, _slot_1, _slot_2)
                            lcl_1 = prim__mk__ast('List', lcl_1)
                            _slot_local__1 = lcl_1
                            lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 2):
                    lcl_1 = parse_CommaExps(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 27
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
                            lcl_1 = (lcl_1, 'quote ] not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = (_slot_0, _slot_1, _slot_2)
                            lcl_1 = prim__mk__ast('List', lcl_1)
                            _slot_local__1 = lcl_1
                            lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 4):
                    lcl_1 = parse_CommaExps(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 27
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
                            lcl_1 = (lcl_1, 'quote ] not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = (_slot_0, _slot_1, _slot_2)
                            lcl_1 = prim__mk__ast('List', lcl_1)
                            _slot_local__1 = lcl_1
                            lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                else:
                    lcl_1 = (_off_1, 'List lookahead failed')
                    lcl_1 = prim__cons(lcl_1, prim__nil)
                    lcl_1 = lcl_1
                    lcl_1 = (False, lcl_1)
                    lcl_0 = lcl_1
            else:
                lcl_0 = (_off_1, 'List got EOF')
                lcl_0 = prim__cons(lcl_0, prim__nil)
                lcl_0 = lcl_0
                lcl_0 = (False, lcl_0)
        return lcl_0

    def parse_ListCase(prim__state, prim__tokens):
        lcl_0 = 26
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
            lcl_0 = (lcl_0, 'quote [ not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = prim__tokens.offset
            _off_1 = lcl_0
            lcl_0 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
            if lcl_0:
                lcl_1 = prim__tokens.array[(prim__tokens.offset + 0)]
                lcl_1 = lcl_1.idint
                if (lcl_1 == 5):
                    lcl_1 = parse_CommaCases(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 27
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
                            lcl_1 = (lcl_1, 'quote ] not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = (_slot_0, _slot_1, _slot_2)
                            lcl_1 = prim__mk__ast('ListCase', lcl_1)
                            _slot_local__1 = lcl_1
                            lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 15):
                    lcl_1 = parse_CommaCases(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 27
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
                            lcl_1 = (lcl_1, 'quote ] not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = (_slot_0, _slot_1, _slot_2)
                            lcl_1 = prim__mk__ast('ListCase', lcl_1)
                            _slot_local__1 = lcl_1
                            lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 27):
                    _py_local_i = prim__tokens.offset
                    _py_local_t = prim__tokens.array[_py_local_i]
                    prim__tokens.offset = (_py_local_i + 1)
                    lcl_1 = _py_local_t
                    _slot_1 = lcl_1
                    lcl_1 = (_slot_0, _slot_1)
                    lcl_1 = prim__mk__ast('ListCase', lcl_1)
                    _slot_local__1 = lcl_1
                    lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 26):
                    lcl_1 = parse_CommaCases(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 27
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
                            lcl_1 = (lcl_1, 'quote ] not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = (_slot_0, _slot_1, _slot_2)
                            lcl_1 = prim__mk__ast('ListCase', lcl_1)
                            _slot_local__1 = lcl_1
                            lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 10):
                    lcl_1 = parse_CommaCases(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 27
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
                            lcl_1 = (lcl_1, 'quote ] not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = (_slot_0, _slot_1, _slot_2)
                            lcl_1 = prim__mk__ast('ListCase', lcl_1)
                            _slot_local__1 = lcl_1
                            lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 2):
                    lcl_1 = parse_CommaCases(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 27
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
                            lcl_1 = (lcl_1, 'quote ] not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = (_slot_0, _slot_1, _slot_2)
                            lcl_1 = prim__mk__ast('ListCase', lcl_1)
                            _slot_local__1 = lcl_1
                            lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 4):
                    lcl_1 = parse_CommaCases(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 27
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
                            lcl_1 = (lcl_1, 'quote ] not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = (_slot_0, _slot_1, _slot_2)
                            lcl_1 = prim__mk__ast('ListCase', lcl_1)
                            _slot_local__1 = lcl_1
                            lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                else:
                    lcl_1 = (_off_1, 'ListCase lookahead failed')
                    lcl_1 = prim__cons(lcl_1, prim__nil)
                    lcl_1 = lcl_1
                    lcl_1 = (False, lcl_1)
                    lcl_0 = lcl_1
            else:
                lcl_0 = (_off_1, 'ListCase got EOF')
                lcl_0 = prim__cons(lcl_0, prim__nil)
                lcl_0 = lcl_0
                lcl_0 = (False, lcl_0)
        return lcl_0

    def parse_Lit(prim__state, prim__tokens):
        lcl_0 = prim__tokens.offset
        _off_0 = lcl_0
        lcl_0 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
        if lcl_0:
            lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
            lcl_2 = lcl_2.idint
            if (lcl_2 == 5):
                lcl_2 = parse_Str(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('Lit', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (True, _slot_local__1)
                lcl_1 = lcl_2
            elif (lcl_2 == 26):
                lcl_2 = parse_List(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_3 = _slot_0_check[1]
                    lcl_3 = lcl_3
                    _slot_0 = lcl_3
                    lcl_3 = (_slot_0,)
                    lcl_3 = prim__mk__ast('Lit', lcl_3)
                    _slot_local__1 = lcl_3
                    lcl_3 = (True, _slot_local__1)
                    lcl_2 = lcl_3
                lcl_1 = lcl_2
            elif (lcl_2 == 10):
                lcl_2 = parse_Tuple(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_3 = _slot_0_check[0]
                lcl_2 = (lcl_3 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('Lit', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (True, _slot_local__1)
                lcl_1 = lcl_2
            elif (lcl_2 == 2):
                lcl_2 = parse_Num(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_3 = _slot_0_check[1]
                    lcl_3 = lcl_3
                    _slot_0 = lcl_3
                    lcl_3 = (_slot_0,)
                    lcl_3 = prim__mk__ast('Lit', lcl_3)
                    _slot_local__1 = lcl_3
                    lcl_3 = (True, _slot_local__1)
                    lcl_2 = lcl_3
                lcl_1 = lcl_2
            elif (lcl_2 == 4):
                lcl_2 = parse_DotId(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_3 = _slot_0_check[0]
                lcl_2 = (lcl_3 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('Lit', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (True, _slot_local__1)
                lcl_1 = lcl_2
            else:
                lcl_2 = (_off_0, 'Lit lookahead failed')
                lcl_2 = prim__cons(lcl_2, prim__nil)
                lcl_2 = lcl_2
                lcl_2 = (False, lcl_2)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        else:
            lcl_1 = (_off_0, 'Lit got EOF')
            lcl_2 = prim__cons(lcl_1, prim__nil)
            lcl_1 = lcl_2
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        return lcl_0

    def parse_LitCase(prim__state, prim__tokens):
        lcl_0 = prim__tokens.offset
        _off_0 = lcl_0
        lcl_0 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
        if lcl_0:
            lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
            lcl_2 = lcl_2.idint
            if (lcl_2 == 5):
                lcl_2 = parse_StrCase(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('LitCase', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (True, _slot_local__1)
                lcl_1 = lcl_2
            elif (lcl_2 == 15):
                lcl_2 = parse_PinCase(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_3 = _slot_0_check[1]
                    lcl_3 = lcl_3
                    _slot_0 = lcl_3
                    lcl_3 = (_slot_0,)
                    lcl_3 = prim__mk__ast('LitCase', lcl_3)
                    _slot_local__1 = lcl_3
                    lcl_3 = (True, _slot_local__1)
                    lcl_2 = lcl_3
                lcl_1 = lcl_2
            elif (lcl_2 == 26):
                lcl_2 = parse_ListCase(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_3 = _slot_0_check[0]
                lcl_2 = (lcl_3 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('LitCase', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (True, _slot_local__1)
                lcl_1 = lcl_2
            elif (lcl_2 == 10):
                lcl_2 = parse_TupleCase(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_3 = _slot_0_check[1]
                    lcl_3 = lcl_3
                    _slot_0 = lcl_3
                    lcl_3 = (_slot_0,)
                    lcl_3 = prim__mk__ast('LitCase', lcl_3)
                    _slot_local__1 = lcl_3
                    lcl_3 = (True, _slot_local__1)
                    lcl_2 = lcl_3
                lcl_1 = lcl_2
            elif (lcl_2 == 2):
                lcl_2 = parse_NumCase(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_3 = _slot_0_check[0]
                lcl_2 = (lcl_3 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('LitCase', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (True, _slot_local__1)
                lcl_1 = lcl_2
            else:
                lcl_2 = (_off_0, 'LitCase lookahead failed')
                lcl_2 = prim__cons(lcl_2, prim__nil)
                lcl_2 = lcl_2
                lcl_2 = (False, lcl_2)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        else:
            lcl_1 = (_off_0, 'LitCase got EOF')
            lcl_2 = prim__cons(lcl_1, prim__nil)
            lcl_1 = lcl_2
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        return lcl_0

    def parse_Match(prim__state, prim__tokens):
        lcl_0 = 28
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
            lcl_0 = (lcl_0, 'quote match not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = parse_Exp(prim__state, prim__tokens)
            _slot_1_check = lcl_0
            lcl_0 = _slot_1_check[0]
            lcl_0 = (lcl_0 is False)
            if lcl_0:
                lcl_0 = _slot_1_check
            else:
                lcl_1 = _slot_1_check[1]
                lcl_1 = lcl_1
                _slot_1 = lcl_1
                lcl_1 = 29
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
                    lcl_1 = (lcl_1, 'quote with not match')
                    lcl_1 = prim__cons(lcl_1, prim__nil)
                    lcl_1 = lcl_1
                    lcl_1 = (False, lcl_1)
                else:
                    lcl_1 = parse_CaseExps(prim__state, prim__tokens)
                    _slot_3_check = lcl_1
                    lcl_1 = _slot_3_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_3_check
                    else:
                        lcl_2 = _slot_3_check[1]
                        lcl_2 = lcl_2
                        _slot_3 = lcl_2
                        lcl_2 = prim__tokens.offset
                        _off_2 = lcl_2
                        lcl_2 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                        if lcl_2:
                            lcl_4 = prim__tokens.array[(prim__tokens.offset + 0)]
                            lcl_4 = lcl_4.idint
                            if (lcl_4 == 23):
                                _py_local_i = prim__tokens.offset
                                _py_local_t = prim__tokens.array[_py_local_i]
                                prim__tokens.offset = (_py_local_i + 1)
                                lcl_4 = _py_local_t
                                _slot_4 = lcl_4
                                lcl_4 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                lcl_4 = prim__mk__ast('Match', lcl_4)
                                _slot_local__1 = lcl_4
                                lcl_4 = (True, _slot_local__1)
                                lcl_3 = lcl_4
                            else:
                                lcl_4 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                lcl_4 = prim__mk__ast('Match', lcl_4)
                                _slot_local__1 = lcl_4
                                lcl_4 = (True, _slot_local__1)
                                lcl_3 = lcl_4
                            lcl_2 = lcl_3
                        else:
                            lcl_3 = (_off_2, 'Match got EOF')
                            lcl_4 = prim__cons(lcl_3, prim__nil)
                            lcl_3 = lcl_4
                            lcl_3 = (False, lcl_3)
                            lcl_2 = lcl_3
                        lcl_1 = lcl_2
                lcl_0 = lcl_1
        return lcl_0

    def parse_Mod(prim__state, prim__tokens):
        lcl_0 = 19
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
            lcl_0 = (lcl_0, 'quote module not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = parse_Id(prim__state, prim__tokens)
            _slot_1_check = lcl_0
            lcl_0 = _slot_1_check[0]
            lcl_0 = (lcl_0 is False)
            if lcl_0:
                lcl_0 = _slot_1_check
            else:
                lcl_1 = _slot_1_check[1]
                lcl_1 = lcl_1
                _slot_1 = lcl_1
                lcl_1 = 13
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
                    lcl_1 = (lcl_1, 'quote = not match')
                    lcl_1 = prim__cons(lcl_1, prim__nil)
                    lcl_1 = lcl_1
                    lcl_1 = (False, lcl_1)
                else:
                    lcl_1 = 8
                    try:
                        _py_local_tk = prim__tokens.array[prim__tokens.offset]
                        if (_py_local_tk.idint is lcl_1):
                            prim__tokens.offset += 1
                        else:
                            _py_local_tk = None
                    except IndexError:
                        _py_local_tk = None
                    lcl_1 = _py_local_tk
                    _slot_3 = lcl_1
                    lcl_1 = (_slot_3 is None)
                    if lcl_1:
                        lcl_2 = prim__tokens.offset
                        lcl_2 = (lcl_2, 'quote { not match')
                        lcl_2 = prim__cons(lcl_2, prim__nil)
                        lcl_2 = lcl_2
                        lcl_2 = (False, lcl_2)
                        lcl_1 = lcl_2
                    else:
                        lcl_2 = prim__tokens.offset
                        _off_3 = lcl_2
                        lcl_2 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                        if lcl_2:
                            lcl_3 = prim__tokens.array[(prim__tokens.offset + 0)]
                            lcl_3 = lcl_3.idint
                            if (lcl_3 == 9):
                                _py_local_i = prim__tokens.offset
                                _py_local_t = prim__tokens.array[_py_local_i]
                                prim__tokens.offset = (_py_local_i + 1)
                                lcl_3 = _py_local_t
                                _slot_4 = lcl_3
                                lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                lcl_3 = prim__mk__ast('Mod', lcl_3)
                                _slot_local__1 = lcl_3
                                lcl_3 = (True, _slot_local__1)
                                lcl_2 = lcl_3
                            elif (lcl_3 == 18):
                                lcl_3 = parse_Stmts(prim__state, prim__tokens)
                                _slot_4_check = lcl_3
                                lcl_3 = _slot_4_check[0]
                                lcl_3 = (lcl_3 is False)
                                if lcl_3:
                                    lcl_3 = _slot_4_check
                                else:
                                    lcl_3 = _slot_4_check[1]
                                    lcl_3 = lcl_3
                                    _slot_4 = lcl_3
                                    lcl_3 = 9
                                    try:
                                        _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                        if (_py_local_tk.idint is lcl_3):
                                            prim__tokens.offset += 1
                                        else:
                                            _py_local_tk = None
                                    except IndexError:
                                        _py_local_tk = None
                                    lcl_3 = _py_local_tk
                                    _slot_5 = lcl_3
                                    lcl_3 = (_slot_5 is None)
                                    if lcl_3:
                                        lcl_3 = prim__tokens.offset
                                        lcl_3 = (lcl_3, 'quote } not match')
                                        lcl_3 = prim__cons(lcl_3, prim__nil)
                                        lcl_3 = lcl_3
                                        lcl_3 = (False, lcl_3)
                                    else:
                                        lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4, _slot_5)
                                        lcl_3 = prim__mk__ast('Mod', lcl_3)
                                        _slot_local__1 = lcl_3
                                        lcl_3 = (True, _slot_local__1)
                                lcl_2 = lcl_3
                            elif (lcl_3 == 17):
                                lcl_3 = parse_Stmts(prim__state, prim__tokens)
                                _slot_4_check = lcl_3
                                lcl_3 = _slot_4_check[0]
                                lcl_3 = (lcl_3 is False)
                                if lcl_3:
                                    lcl_3 = _slot_4_check
                                else:
                                    lcl_3 = _slot_4_check[1]
                                    lcl_3 = lcl_3
                                    _slot_4 = lcl_3
                                    lcl_3 = 9
                                    try:
                                        _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                        if (_py_local_tk.idint is lcl_3):
                                            prim__tokens.offset += 1
                                        else:
                                            _py_local_tk = None
                                    except IndexError:
                                        _py_local_tk = None
                                    lcl_3 = _py_local_tk
                                    _slot_5 = lcl_3
                                    lcl_3 = (_slot_5 is None)
                                    if lcl_3:
                                        lcl_3 = prim__tokens.offset
                                        lcl_3 = (lcl_3, 'quote } not match')
                                        lcl_3 = prim__cons(lcl_3, prim__nil)
                                        lcl_3 = lcl_3
                                        lcl_3 = (False, lcl_3)
                                    else:
                                        lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4, _slot_5)
                                        lcl_3 = prim__mk__ast('Mod', lcl_3)
                                        _slot_local__1 = lcl_3
                                        lcl_3 = (True, _slot_local__1)
                                lcl_2 = lcl_3
                            else:
                                lcl_3 = (_off_3, 'Mod lookahead failed')
                                lcl_3 = prim__cons(lcl_3, prim__nil)
                                lcl_3 = lcl_3
                                lcl_3 = (False, lcl_3)
                                lcl_2 = lcl_3
                        else:
                            lcl_2 = (_off_3, 'Mod got EOF')
                            lcl_2 = prim__cons(lcl_2, prim__nil)
                            lcl_2 = lcl_2
                            lcl_2 = (False, lcl_2)
                        lcl_1 = lcl_2
                lcl_0 = lcl_1
        return lcl_0

    def parse_Num(prim__state, prim__tokens):
        lcl_0 = 2
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
            lcl_0 = (lcl_0, 'number not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = (_slot_0,)
            lcl_0 = prim__mk__ast('Num', lcl_0)
            _slot_local__1 = lcl_0
            lcl_0 = (True, _slot_local__1)
        return lcl_0

    def parse_NumCase(prim__state, prim__tokens):
        lcl_0 = 2
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
            lcl_0 = (lcl_0, 'number not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = (_slot_0,)
            lcl_0 = prim__mk__ast('NumCase', lcl_0)
            _slot_local__1 = lcl_0
            lcl_0 = (True, _slot_local__1)
        return lcl_0

    def parse_Open(prim__state, prim__tokens):
        lcl_0 = 18
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
            lcl_0 = (lcl_0, 'quote open not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = parse_DotId(prim__state, prim__tokens)
            _slot_1_check = lcl_0
            lcl_0 = _slot_1_check[0]
            lcl_0 = (lcl_0 is False)
            if lcl_0:
                lcl_0 = _slot_1_check
            else:
                lcl_1 = _slot_1_check[1]
                lcl_1 = lcl_1
                _slot_1 = lcl_1
                lcl_1 = (_slot_0, _slot_1)
                lcl_1 = prim__mk__ast('Open', lcl_1)
                _slot_local__1 = lcl_1
                lcl_1 = (True, _slot_local__1)
                lcl_0 = lcl_1
        return lcl_0

    def parse_PinCase(prim__state, prim__tokens):
        lcl_0 = 15
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
            lcl_0 = (lcl_0, 'quote ^ not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = parse_Exp(prim__state, prim__tokens)
            _slot_1_check = lcl_0
            lcl_0 = _slot_1_check[0]
            lcl_0 = (lcl_0 is False)
            if lcl_0:
                lcl_0 = _slot_1_check
            else:
                lcl_1 = _slot_1_check[1]
                lcl_1 = lcl_1
                _slot_1 = lcl_1
                lcl_1 = (_slot_0, _slot_1)
                lcl_1 = prim__mk__ast('PinCase', lcl_1)
                _slot_local__1 = lcl_1
                lcl_1 = (True, _slot_local__1)
                lcl_0 = lcl_1
        return lcl_0

    def parse_Recogniser(prim__state, prim__tokens):
        lcl_0 = parse_DotId(prim__state, prim__tokens)
        _slot_0_check = lcl_0
        lcl_0 = _slot_0_check[0]
        lcl_0 = (lcl_0 is False)
        if lcl_0:
            lcl_0 = _slot_0_check
        else:
            lcl_0 = _slot_0_check[1]
            lcl_0 = lcl_0
            _slot_0 = lcl_0
            lcl_0 = prim__tokens.offset
            _off_0 = lcl_0
            lcl_0 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
            if lcl_0:
                lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
                lcl_2 = lcl_2.idint
                if (lcl_2 == 10):
                    _py_local_i = prim__tokens.offset
                    _py_local_t = prim__tokens.array[_py_local_i]
                    prim__tokens.offset = (_py_local_i + 1)
                    lcl_2 = _py_local_t
                    _slot_1 = lcl_2
                    lcl_2 = prim__tokens.offset
                    _off_1 = lcl_2
                    lcl_2 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                    if lcl_2:
                        lcl_3 = prim__tokens.array[(prim__tokens.offset + 0)]
                        lcl_3 = lcl_3.idint
                        if (lcl_3 == 5):
                            lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                            _slot_2_check = lcl_3
                            lcl_3 = _slot_2_check[0]
                            lcl_3 = (lcl_3 is False)
                            if lcl_3:
                                lcl_3 = _slot_2_check
                            else:
                                lcl_3 = _slot_2_check[1]
                                lcl_3 = lcl_3
                                _slot_2 = lcl_3
                                lcl_3 = 11
                                try:
                                    _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                    if (_py_local_tk.idint is lcl_3):
                                        prim__tokens.offset += 1
                                    else:
                                        _py_local_tk = None
                                except IndexError:
                                    _py_local_tk = None
                                lcl_3 = _py_local_tk
                                _slot_3 = lcl_3
                                lcl_3 = (_slot_3 is None)
                                if lcl_3:
                                    lcl_3 = prim__tokens.offset
                                    lcl_3 = (lcl_3, 'quote ) not match')
                                    lcl_3 = prim__cons(lcl_3, prim__nil)
                                    lcl_3 = lcl_3
                                    lcl_3 = (False, lcl_3)
                                else:
                                    lcl_3 = (_slot_1, _slot_2, _slot_3)
                                    _slot_local__1 = lcl_3
                                    lcl_3 = (_slot_0, _slot_local__1)
                                    lcl_3 = prim__mk__ast('Recogniser', lcl_3)
                                    _slot_local__2 = lcl_3
                                    lcl_3 = (True, _slot_local__2)
                            lcl_2 = lcl_3
                        elif (lcl_3 == 15):
                            lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                            _slot_2_check = lcl_3
                            lcl_3 = _slot_2_check[0]
                            lcl_3 = (lcl_3 is False)
                            if lcl_3:
                                lcl_3 = _slot_2_check
                            else:
                                lcl_4 = _slot_2_check[1]
                                lcl_4 = lcl_4
                                _slot_2 = lcl_4
                                lcl_4 = 11
                                try:
                                    _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                    if (_py_local_tk.idint is lcl_4):
                                        prim__tokens.offset += 1
                                    else:
                                        _py_local_tk = None
                                except IndexError:
                                    _py_local_tk = None
                                lcl_4 = _py_local_tk
                                _slot_3 = lcl_4
                                lcl_4 = (_slot_3 is None)
                                if lcl_4:
                                    lcl_4 = prim__tokens.offset
                                    lcl_4 = (lcl_4, 'quote ) not match')
                                    lcl_4 = prim__cons(lcl_4, prim__nil)
                                    lcl_4 = lcl_4
                                    lcl_4 = (False, lcl_4)
                                else:
                                    lcl_4 = (_slot_1, _slot_2, _slot_3)
                                    _slot_local__1 = lcl_4
                                    lcl_4 = (_slot_0, _slot_local__1)
                                    lcl_4 = prim__mk__ast('Recogniser', lcl_4)
                                    _slot_local__2 = lcl_4
                                    lcl_4 = (True, _slot_local__2)
                                lcl_3 = lcl_4
                            lcl_2 = lcl_3
                        elif (lcl_3 == 26):
                            lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                            _slot_2_check = lcl_3
                            lcl_4 = _slot_2_check[0]
                            lcl_3 = (lcl_4 is False)
                            if lcl_3:
                                lcl_3 = _slot_2_check
                            else:
                                lcl_3 = _slot_2_check[1]
                                lcl_3 = lcl_3
                                _slot_2 = lcl_3
                                lcl_3 = 11
                                try:
                                    _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                    if (_py_local_tk.idint is lcl_3):
                                        prim__tokens.offset += 1
                                    else:
                                        _py_local_tk = None
                                except IndexError:
                                    _py_local_tk = None
                                lcl_3 = _py_local_tk
                                _slot_3 = lcl_3
                                lcl_3 = (_slot_3 is None)
                                if lcl_3:
                                    lcl_3 = prim__tokens.offset
                                    lcl_3 = (lcl_3, 'quote ) not match')
                                    lcl_3 = prim__cons(lcl_3, prim__nil)
                                    lcl_3 = lcl_3
                                    lcl_3 = (False, lcl_3)
                                else:
                                    lcl_3 = (_slot_1, _slot_2, _slot_3)
                                    _slot_local__1 = lcl_3
                                    lcl_3 = (_slot_0, _slot_local__1)
                                    lcl_3 = prim__mk__ast('Recogniser', lcl_3)
                                    _slot_local__2 = lcl_3
                                    lcl_3 = (True, _slot_local__2)
                            lcl_2 = lcl_3
                        elif (lcl_3 == 11):
                            _py_local_i = prim__tokens.offset
                            _py_local_t = prim__tokens.array[_py_local_i]
                            prim__tokens.offset = (_py_local_i + 1)
                            lcl_3 = _py_local_t
                            _slot_2 = lcl_3
                            lcl_3 = (_slot_1, _slot_2)
                            _slot_local__1 = lcl_3
                            lcl_3 = (_slot_0, _slot_local__1)
                            lcl_3 = prim__mk__ast('Recogniser', lcl_3)
                            _slot_local__2 = lcl_3
                            lcl_3 = (True, _slot_local__2)
                            lcl_2 = lcl_3
                        elif (lcl_3 == 10):
                            lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                            _slot_2_check = lcl_3
                            lcl_3 = _slot_2_check[0]
                            lcl_3 = (lcl_3 is False)
                            if lcl_3:
                                lcl_3 = _slot_2_check
                            else:
                                lcl_3 = _slot_2_check[1]
                                lcl_3 = lcl_3
                                _slot_2 = lcl_3
                                lcl_3 = 11
                                try:
                                    _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                    if (_py_local_tk.idint is lcl_3):
                                        prim__tokens.offset += 1
                                    else:
                                        _py_local_tk = None
                                except IndexError:
                                    _py_local_tk = None
                                lcl_3 = _py_local_tk
                                _slot_3 = lcl_3
                                lcl_3 = (_slot_3 is None)
                                if lcl_3:
                                    lcl_3 = prim__tokens.offset
                                    lcl_3 = (lcl_3, 'quote ) not match')
                                    lcl_3 = prim__cons(lcl_3, prim__nil)
                                    lcl_3 = lcl_3
                                    lcl_3 = (False, lcl_3)
                                else:
                                    lcl_3 = (_slot_1, _slot_2, _slot_3)
                                    _slot_local__1 = lcl_3
                                    lcl_3 = (_slot_0, _slot_local__1)
                                    lcl_3 = prim__mk__ast('Recogniser', lcl_3)
                                    _slot_local__2 = lcl_3
                                    lcl_3 = (True, _slot_local__2)
                            lcl_2 = lcl_3
                        elif (lcl_3 == 2):
                            lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                            _slot_2_check = lcl_3
                            lcl_3 = _slot_2_check[0]
                            lcl_3 = (lcl_3 is False)
                            if lcl_3:
                                lcl_3 = _slot_2_check
                            else:
                                lcl_4 = _slot_2_check[1]
                                lcl_4 = lcl_4
                                _slot_2 = lcl_4
                                lcl_4 = 11
                                try:
                                    _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                    if (_py_local_tk.idint is lcl_4):
                                        prim__tokens.offset += 1
                                    else:
                                        _py_local_tk = None
                                except IndexError:
                                    _py_local_tk = None
                                lcl_4 = _py_local_tk
                                _slot_3 = lcl_4
                                lcl_4 = (_slot_3 is None)
                                if lcl_4:
                                    lcl_4 = prim__tokens.offset
                                    lcl_4 = (lcl_4, 'quote ) not match')
                                    lcl_4 = prim__cons(lcl_4, prim__nil)
                                    lcl_4 = lcl_4
                                    lcl_4 = (False, lcl_4)
                                else:
                                    lcl_4 = (_slot_1, _slot_2, _slot_3)
                                    _slot_local__1 = lcl_4
                                    lcl_4 = (_slot_0, _slot_local__1)
                                    lcl_4 = prim__mk__ast('Recogniser', lcl_4)
                                    _slot_local__2 = lcl_4
                                    lcl_4 = (True, _slot_local__2)
                                lcl_3 = lcl_4
                            lcl_2 = lcl_3
                        elif (lcl_3 == 4):
                            lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                            _slot_2_check = lcl_3
                            lcl_4 = _slot_2_check[0]
                            lcl_3 = (lcl_4 is False)
                            if lcl_3:
                                lcl_3 = _slot_2_check
                            else:
                                lcl_3 = _slot_2_check[1]
                                lcl_3 = lcl_3
                                _slot_2 = lcl_3
                                lcl_3 = 11
                                try:
                                    _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                    if (_py_local_tk.idint is lcl_3):
                                        prim__tokens.offset += 1
                                    else:
                                        _py_local_tk = None
                                except IndexError:
                                    _py_local_tk = None
                                lcl_3 = _py_local_tk
                                _slot_3 = lcl_3
                                lcl_3 = (_slot_3 is None)
                                if lcl_3:
                                    lcl_3 = prim__tokens.offset
                                    lcl_3 = (lcl_3, 'quote ) not match')
                                    lcl_3 = prim__cons(lcl_3, prim__nil)
                                    lcl_3 = lcl_3
                                    lcl_3 = (False, lcl_3)
                                else:
                                    lcl_3 = (_slot_1, _slot_2, _slot_3)
                                    _slot_local__1 = lcl_3
                                    lcl_3 = (_slot_0, _slot_local__1)
                                    lcl_3 = prim__mk__ast('Recogniser', lcl_3)
                                    _slot_local__2 = lcl_3
                                    lcl_3 = (True, _slot_local__2)
                            lcl_2 = lcl_3
                        else:
                            lcl_3 = (_off_1, 'Recogniser lookahead failed')
                            lcl_3 = prim__cons(lcl_3, prim__nil)
                            lcl_3 = lcl_3
                            lcl_3 = (False, lcl_3)
                            lcl_2 = lcl_3
                    else:
                        lcl_2 = (_off_1, 'Recogniser got EOF')
                        lcl_3 = prim__cons(lcl_2, prim__nil)
                        lcl_2 = lcl_3
                        lcl_2 = (False, lcl_2)
                    lcl_1 = lcl_2
                else:
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('Recogniser', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (True, _slot_local__1)
                    lcl_1 = lcl_2
                lcl_0 = lcl_1
            else:
                lcl_1 = (_off_0, 'Recogniser got EOF')
                lcl_2 = prim__cons(lcl_1, prim__nil)
                lcl_1 = lcl_2
                lcl_1 = (False, lcl_1)
                lcl_0 = lcl_1
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
            lcl_0 = parse_Mod(prim__state, prim__tokens)
            _slot_1_check = lcl_0
            lcl_0 = _slot_1_check[0]
            lcl_0 = (lcl_0 is False)
            if lcl_0:
                lcl_0 = _slot_1_check
            else:
                lcl_1 = _slot_1_check[1]
                lcl_1 = lcl_1
                _slot_1 = lcl_1
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
                    lcl_1 = (_slot_0, _slot_1, _slot_2)
                    lcl_1 = prim__mk__ast('START', lcl_1)
                    _slot_local__1 = lcl_1
                    lcl_1 = (True, _slot_local__1)
                lcl_0 = lcl_1
        return lcl_0

    def parse_Stmt(prim__state, prim__tokens):
        lcl_0 = prim__tokens.offset
        _off_0 = lcl_0
        lcl_0 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
        if lcl_0:
            lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
            lcl_2 = lcl_2.idint
            if (lcl_2 == 18):
                lcl_2 = parse_Open(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_2 = _slot_0_check[1]
                    lcl_2 = lcl_2
                    _slot_0 = lcl_2
                    lcl_2 = (_slot_0,)
                    lcl_2 = prim__mk__ast('Stmt', lcl_2)
                    _slot_local__1 = lcl_2
                    lcl_2 = (True, _slot_local__1)
                lcl_1 = lcl_2
            elif (lcl_2 == 17):
                lcl_2 = parse_Let(prim__state, prim__tokens)
                _slot_0_check = lcl_2
                lcl_2 = _slot_0_check[0]
                lcl_2 = (lcl_2 is False)
                if lcl_2:
                    lcl_2 = _slot_0_check
                else:
                    lcl_3 = _slot_0_check[1]
                    lcl_3 = lcl_3
                    _slot_0 = lcl_3
                    lcl_3 = (_slot_0,)
                    lcl_3 = prim__mk__ast('Stmt', lcl_3)
                    _slot_local__1 = lcl_3
                    lcl_3 = (True, _slot_local__1)
                    lcl_2 = lcl_3
                lcl_1 = lcl_2
            else:
                lcl_2 = (_off_0, 'Stmt lookahead failed')
                lcl_3 = prim__cons(lcl_2, prim__nil)
                lcl_2 = lcl_3
                lcl_2 = (False, lcl_2)
                lcl_1 = lcl_2
            lcl_0 = lcl_1
        else:
            lcl_1 = (_off_0, 'Stmt got EOF')
            lcl_1 = prim__cons(lcl_1, prim__nil)
            lcl_1 = lcl_1
            lcl_1 = (False, lcl_1)
            lcl_0 = lcl_1
        return lcl_0

    def parse_Stmts(prim__state, prim__tokens):
        lcl_0 = parse_Stmt(prim__state, prim__tokens)
        _slot_0_check = lcl_0
        lcl_0 = _slot_0_check[0]
        lcl_0 = (lcl_0 is False)
        if lcl_0:
            lcl_0 = _slot_0_check
        else:
            lcl_0 = _slot_0_check[1]
            lcl_0 = lcl_0
            _slot_0 = lcl_0
            lcl_0 = (_slot_0,)
            lcl_0 = prim__mk__ast('Stmts', lcl_0)
            _slot_local__1 = lcl_0
            lcl_0 = lr_loop_Stmts(_slot_local__1, prim__state, prim__tokens)
            lcl_0 = (True, lcl_0)
        return lcl_0

    def parse_Str(prim__state, prim__tokens):
        lcl_0 = 5
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
            lcl_0 = (lcl_0, 'str not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = (_slot_0,)
            lcl_0 = prim__mk__ast('Str', lcl_0)
            _slot_local__1 = lcl_0
            lcl_0 = (True, _slot_local__1)
        return lcl_0

    def parse_StrCase(prim__state, prim__tokens):
        lcl_0 = 5
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
            lcl_0 = (lcl_0, 'str not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = (_slot_0,)
            lcl_0 = prim__mk__ast('StrCase', lcl_0)
            _slot_local__1 = lcl_0
            lcl_0 = (True, _slot_local__1)
        return lcl_0

    def parse_Tuple(prim__state, prim__tokens):
        lcl_0 = 10
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
            lcl_0 = (lcl_0, 'quote ( not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = prim__tokens.offset
            _off_1 = lcl_0
            lcl_0 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
            if lcl_0:
                lcl_1 = prim__tokens.array[(prim__tokens.offset + 0)]
                lcl_1 = lcl_1.idint
                if (lcl_1 == 5):
                    lcl_1 = parse_Exp(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 7
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
                            lcl_1 = (lcl_1, 'quote , not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = prim__tokens.offset
                            _off_3 = lcl_1
                            lcl_1 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                            if lcl_1:
                                lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
                                lcl_2 = lcl_2.idint
                                if (lcl_2 == 5):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 18):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 28):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 17):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 20):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 24):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 26):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 11):
                                    _py_local_i = prim__tokens.offset
                                    _py_local_t = prim__tokens.array[_py_local_i]
                                    prim__tokens.offset = (_py_local_i + 1)
                                    lcl_2 = _py_local_t
                                    _slot_3 = lcl_2
                                    lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                    lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                    _slot_local__1 = lcl_2
                                    lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 10):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 2):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 4):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                else:
                                    lcl_2 = (_off_3, 'Tuple lookahead failed')
                                    lcl_2 = prim__cons(lcl_2, prim__nil)
                                    lcl_2 = lcl_2
                                    lcl_2 = (False, lcl_2)
                                    lcl_1 = lcl_2
                            else:
                                lcl_1 = (_off_3, 'Tuple got EOF')
                                lcl_1 = prim__cons(lcl_1, prim__nil)
                                lcl_1 = lcl_1
                                lcl_1 = (False, lcl_1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 18):
                    lcl_1 = parse_Exp(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_2 = _slot_1_check[1]
                        lcl_2 = lcl_2
                        _slot_1 = lcl_2
                        lcl_2 = 7
                        try:
                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                            if (_py_local_tk.idint is lcl_2):
                                prim__tokens.offset += 1
                            else:
                                _py_local_tk = None
                        except IndexError:
                            _py_local_tk = None
                        lcl_2 = _py_local_tk
                        _slot_2 = lcl_2
                        lcl_2 = (_slot_2 is None)
                        if lcl_2:
                            lcl_2 = prim__tokens.offset
                            lcl_2 = (lcl_2, 'quote , not match')
                            lcl_2 = prim__cons(lcl_2, prim__nil)
                            lcl_2 = lcl_2
                            lcl_2 = (False, lcl_2)
                        else:
                            lcl_2 = prim__tokens.offset
                            _off_3 = lcl_2
                            lcl_2 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                            if lcl_2:
                                lcl_3 = prim__tokens.array[(prim__tokens.offset + 0)]
                                lcl_3 = lcl_3.idint
                                if (lcl_3 == 5):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 18):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 28):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 17):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 20):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 24):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 26):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 11):
                                    _py_local_i = prim__tokens.offset
                                    _py_local_t = prim__tokens.array[_py_local_i]
                                    prim__tokens.offset = (_py_local_i + 1)
                                    lcl_3 = _py_local_t
                                    _slot_3 = lcl_3
                                    lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                    lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                    _slot_local__1 = lcl_3
                                    lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 10):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 2):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 4):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                else:
                                    lcl_3 = (_off_3, 'Tuple lookahead failed')
                                    lcl_3 = prim__cons(lcl_3, prim__nil)
                                    lcl_3 = lcl_3
                                    lcl_3 = (False, lcl_3)
                                    lcl_2 = lcl_3
                            else:
                                lcl_2 = (_off_3, 'Tuple got EOF')
                                lcl_2 = prim__cons(lcl_2, prim__nil)
                                lcl_2 = lcl_2
                                lcl_2 = (False, lcl_2)
                        lcl_1 = lcl_2
                    lcl_0 = lcl_1
                elif (lcl_1 == 28):
                    lcl_1 = parse_Exp(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_2 = _slot_1_check[0]
                    lcl_1 = (lcl_2 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 7
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
                            lcl_1 = (lcl_1, 'quote , not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = prim__tokens.offset
                            _off_3 = lcl_1
                            lcl_1 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                            if lcl_1:
                                lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
                                lcl_2 = lcl_2.idint
                                if (lcl_2 == 5):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 18):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 28):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 17):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 20):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 24):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 26):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 11):
                                    _py_local_i = prim__tokens.offset
                                    _py_local_t = prim__tokens.array[_py_local_i]
                                    prim__tokens.offset = (_py_local_i + 1)
                                    lcl_2 = _py_local_t
                                    _slot_3 = lcl_2
                                    lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                    lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                    _slot_local__1 = lcl_2
                                    lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 10):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 2):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 4):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                else:
                                    lcl_2 = (_off_3, 'Tuple lookahead failed')
                                    lcl_2 = prim__cons(lcl_2, prim__nil)
                                    lcl_2 = lcl_2
                                    lcl_2 = (False, lcl_2)
                                    lcl_1 = lcl_2
                            else:
                                lcl_1 = (_off_3, 'Tuple got EOF')
                                lcl_1 = prim__cons(lcl_1, prim__nil)
                                lcl_1 = lcl_1
                                lcl_1 = (False, lcl_1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 17):
                    lcl_1 = parse_Exp(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_2 = _slot_1_check[1]
                        lcl_2 = lcl_2
                        _slot_1 = lcl_2
                        lcl_2 = 7
                        try:
                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                            if (_py_local_tk.idint is lcl_2):
                                prim__tokens.offset += 1
                            else:
                                _py_local_tk = None
                        except IndexError:
                            _py_local_tk = None
                        lcl_2 = _py_local_tk
                        _slot_2 = lcl_2
                        lcl_2 = (_slot_2 is None)
                        if lcl_2:
                            lcl_2 = prim__tokens.offset
                            lcl_2 = (lcl_2, 'quote , not match')
                            lcl_2 = prim__cons(lcl_2, prim__nil)
                            lcl_2 = lcl_2
                            lcl_2 = (False, lcl_2)
                        else:
                            lcl_2 = prim__tokens.offset
                            _off_3 = lcl_2
                            lcl_2 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                            if lcl_2:
                                lcl_3 = prim__tokens.array[(prim__tokens.offset + 0)]
                                lcl_3 = lcl_3.idint
                                if (lcl_3 == 5):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 18):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 28):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 17):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 20):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 24):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 26):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 11):
                                    _py_local_i = prim__tokens.offset
                                    _py_local_t = prim__tokens.array[_py_local_i]
                                    prim__tokens.offset = (_py_local_i + 1)
                                    lcl_3 = _py_local_t
                                    _slot_3 = lcl_3
                                    lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                    lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                    _slot_local__1 = lcl_3
                                    lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 10):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 2):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 4):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                else:
                                    lcl_3 = (_off_3, 'Tuple lookahead failed')
                                    lcl_3 = prim__cons(lcl_3, prim__nil)
                                    lcl_3 = lcl_3
                                    lcl_3 = (False, lcl_3)
                                    lcl_2 = lcl_3
                            else:
                                lcl_2 = (_off_3, 'Tuple got EOF')
                                lcl_2 = prim__cons(lcl_2, prim__nil)
                                lcl_2 = lcl_2
                                lcl_2 = (False, lcl_2)
                        lcl_1 = lcl_2
                    lcl_0 = lcl_1
                elif (lcl_1 == 20):
                    lcl_1 = parse_Exp(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_2 = _slot_1_check[0]
                    lcl_1 = (lcl_2 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 7
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
                            lcl_1 = (lcl_1, 'quote , not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = prim__tokens.offset
                            _off_3 = lcl_1
                            lcl_1 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                            if lcl_1:
                                lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
                                lcl_2 = lcl_2.idint
                                if (lcl_2 == 5):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 18):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 28):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 17):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 20):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 24):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 26):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 11):
                                    _py_local_i = prim__tokens.offset
                                    _py_local_t = prim__tokens.array[_py_local_i]
                                    prim__tokens.offset = (_py_local_i + 1)
                                    lcl_2 = _py_local_t
                                    _slot_3 = lcl_2
                                    lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                    lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                    _slot_local__1 = lcl_2
                                    lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 10):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 2):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 4):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                else:
                                    lcl_2 = (_off_3, 'Tuple lookahead failed')
                                    lcl_2 = prim__cons(lcl_2, prim__nil)
                                    lcl_2 = lcl_2
                                    lcl_2 = (False, lcl_2)
                                    lcl_1 = lcl_2
                            else:
                                lcl_1 = (_off_3, 'Tuple got EOF')
                                lcl_1 = prim__cons(lcl_1, prim__nil)
                                lcl_1 = lcl_1
                                lcl_1 = (False, lcl_1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 24):
                    lcl_1 = parse_Exp(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_2 = _slot_1_check[1]
                        lcl_2 = lcl_2
                        _slot_1 = lcl_2
                        lcl_2 = 7
                        try:
                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                            if (_py_local_tk.idint is lcl_2):
                                prim__tokens.offset += 1
                            else:
                                _py_local_tk = None
                        except IndexError:
                            _py_local_tk = None
                        lcl_2 = _py_local_tk
                        _slot_2 = lcl_2
                        lcl_2 = (_slot_2 is None)
                        if lcl_2:
                            lcl_2 = prim__tokens.offset
                            lcl_2 = (lcl_2, 'quote , not match')
                            lcl_2 = prim__cons(lcl_2, prim__nil)
                            lcl_2 = lcl_2
                            lcl_2 = (False, lcl_2)
                        else:
                            lcl_2 = prim__tokens.offset
                            _off_3 = lcl_2
                            lcl_2 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                            if lcl_2:
                                lcl_3 = prim__tokens.array[(prim__tokens.offset + 0)]
                                lcl_3 = lcl_3.idint
                                if (lcl_3 == 5):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 18):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 28):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 17):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 20):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 24):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 26):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 11):
                                    _py_local_i = prim__tokens.offset
                                    _py_local_t = prim__tokens.array[_py_local_i]
                                    prim__tokens.offset = (_py_local_i + 1)
                                    lcl_3 = _py_local_t
                                    _slot_3 = lcl_3
                                    lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                    lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                    _slot_local__1 = lcl_3
                                    lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 10):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 2):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 4):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                else:
                                    lcl_3 = (_off_3, 'Tuple lookahead failed')
                                    lcl_3 = prim__cons(lcl_3, prim__nil)
                                    lcl_3 = lcl_3
                                    lcl_3 = (False, lcl_3)
                                    lcl_2 = lcl_3
                            else:
                                lcl_2 = (_off_3, 'Tuple got EOF')
                                lcl_2 = prim__cons(lcl_2, prim__nil)
                                lcl_2 = lcl_2
                                lcl_2 = (False, lcl_2)
                        lcl_1 = lcl_2
                    lcl_0 = lcl_1
                elif (lcl_1 == 26):
                    lcl_1 = parse_Exp(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_2 = _slot_1_check[0]
                    lcl_1 = (lcl_2 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 7
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
                            lcl_1 = (lcl_1, 'quote , not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = prim__tokens.offset
                            _off_3 = lcl_1
                            lcl_1 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                            if lcl_1:
                                lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
                                lcl_2 = lcl_2.idint
                                if (lcl_2 == 5):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 18):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 28):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 17):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 20):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 24):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 26):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 11):
                                    _py_local_i = prim__tokens.offset
                                    _py_local_t = prim__tokens.array[_py_local_i]
                                    prim__tokens.offset = (_py_local_i + 1)
                                    lcl_2 = _py_local_t
                                    _slot_3 = lcl_2
                                    lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                    lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                    _slot_local__1 = lcl_2
                                    lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 10):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 2):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 4):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                else:
                                    lcl_2 = (_off_3, 'Tuple lookahead failed')
                                    lcl_2 = prim__cons(lcl_2, prim__nil)
                                    lcl_2 = lcl_2
                                    lcl_2 = (False, lcl_2)
                                    lcl_1 = lcl_2
                            else:
                                lcl_1 = (_off_3, 'Tuple got EOF')
                                lcl_1 = prim__cons(lcl_1, prim__nil)
                                lcl_1 = lcl_1
                                lcl_1 = (False, lcl_1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 11):
                    _py_local_i = prim__tokens.offset
                    _py_local_t = prim__tokens.array[_py_local_i]
                    prim__tokens.offset = (_py_local_i + 1)
                    lcl_1 = _py_local_t
                    _slot_1 = lcl_1
                    lcl_1 = (_slot_0, _slot_1)
                    lcl_1 = prim__mk__ast('Tuple', lcl_1)
                    _slot_local__1 = lcl_1
                    lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 10):
                    lcl_1 = parse_Exp(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_2 = _slot_1_check[1]
                        lcl_2 = lcl_2
                        _slot_1 = lcl_2
                        lcl_2 = 7
                        try:
                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                            if (_py_local_tk.idint is lcl_2):
                                prim__tokens.offset += 1
                            else:
                                _py_local_tk = None
                        except IndexError:
                            _py_local_tk = None
                        lcl_2 = _py_local_tk
                        _slot_2 = lcl_2
                        lcl_2 = (_slot_2 is None)
                        if lcl_2:
                            lcl_2 = prim__tokens.offset
                            lcl_2 = (lcl_2, 'quote , not match')
                            lcl_2 = prim__cons(lcl_2, prim__nil)
                            lcl_2 = lcl_2
                            lcl_2 = (False, lcl_2)
                        else:
                            lcl_2 = prim__tokens.offset
                            _off_3 = lcl_2
                            lcl_2 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                            if lcl_2:
                                lcl_3 = prim__tokens.array[(prim__tokens.offset + 0)]
                                lcl_3 = lcl_3.idint
                                if (lcl_3 == 5):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 18):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 28):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 17):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 20):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 24):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 26):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 11):
                                    _py_local_i = prim__tokens.offset
                                    _py_local_t = prim__tokens.array[_py_local_i]
                                    prim__tokens.offset = (_py_local_i + 1)
                                    lcl_3 = _py_local_t
                                    _slot_3 = lcl_3
                                    lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                    lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                    _slot_local__1 = lcl_3
                                    lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 10):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 2):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 4):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                else:
                                    lcl_3 = (_off_3, 'Tuple lookahead failed')
                                    lcl_3 = prim__cons(lcl_3, prim__nil)
                                    lcl_3 = lcl_3
                                    lcl_3 = (False, lcl_3)
                                    lcl_2 = lcl_3
                            else:
                                lcl_2 = (_off_3, 'Tuple got EOF')
                                lcl_2 = prim__cons(lcl_2, prim__nil)
                                lcl_2 = lcl_2
                                lcl_2 = (False, lcl_2)
                        lcl_1 = lcl_2
                    lcl_0 = lcl_1
                elif (lcl_1 == 2):
                    lcl_1 = parse_Exp(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_2 = _slot_1_check[0]
                    lcl_1 = (lcl_2 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 7
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
                            lcl_1 = (lcl_1, 'quote , not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = prim__tokens.offset
                            _off_3 = lcl_1
                            lcl_1 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                            if lcl_1:
                                lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
                                lcl_2 = lcl_2.idint
                                if (lcl_2 == 5):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 18):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 28):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 17):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 20):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 24):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 26):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 11):
                                    _py_local_i = prim__tokens.offset
                                    _py_local_t = prim__tokens.array[_py_local_i]
                                    prim__tokens.offset = (_py_local_i + 1)
                                    lcl_2 = _py_local_t
                                    _slot_3 = lcl_2
                                    lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                    lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                    _slot_local__1 = lcl_2
                                    lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 10):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 2):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 4):
                                    lcl_2 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('Tuple', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                else:
                                    lcl_2 = (_off_3, 'Tuple lookahead failed')
                                    lcl_2 = prim__cons(lcl_2, prim__nil)
                                    lcl_2 = lcl_2
                                    lcl_2 = (False, lcl_2)
                                    lcl_1 = lcl_2
                            else:
                                lcl_1 = (_off_3, 'Tuple got EOF')
                                lcl_1 = prim__cons(lcl_1, prim__nil)
                                lcl_1 = lcl_1
                                lcl_1 = (False, lcl_1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 4):
                    lcl_1 = parse_Exp(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_2 = _slot_1_check[1]
                        lcl_2 = lcl_2
                        _slot_1 = lcl_2
                        lcl_2 = 7
                        try:
                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                            if (_py_local_tk.idint is lcl_2):
                                prim__tokens.offset += 1
                            else:
                                _py_local_tk = None
                        except IndexError:
                            _py_local_tk = None
                        lcl_2 = _py_local_tk
                        _slot_2 = lcl_2
                        lcl_2 = (_slot_2 is None)
                        if lcl_2:
                            lcl_2 = prim__tokens.offset
                            lcl_2 = (lcl_2, 'quote , not match')
                            lcl_2 = prim__cons(lcl_2, prim__nil)
                            lcl_2 = lcl_2
                            lcl_2 = (False, lcl_2)
                        else:
                            lcl_2 = prim__tokens.offset
                            _off_3 = lcl_2
                            lcl_2 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                            if lcl_2:
                                lcl_3 = prim__tokens.array[(prim__tokens.offset + 0)]
                                lcl_3 = lcl_3.idint
                                if (lcl_3 == 5):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 18):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 28):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 17):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 20):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 24):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 26):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 11):
                                    _py_local_i = prim__tokens.offset
                                    _py_local_t = prim__tokens.array[_py_local_i]
                                    prim__tokens.offset = (_py_local_i + 1)
                                    lcl_3 = _py_local_t
                                    _slot_3 = lcl_3
                                    lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                    lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                    _slot_local__1 = lcl_3
                                    lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 10):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 2):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 4):
                                    lcl_3 = parse_CommaExps(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('Tuple', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                else:
                                    lcl_3 = (_off_3, 'Tuple lookahead failed')
                                    lcl_3 = prim__cons(lcl_3, prim__nil)
                                    lcl_3 = lcl_3
                                    lcl_3 = (False, lcl_3)
                                    lcl_2 = lcl_3
                            else:
                                lcl_2 = (_off_3, 'Tuple got EOF')
                                lcl_2 = prim__cons(lcl_2, prim__nil)
                                lcl_2 = lcl_2
                                lcl_2 = (False, lcl_2)
                        lcl_1 = lcl_2
                    lcl_0 = lcl_1
                else:
                    lcl_1 = (_off_1, 'Tuple lookahead failed')
                    lcl_2 = prim__cons(lcl_1, prim__nil)
                    lcl_1 = lcl_2
                    lcl_1 = (False, lcl_1)
                    lcl_0 = lcl_1
            else:
                lcl_0 = (_off_1, 'Tuple got EOF')
                lcl_0 = prim__cons(lcl_0, prim__nil)
                lcl_0 = lcl_0
                lcl_0 = (False, lcl_0)
        return lcl_0

    def parse_TupleCase(prim__state, prim__tokens):
        lcl_0 = 10
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
            lcl_0 = (lcl_0, 'quote ( not match')
            lcl_0 = prim__cons(lcl_0, prim__nil)
            lcl_0 = lcl_0
            lcl_0 = (False, lcl_0)
        else:
            lcl_0 = prim__tokens.offset
            _off_1 = lcl_0
            lcl_0 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
            if lcl_0:
                lcl_1 = prim__tokens.array[(prim__tokens.offset + 0)]
                lcl_1 = lcl_1.idint
                if (lcl_1 == 5):
                    lcl_1 = parse_Case(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 7
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
                            lcl_1 = (lcl_1, 'quote , not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = prim__tokens.offset
                            _off_3 = lcl_1
                            lcl_1 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                            if lcl_1:
                                lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
                                lcl_2 = lcl_2.idint
                                if (lcl_2 == 5):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 15):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 26):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 11):
                                    _py_local_i = prim__tokens.offset
                                    _py_local_t = prim__tokens.array[_py_local_i]
                                    prim__tokens.offset = (_py_local_i + 1)
                                    lcl_2 = _py_local_t
                                    _slot_3 = lcl_2
                                    lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                    lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                    _slot_local__1 = lcl_2
                                    lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 10):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 2):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 4):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                else:
                                    lcl_2 = (_off_3, 'TupleCase lookahead failed')
                                    lcl_2 = prim__cons(lcl_2, prim__nil)
                                    lcl_2 = lcl_2
                                    lcl_2 = (False, lcl_2)
                                    lcl_1 = lcl_2
                            else:
                                lcl_1 = (_off_3, 'TupleCase got EOF')
                                lcl_1 = prim__cons(lcl_1, prim__nil)
                                lcl_1 = lcl_1
                                lcl_1 = (False, lcl_1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 15):
                    lcl_1 = parse_Case(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_2 = _slot_1_check[1]
                        lcl_2 = lcl_2
                        _slot_1 = lcl_2
                        lcl_2 = 7
                        try:
                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                            if (_py_local_tk.idint is lcl_2):
                                prim__tokens.offset += 1
                            else:
                                _py_local_tk = None
                        except IndexError:
                            _py_local_tk = None
                        lcl_2 = _py_local_tk
                        _slot_2 = lcl_2
                        lcl_2 = (_slot_2 is None)
                        if lcl_2:
                            lcl_2 = prim__tokens.offset
                            lcl_2 = (lcl_2, 'quote , not match')
                            lcl_2 = prim__cons(lcl_2, prim__nil)
                            lcl_2 = lcl_2
                            lcl_2 = (False, lcl_2)
                        else:
                            lcl_2 = prim__tokens.offset
                            _off_3 = lcl_2
                            lcl_2 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                            if lcl_2:
                                lcl_3 = prim__tokens.array[(prim__tokens.offset + 0)]
                                lcl_3 = lcl_3.idint
                                if (lcl_3 == 5):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 15):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 26):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 11):
                                    _py_local_i = prim__tokens.offset
                                    _py_local_t = prim__tokens.array[_py_local_i]
                                    prim__tokens.offset = (_py_local_i + 1)
                                    lcl_3 = _py_local_t
                                    _slot_3 = lcl_3
                                    lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                    lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                    _slot_local__1 = lcl_3
                                    lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 10):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 2):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 4):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                else:
                                    lcl_3 = (_off_3, 'TupleCase lookahead failed')
                                    lcl_3 = prim__cons(lcl_3, prim__nil)
                                    lcl_3 = lcl_3
                                    lcl_3 = (False, lcl_3)
                                    lcl_2 = lcl_3
                            else:
                                lcl_2 = (_off_3, 'TupleCase got EOF')
                                lcl_2 = prim__cons(lcl_2, prim__nil)
                                lcl_2 = lcl_2
                                lcl_2 = (False, lcl_2)
                        lcl_1 = lcl_2
                    lcl_0 = lcl_1
                elif (lcl_1 == 26):
                    lcl_1 = parse_Case(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_2 = _slot_1_check[0]
                    lcl_1 = (lcl_2 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 7
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
                            lcl_1 = (lcl_1, 'quote , not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = prim__tokens.offset
                            _off_3 = lcl_1
                            lcl_1 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                            if lcl_1:
                                lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
                                lcl_2 = lcl_2.idint
                                if (lcl_2 == 5):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 15):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 26):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 11):
                                    _py_local_i = prim__tokens.offset
                                    _py_local_t = prim__tokens.array[_py_local_i]
                                    prim__tokens.offset = (_py_local_i + 1)
                                    lcl_2 = _py_local_t
                                    _slot_3 = lcl_2
                                    lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                    lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                    _slot_local__1 = lcl_2
                                    lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 10):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 2):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 4):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                else:
                                    lcl_2 = (_off_3, 'TupleCase lookahead failed')
                                    lcl_2 = prim__cons(lcl_2, prim__nil)
                                    lcl_2 = lcl_2
                                    lcl_2 = (False, lcl_2)
                                    lcl_1 = lcl_2
                            else:
                                lcl_1 = (_off_3, 'TupleCase got EOF')
                                lcl_1 = prim__cons(lcl_1, prim__nil)
                                lcl_1 = lcl_1
                                lcl_1 = (False, lcl_1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 11):
                    _py_local_i = prim__tokens.offset
                    _py_local_t = prim__tokens.array[_py_local_i]
                    prim__tokens.offset = (_py_local_i + 1)
                    lcl_1 = _py_local_t
                    _slot_1 = lcl_1
                    lcl_1 = (_slot_0, _slot_1)
                    lcl_1 = prim__mk__ast('TupleCase', lcl_1)
                    _slot_local__1 = lcl_1
                    lcl_1 = (True, _slot_local__1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 10):
                    lcl_1 = parse_Case(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_2 = _slot_1_check[1]
                        lcl_2 = lcl_2
                        _slot_1 = lcl_2
                        lcl_2 = 7
                        try:
                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                            if (_py_local_tk.idint is lcl_2):
                                prim__tokens.offset += 1
                            else:
                                _py_local_tk = None
                        except IndexError:
                            _py_local_tk = None
                        lcl_2 = _py_local_tk
                        _slot_2 = lcl_2
                        lcl_2 = (_slot_2 is None)
                        if lcl_2:
                            lcl_2 = prim__tokens.offset
                            lcl_2 = (lcl_2, 'quote , not match')
                            lcl_2 = prim__cons(lcl_2, prim__nil)
                            lcl_2 = lcl_2
                            lcl_2 = (False, lcl_2)
                        else:
                            lcl_2 = prim__tokens.offset
                            _off_3 = lcl_2
                            lcl_2 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                            if lcl_2:
                                lcl_3 = prim__tokens.array[(prim__tokens.offset + 0)]
                                lcl_3 = lcl_3.idint
                                if (lcl_3 == 5):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 15):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 26):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 11):
                                    _py_local_i = prim__tokens.offset
                                    _py_local_t = prim__tokens.array[_py_local_i]
                                    prim__tokens.offset = (_py_local_i + 1)
                                    lcl_3 = _py_local_t
                                    _slot_3 = lcl_3
                                    lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                    lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                    _slot_local__1 = lcl_3
                                    lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 10):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 2):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 4):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                else:
                                    lcl_3 = (_off_3, 'TupleCase lookahead failed')
                                    lcl_3 = prim__cons(lcl_3, prim__nil)
                                    lcl_3 = lcl_3
                                    lcl_3 = (False, lcl_3)
                                    lcl_2 = lcl_3
                            else:
                                lcl_2 = (_off_3, 'TupleCase got EOF')
                                lcl_2 = prim__cons(lcl_2, prim__nil)
                                lcl_2 = lcl_2
                                lcl_2 = (False, lcl_2)
                        lcl_1 = lcl_2
                    lcl_0 = lcl_1
                elif (lcl_1 == 2):
                    lcl_1 = parse_Case(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_2 = _slot_1_check[0]
                    lcl_1 = (lcl_2 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_1 = _slot_1_check[1]
                        lcl_1 = lcl_1
                        _slot_1 = lcl_1
                        lcl_1 = 7
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
                            lcl_1 = (lcl_1, 'quote , not match')
                            lcl_1 = prim__cons(lcl_1, prim__nil)
                            lcl_1 = lcl_1
                            lcl_1 = (False, lcl_1)
                        else:
                            lcl_1 = prim__tokens.offset
                            _off_3 = lcl_1
                            lcl_1 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                            if lcl_1:
                                lcl_2 = prim__tokens.array[(prim__tokens.offset + 0)]
                                lcl_2 = lcl_2.idint
                                if (lcl_2 == 5):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 15):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 26):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 11):
                                    _py_local_i = prim__tokens.offset
                                    _py_local_t = prim__tokens.array[_py_local_i]
                                    prim__tokens.offset = (_py_local_i + 1)
                                    lcl_2 = _py_local_t
                                    _slot_3 = lcl_2
                                    lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                    lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                    _slot_local__1 = lcl_2
                                    lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 10):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 2):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                elif (lcl_2 == 4):
                                    lcl_2 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_2
                                    lcl_2 = _slot_3_check[0]
                                    lcl_2 = (lcl_2 is False)
                                    if lcl_2:
                                        lcl_2 = _slot_3_check
                                    else:
                                        lcl_2 = _slot_3_check[1]
                                        lcl_2 = lcl_2
                                        _slot_3 = lcl_2
                                        lcl_2 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_2):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_2 = _py_local_tk
                                        _slot_4 = lcl_2
                                        lcl_2 = (_slot_4 is None)
                                        if lcl_2:
                                            lcl_2 = prim__tokens.offset
                                            lcl_2 = (lcl_2, 'quote ) not match')
                                            lcl_2 = prim__cons(lcl_2, prim__nil)
                                            lcl_2 = lcl_2
                                            lcl_2 = (False, lcl_2)
                                        else:
                                            lcl_2 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_2 = prim__mk__ast('TupleCase', lcl_2)
                                            _slot_local__1 = lcl_2
                                            lcl_2 = (True, _slot_local__1)
                                    lcl_1 = lcl_2
                                else:
                                    lcl_2 = (_off_3, 'TupleCase lookahead failed')
                                    lcl_2 = prim__cons(lcl_2, prim__nil)
                                    lcl_2 = lcl_2
                                    lcl_2 = (False, lcl_2)
                                    lcl_1 = lcl_2
                            else:
                                lcl_1 = (_off_3, 'TupleCase got EOF')
                                lcl_1 = prim__cons(lcl_1, prim__nil)
                                lcl_1 = lcl_1
                                lcl_1 = (False, lcl_1)
                    lcl_0 = lcl_1
                elif (lcl_1 == 4):
                    lcl_1 = parse_Case(prim__state, prim__tokens)
                    _slot_1_check = lcl_1
                    lcl_1 = _slot_1_check[0]
                    lcl_1 = (lcl_1 is False)
                    if lcl_1:
                        lcl_1 = _slot_1_check
                    else:
                        lcl_2 = _slot_1_check[1]
                        lcl_2 = lcl_2
                        _slot_1 = lcl_2
                        lcl_2 = 7
                        try:
                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                            if (_py_local_tk.idint is lcl_2):
                                prim__tokens.offset += 1
                            else:
                                _py_local_tk = None
                        except IndexError:
                            _py_local_tk = None
                        lcl_2 = _py_local_tk
                        _slot_2 = lcl_2
                        lcl_2 = (_slot_2 is None)
                        if lcl_2:
                            lcl_2 = prim__tokens.offset
                            lcl_2 = (lcl_2, 'quote , not match')
                            lcl_2 = prim__cons(lcl_2, prim__nil)
                            lcl_2 = lcl_2
                            lcl_2 = (False, lcl_2)
                        else:
                            lcl_2 = prim__tokens.offset
                            _off_3 = lcl_2
                            lcl_2 = (len(prim__tokens.array) > (prim__tokens.offset + 0))
                            if lcl_2:
                                lcl_3 = prim__tokens.array[(prim__tokens.offset + 0)]
                                lcl_3 = lcl_3.idint
                                if (lcl_3 == 5):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 15):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 26):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 11):
                                    _py_local_i = prim__tokens.offset
                                    _py_local_t = prim__tokens.array[_py_local_i]
                                    prim__tokens.offset = (_py_local_i + 1)
                                    lcl_3 = _py_local_t
                                    _slot_3 = lcl_3
                                    lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3)
                                    lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                    _slot_local__1 = lcl_3
                                    lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 10):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 2):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                elif (lcl_3 == 4):
                                    lcl_3 = parse_CommaCases(prim__state, prim__tokens)
                                    _slot_3_check = lcl_3
                                    lcl_3 = _slot_3_check[0]
                                    lcl_3 = (lcl_3 is False)
                                    if lcl_3:
                                        lcl_3 = _slot_3_check
                                    else:
                                        lcl_3 = _slot_3_check[1]
                                        lcl_3 = lcl_3
                                        _slot_3 = lcl_3
                                        lcl_3 = 11
                                        try:
                                            _py_local_tk = prim__tokens.array[prim__tokens.offset]
                                            if (_py_local_tk.idint is lcl_3):
                                                prim__tokens.offset += 1
                                            else:
                                                _py_local_tk = None
                                        except IndexError:
                                            _py_local_tk = None
                                        lcl_3 = _py_local_tk
                                        _slot_4 = lcl_3
                                        lcl_3 = (_slot_4 is None)
                                        if lcl_3:
                                            lcl_3 = prim__tokens.offset
                                            lcl_3 = (lcl_3, 'quote ) not match')
                                            lcl_3 = prim__cons(lcl_3, prim__nil)
                                            lcl_3 = lcl_3
                                            lcl_3 = (False, lcl_3)
                                        else:
                                            lcl_3 = (_slot_0, _slot_1, _slot_2, _slot_3, _slot_4)
                                            lcl_3 = prim__mk__ast('TupleCase', lcl_3)
                                            _slot_local__1 = lcl_3
                                            lcl_3 = (True, _slot_local__1)
                                    lcl_2 = lcl_3
                                else:
                                    lcl_3 = (_off_3, 'TupleCase lookahead failed')
                                    lcl_3 = prim__cons(lcl_3, prim__nil)
                                    lcl_3 = lcl_3
                                    lcl_3 = (False, lcl_3)
                                    lcl_2 = lcl_3
                            else:
                                lcl_2 = (_off_3, 'TupleCase got EOF')
                                lcl_2 = prim__cons(lcl_2, prim__nil)
                                lcl_2 = lcl_2
                                lcl_2 = (False, lcl_2)
                        lcl_1 = lcl_2
                    lcl_0 = lcl_1
                else:
                    lcl_1 = (_off_1, 'TupleCase lookahead failed')
                    lcl_2 = prim__cons(lcl_1, prim__nil)
                    lcl_1 = lcl_2
                    lcl_1 = (False, lcl_1)
                    lcl_0 = lcl_1
            else:
                lcl_0 = (_off_1, 'TupleCase got EOF')
                lcl_0 = prim__cons(lcl_0, prim__nil)
                lcl_0 = lcl_0
                lcl_0 = (False, lcl_0)
        return lcl_0
    return parse_START
