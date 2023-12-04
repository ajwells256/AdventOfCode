using System.Collections.Generic;
using System.Linq;

namespace AoC2020
{
    public class JoltChainer : AoCIntReader
    {
        public JoltChainer(string filepath, int debugLevel = 0) : base(filepath, debugLevel)
        {
        }

        public int Part1()
        {
            _lines.Add(0); // add the socket
            _lines.Add(_lines.Max()+3); // add the machine
            _lines.Sort();
            Dictionary<int, int> diffs = new Dictionary<int, int>();
            int i;
            // prepare the dictionary, only 1,2,3 are allowed
            for (i = 1; i < 4; i++)
                diffs.Add(i, 0); 
            for (i = 0; i < _lines.Count-1; i++)
                diffs[_lines[i + 1] - _lines[i]]++;
            return diffs[1] * diffs[3];
        }

        public long Part2()
        {
            // part 1 must be called first
            // _lines is assumed to have socket, machine added and be sorted
            Dictionary<int, long> memo = new Dictionary<int, long>();
            return GetPossibilities(memo, 0);
        }

        /// <summary>
        /// Count the number of possible valid selections of adapters from index idx
        /// which result in reaching the machine (end of the list)
        /// </summary>
        /// <param name="memo">A memo dictionary, saving results from paths that have already
        /// been followed</param>
        /// <param name="idx">The index specifying the starting point</param>
        /// <returns>The count of possibilities</returns>
        private long GetPossibilities(Dictionary<int, long> memo, int idx) {
            if (memo.ContainsKey(idx)) {
                DebugLog($"Cache hit at idx {idx}", 2);
                return memo.GetValueOrDefault(idx);
            } else if (idx == _lines.Count-1) {
                return 1;
            }

            int current = _lines[idx];
            long possibilities = 0;
            for (int i = 1; i < 4 && idx + i < _lines.Count; i++) {
                // Under the assumption that there is a valid arrangement using each adapter,
                // adjacent adapters must be at least 1 jolt rating off, so there are
                // at most 3 valid subsequent choices for the next adapter
                if (_lines[idx + i] - current < 4) {
                    possibilities += GetPossibilities(memo, idx + i);
                } else {
                    break;
                }
            }

            memo.Add(idx, possibilities);
            return possibilities;
        }
    }
}
