using System.Collections.Generic;

namespace AoC2020
{
    public class MemoryGame : AoCBase
    {
        public MemoryGame(int debugLevel = 0) : base(debugLevel)
        {
        }

        public int PlayGame(List<int> startingNumbers, int target) {
            Dictionary<int, int> memory = new Dictionary<int, int>();
            int t = 0;
            int lastNum = 0;
            foreach (int num in startingNumbers) {
                t++;
                memory[num] = t;
                lastNum = num;
            }

            // We add the number to memory after checking for the previous
            // mention of it; so the last of the starting values shouldn't
            // be in memory
            memory.Remove(lastNum);
            
            for ( ; t < target; t++) {
                if (!memory.ContainsKey(lastNum)) {
                    memory[lastNum] = t;
                    lastNum = 0;
                } else {
                    int nextLast = t - memory[lastNum];
                    memory[lastNum] = t;
                    lastNum = nextLast;
                }
            }
            return lastNum;
        }
    }
}
