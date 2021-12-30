
from math import prod

x = open("inputs/d16input.txt")
y = x.readlines()
input = [z.rstrip("\n") for z in y]

def HexToBits(c):
    bits = ""
    if (c == "0"):
        bits = "0000"
    elif (c == "1"):
        bits = "0001"
    elif (c == "2"):
        bits = "0010"
    elif (c == "3"):
        bits = "0011"
    elif (c == "4"):
        bits = "0100"
    elif (c == "5"):
        bits = "0101"
    elif (c == "6"):
        bits = "0110"
    elif (c == "7"):
        bits = "0111"
    elif (c == "8"):
        bits = "1000"
    elif (c == "9"):
        bits = "1001"
    elif (c == "A"):
        bits = "1010"
    elif (c == "B"):
        bits = "1011"
    elif (c == "C"):
        bits = "1100"
    elif (c == "D"):
        bits = "1101"
    elif (c == "E"):
        bits = "1110"
    elif (c == "F"):
        bits = "1111"
    return bits

def HexStringToBitString(hex):
    bitstring = ""
    for c in hex:
        bitstring += HexToBits(c)
    return bitstring

def BitsToInt(bits: str):
    exp = len(bits)-1
    total = 0
    for b in bits:
        total += 2**(exp) if b == '1' else 0
        exp -= 1
    return total

class packet:
    def __literal__(self, bitstring):
        self.packets = []
        cursor = 6
        intBuilder = bitstring[cursor+1:cursor+5]
        while (bitstring[cursor] == '1'):
            cursor += 5
            intBuilder += bitstring[cursor+1:cursor+5]
        self.literal = BitsToInt(intBuilder)
        return cursor+5

    def __operator__(self, bitstring):
        cursor = 6
        self.packets = []
        bitsConsumed = 0
        if bitstring[cursor] == '0':
            bitModeLength = 15
            cursor += 1
            bits = BitsToInt(bitstring[cursor:cursor+bitModeLength])
            cursor += bitModeLength
            subPacketsBitstring = bitstring[cursor:cursor+bits]
            bitsConsumed = cursor + bits
            self.packets.append(packet(subPacketsBitstring))
            cursor = self.packets[-1].bits_consumed
            while(cursor < bits):
                newPacket = packet(subPacketsBitstring[cursor:])
                if newPacket.valid:
                    cursor += newPacket.bits_consumed
                    self.packets.append(newPacket)
                else:
                    break
        else:
            packetModeLength = 11
            cursor += 1
            packets = BitsToInt(bitstring[cursor:cursor+packetModeLength])
            cursor += packetModeLength
            subPacketsBitstring = bitstring[cursor:]
            self.packets = []
            subCursor = 0
            for i in range(packets):
                newPacket = packet(subPacketsBitstring[subCursor:])
                subCursor += newPacket.bits_consumed
                self.packets.append(newPacket)
            # might need to process padding
            bitsConsumed = cursor+subCursor
        return bitsConsumed

    def __init__(self, bitstring):
        if (len(bitstring) < 7):
            self.valid = False
        else:
            self.valid = True
            self.version = BitsToInt(bitstring[:3])
            self.id = BitsToInt(bitstring[3:6])
            
            if (self.id == 4):
                self.bits_consumed = self.__literal__(bitstring)
            else:
                self.bits_consumed = self.__operator__(bitstring)

    def evaluate(self):
        result = 0
        if self.id == 0:
            result = sum([p.evaluate() for p in self.packets])
        elif self.id == 1:
            result = prod([p.evaluate() for p in self.packets])
        elif self.id == 2:
            result = min([p.evaluate() for p in self.packets])
        elif self.id == 3:
            result = max([p.evaluate() for p in self.packets])
        elif self.id == 4:
            result = self.literal
        elif self.id == 5:
            assert(len(self.packets) == 2)
            result = 1 if self.packets[0].evaluate() > self.packets[1].evaluate() else 0
        elif self.id == 6:
            assert(len(self.packets) == 2)
            result = 1 if self.packets[0].evaluate() < self.packets[1].evaluate() else 0
        elif self.id == 7:
            assert(len(self.packets) == 2)
            result = 1 if self.packets[0].evaluate() == self.packets[1].evaluate() else 0
        return result


def packetTraverse(parent, accessor):
    result = [accessor(parent)]
    for p in parent.packets:
        result += packetTraverse(p, accessor)
    return result

root = packet(HexStringToBitString(input[0]))

print(sum(packetTraverse(root, lambda p: p.version)))
print(root.evaluate())


