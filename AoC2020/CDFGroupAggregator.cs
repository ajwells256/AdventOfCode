using System.Collections.Generic;
using System.Linq;

namespace AoC2020
{
    public class CDFGroupAggregator : AoCLineReader
    {
        public CDFGroupAggregator(string filepath, int debugLevel = 0) : base(filepath, debugLevel)
        {
        }

        public int Part1()
        {
            int sum = 0;
            HashSet<char> groupSet = new HashSet<char>(26);
            foreach (string line in _lines) {
                DebugLog(line, 2);
                if (line.Equals("")) {
                    sum += groupSet.Count; 
                    groupSet = new HashSet<char>(26);
                    continue;
                }
                groupSet.UnionWith(line.ToHashSet<char>());
            }
            return sum;
        }

        public int Part2()
        {
            int sum = 0;
            HashSet<char> groupSet = new HashSet<char>("abcdefghijklmnopqrstuvwxyz".ToList());
            foreach (string line in _lines)
            {
                DebugLog(line, 2);
                if (line.Equals(""))
                {
                    sum += groupSet.Count;
                    groupSet = new HashSet<char>("abcdefghijklmnopqrstuvwxyz".ToList());
                    continue;
                }
                groupSet.IntersectWith(line.ToHashSet<char>());
            }
            return sum;
        }
    }
}
