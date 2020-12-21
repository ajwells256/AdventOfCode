using System.Collections.Generic;
using System.Linq;

namespace AoC2020
{
    public class Docker : AoCLineReader
    {
        private Dictionary<long, long> _mem;
        private long _maskZero;
        private long _maskOne;
        private string _bankMask;
        public Docker(string filepath, int debugLevel = 0) : base(filepath, debugLevel)
        {
            _mem = new Dictionary<long, long>();
        }

        public long Part1() {
            foreach (string line in _lines) {
                string type = line.Substring(0, 3);
                if (type.Equals("mem"))
                    WriteMaskMem(line);
                else if (type.Equals("mas"))
                    UpdateMask(line);
            }
            return _mem.Aggregate(0L, (acc, next) => acc + next.Value); 
        }

        public long Part2() {
            _mem = new Dictionary<long, long>();
            foreach (string line in _lines) {
                string type = line.Substring(0, 3);
                if (type.Equals("mem"))
                    WriteMemMask(line);
                else if (type.Equals("mas"))
                    UpdateBankMask(line);
            }
            return _mem.Aggregate(0L, (acc, next) => acc + next.Value);
        }

        private void UpdateMask(string line) {
            _maskOne = 0;
            _maskZero = (1L << 36) - 1;
            string[] parse = line.Split(' ');
            string mask = parse[2];
            int i = 0;
            for (i = 0; i < mask.Length; i++) {
                if (mask[i] == '1')
                    _maskOne |= 1L << (35 - i);
                else if (mask[i] == '0')
                    _maskZero &= ~(1L << (35 - i));
            }
        }

        private void UpdateBankMask(string line) {
            string[] parse = line.Split(' ');
            _bankMask = parse[2];
        }

        private void WriteMaskMem(string line) {
            string[] parse = line.Split(' ');
            long value = long.Parse(parse[2]);
            int bank = int.Parse(parse[0].Substring(4, parse[0].Length - 5));
            long write = (_maskOne | value) & _maskZero;
            _mem[bank] = write;
        }

        private void WriteMemMask(string line) {
            string[] parse = line.Split(' ');
            long value = long.Parse(parse[2]);
            long bank = long.Parse(parse[0].Substring(4, parse[0].Length - 5));
            long baseMask = 0L;
            for (int i = 0; i < _bankMask.Length; i++) {
                if (_bankMask[i] == '1' || (_bankMask[i] != 'X' && (((bank >> (35 - i)) & 0x1) == 1)))
                    baseMask |= 1L << (35 - i);
            }
            WriteBanks(0, baseMask, value);
        }

        private void WriteBanks(int idx, long baseMask, long value) {
            int nextFloat = _bankMask.IndexOf('X', idx);
            if (nextFloat == -1) {
                _mem[baseMask] = value;
                return;
            }
            WriteBanks(nextFloat + 1, baseMask, value);
            long newBase = baseMask | (1L << (35 - nextFloat));
            WriteBanks(nextFloat + 1, newBase, value);
        }
    }
}
