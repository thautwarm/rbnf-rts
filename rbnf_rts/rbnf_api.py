from subprocess import check_call


def codegen(filename: str, out: str, inline=True, k: int = 1, traceback: bool = True):
    """
    :param filename: grammar filename
    :param inline: flag to indicate if use grammar inline optimisation.
    :param k: maximum Lookahead count.
    :param out: storing generated python code
    :param traceback: whether to support good error messaging in generated code. With overhead.
    """

    assert k > 0
    cmd = ["rbnf-pgen", "-in", filename, "-k", str(k), "-out", out, "-be", "python"]
    if traceback:
        cmd.append("--trace")
    if not inline:
        cmd.append("--noinline")
    check_call(cmd)
