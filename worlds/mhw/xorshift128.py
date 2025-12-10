# Python implementation of Troschuetz.Random.Generators which is used by the randomizer mod
import struct

MASK64 = 0xFFFFFFFFFFFFFFFF
seedX = (521288629 << 32) & MASK64
seedY = 362436069 & MASK64
class XorShift128Generator:
    def __init__(self, seed):
        seed = seed & MASK64
        self.seed = seed
        self.x = (seedX + seed) & MASK64
        self.y = (seedY * ((seed << 32) & MASK64)) & MASK64
        # Discard first result
        self.next_double()

    def next(self, max_value):
        value = self.next_double() * max_value
        return int(value)

    def next_double(self):
        tx = self.x
        ty = self.y
        self.x = ty
        tx ^= (tx << 23) & MASK64
        tx ^= (tx >> 17) & MASK64
        tx ^= ty ^ ((ty >> 26) & MASK64)
        self.y = tx
        return self.to_double((tx + ty) & MASK64)

    @staticmethod
    def to_double(value):
        value = ((value >> 12) | 0x3FF0000000000000) & MASK64
        as_double = struct.unpack('>d', struct.pack('>Q', value))[0]
        return as_double - 1.0