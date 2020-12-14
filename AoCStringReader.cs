using System.IO;
using System.Collections.Generic;

namespace AoC2020
{
    public class AoCStringReader : AoCBase
    {
        protected string[] _lines;

        /// <summary>
        /// A base class implementing a simple reading function. Reads and stores lines
        /// as a string array.
        /// </summary>
        /// <param name="filepath">See AoCBase.</param>
        /// <param name="debugLevel">See AoCBase.</param>
        public AoCStringReader(string filepath, int debugLevel) : base(debugLevel)
        {
            _lines = ReadFile(filepath);
        }

        private string[] ReadFile(string filepath)
        {
            string[] lines = File.ReadAllLines(filepath);
            return lines;
        }
    }
}