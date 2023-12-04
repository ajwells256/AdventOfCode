using System.IO;
using System.Collections.Generic;

namespace AoC2020
{
    public class AoCLineReader : AoCBase
    {
        protected IEnumerable<string> _lines;

        /// <summary>
        /// A base class implementing a simple reading function. Reads and stores lines
        /// as an IEnumerable string.
        /// </summary>
        /// <param name="filepath">See AoCBase.</param>
        /// <param name="debugLevel">See AoCBase.</param>
        public AoCLineReader(string filepath, int debugLevel) : base(debugLevel)
        {
            _lines = ReadFile(filepath);
        }

        private IEnumerable<string> ReadFile(string filepath)
        {
            string[] lines = File.ReadAllLines(filepath);
            return lines;
        }
    }
}