from utils.string import bwt, rle
import utils.io.input as inp
import utils.io.output as out

alph = inp.input_alph()

if alph is None:
    alph = 'abcdefghijklmnopqrstuvwxyz'

s = inp.input_str()
# s_bwt = bwt.bwt(s, alph)
# s_mod = rle.rle(s_bwt)
s_mod = rle.rle(s)      # TODO: make it work with bwt
out.print_res(s_mod)
