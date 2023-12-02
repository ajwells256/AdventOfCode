using System.IO;
using System.Collections.Generic;
using System.Linq;

namespace AoC2020
{
    public class AoCIntReader : AoCBase
    {
        protected List<int> _lines;

        /// <summary>
        /// A base class implementing a simple reading function. Reads and stores lines
        /// as an IEnumerable string.
        /// </summary>
        /// <param name="filepath">See AoCBase.</param>
        /// <param name="debugLevel">See AoCBase.</param>
        public AoCIntReader(string filepath, int debugLevel) : base(debugLevel)
        {
            _lines = ReadFile(filepath);
        }

        private List<int> ReadFile(string filepath)
        {
            string[] lines = File.ReadAllLines(filepath);
            return lines.Select(x => int.Parse(x)).ToList();
        }
    }
}