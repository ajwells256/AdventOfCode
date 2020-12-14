using System.Diagnostics;
using System.Collections.Generic;
using System.Linq;
using System.IO;

namespace AoC2020
{
    public class BusScheduler : AoCStringReader
    {
        // CRT code adapted from Rosetta Code
        private class ChineseRemainderTheorem
        {
            public long Solve(long[] n, int[] a)
            {
                long prod = n.Aggregate((long)1, (i, j) => i * j);
                long p;
                long sm = 0;
                for (long i = 0; i < n.Length; i++) {
                    p = prod / n[i];
                    sm += a[i] * ModularMultiplicativeInverse(p, n[i]) * p;
                }
                return sm % prod;
            }
    
            private long ModularMultiplicativeInverse(long a, long mod)
            {
                long b = a % mod;
                for (long x = 1; x < mod; x++) {
                    if ((b * x) % mod == 1) {
                        return x;
                    }
                }
                return 1;
            }
        }

        private string[] _busses;
        public BusScheduler(string filepath, int debugLevel = 0) : base(filepath, debugLevel)
        {
            _busses = _lines[1].Split(',');
        }

        public int Part1()
        {
            int t = int.Parse(_lines[0]);
            Dictionary<int, int> busArrivals = new Dictionary<int, int>();
            foreach (string bus in _busses) {
                if (bus.Equals("x"))
                    continue;
                int busid = int.Parse(bus);
                busArrivals[busid] = busid - (t % busid);
            }
            int minId = 0;
            foreach (KeyValuePair<int, int> kv in busArrivals) {
                if (minId == 0 || kv.Value < busArrivals[minId])
                    minId = kv.Key;
            }
            return minId * busArrivals[minId];
        }

        public long Part2() {
            // a dictionary of modulos and the remainders expected,
            // for use in CRT
            Dictionary<long, int> modRems = new Dictionary<long, int>();
            int i;
            for (i = 0; i < _busses.Count(); i++) {
                string bus = _busses[i];
                if (bus.Equals("x"))
                    continue;
                int busid = int.Parse(bus);
                int rem = (busid - i) % busid;
                if (rem < 0)
                    rem += busid; 
                DebugLog($"t = {rem} mod {busid}");
                modRems[busid] = rem;
            }
            ChineseRemainderTheorem crt = new ChineseRemainderTheorem();
            return crt.Solve(modRems.Keys.ToArray(), modRems.Values.ToArray());
        }
    }
}
