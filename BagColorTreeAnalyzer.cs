using System.Text.RegularExpressions;
using System.Collections.Generic;
using System.Linq;

namespace AoC2020
{
    public class BagColorTreeAnalyzer : AoCLineReader
    {
        private class Bag {
            public Dictionary<string, int> Contains;

            public List<string> Parents;

            public Bag(Dictionary<string, int> contains) {
                Contains = contains;
                Parents = new List<string>();
            }
        }

        private Dictionary<string, Bag> _bagGraph;

        public BagColorTreeAnalyzer(string filepath, int debugLevel = 0) : base(filepath, debugLevel)
        {
            _bagGraph = new Dictionary<string, Bag>();
            ConstructGraph();
        }

        public int Part1()
        {
            Queue<string> queue = new Queue<string>();
            HashSet<string> seen = new HashSet<string>();
            queue.Enqueue("shiny gold");
            seen.Add("shiny gold");
            while (queue.Count > 0) {
                string color = queue.Dequeue();
                foreach (string line in _lines) {
                    if (Regex.IsMatch(line, $@"\d {color}")) {
                        string newcolor = line.Substring(0, line.IndexOf("bags"));
                        if (!seen.Contains(newcolor)) {
                            seen.Add(newcolor);
                            queue.Enqueue(newcolor);
                        }
                    }
                }
            }
            return seen.Count - 1;
        }

        public int Part2()
        {
            return GetCountFor("shiny gold") - 1; // discount the shiny gold bag
        }

        /// <summary>
        /// Gets the number of bags contained by (and including) a bag of specified color.
        /// </summary>
        /// <param name="color">Color of the bag to be analyzed.</param>
        private int GetCountFor(string color) {
            int sum = 1; // base case, this is a bag
            Bag bagColor;
            if (_bagGraph.TryGetValue(color, out bagColor)) {
                // inductive case, this bag contains these bags in these quantities
                foreach (var keyValuePair in bagColor.Contains)
                    sum += keyValuePair.Value * GetCountFor(keyValuePair.Key);
            }
            DebugLog($"{color} contains {sum} bags");
            return sum;
        }

        /// <summary>
        /// Constructs the graph of relations between bag colors
        /// </summary>
        private void ConstructGraph() {
            foreach (string line in _lines) {
                string color = line.Substring(0, line.IndexOf("bags")-1);
                var containsStrings = Regex.Matches(line, @"\d+[a-z\s]*bag");
                Dictionary<string, int> contains = new Dictionary<string, int>();
                foreach (Match match in containsStrings) {
                    int spaceIdx = match.Value.IndexOf(' ');
                    int count = int.Parse(match.Value.Substring(0, spaceIdx));
                    string name = match.Value.Substring(spaceIdx+1, match.Value.Length - 5 - spaceIdx);
                    DebugLog($"{name}:{count}", 2);
                    contains.Add(name, count);
                }
                _bagGraph.Add(color, new Bag(contains));
            }
        }
    }
}
