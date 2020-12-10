using System;
using System.Collections.Generic;
using System.Linq;

namespace AoC2020
{
    public class XMASReader : AoCLongReader
    {
        public XMASReader(string filepath, int debugLevel = 0) : base(filepath, debugLevel)
        {
        }

        public long Part1(int preamble = 25)
        {
            Queue<long> queue = new Queue<long>(25);
            SetSearcher ss = new SetSearcher();
            int i;
            for (i = 0; i < preamble; i++)
                queue.Enqueue(_lines[i]);
            for ( ; i < _lines.Count; i++) {
                Tuple<long, long> found = ss.HashSetFind(queue.ToList(), _lines[i]);
                if (found == null)
                    break;
                else {
                    queue.Enqueue(_lines[i]);
                    queue.Dequeue();
                }
            }
            return i < _lines.Count ? _lines[i] : -1;
        }

        public long Part2()
        {
            long target = Part1();
            int i;
            Queue<long> queue = new Queue<long>();
            long sum;
            for (i = 0; i < _lines.Count; i++) {
                queue.Enqueue(_lines[i]);
                sum = queue.Aggregate((long)0, (acc, next) => acc + next);
                while (sum > target) {
                    queue.Dequeue();
                    sum = queue.Aggregate((long)0, (acc, next) => acc + next);
                }
                if (sum == target)
                    break;
            }

            return queue.Min() + queue.Max();
        }
    }
}
