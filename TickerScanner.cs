using System.Linq;
using System.Collections.Generic;
using System;
using System.Text.RegularExpressions;

namespace AoC2020
{
    public class TicketScanner : AoCLineReader
    {
        private List<Tuple<int,int,int>> _ranges;
        private List<string> _fields;
        private List<int[]> _nearby;
        private int[] _ticket;
        public TicketScanner(string filepath, int debugLevel = 0) : base(filepath, debugLevel)
        {
        }

        public int Part1() {
            ParseRanges();
            _nearby = new List<int[]>();
            int incorrectSum = 0;
            bool nearbyTickets = false;
            foreach (string line in _lines) {
                if (line.Contains("nearby")) {
                    nearbyTickets = true;
                } else if (nearbyTickets) {
                    int[] values = line
                        .Split(',')
                        .Select(x => int.Parse(x))
                        .ToArray();
                    bool valid = true;
                    foreach (int val in values) {
                        if (!ValidValue(val)) {
                            incorrectSum += val;
                            valid = false;
                        }
                    }
                    if (valid)
                        _nearby.Add(values); // for later use
                }
            }
            return incorrectSum;
        }

        public int Part2() {
            Dictionary<int, HashSet<int>> possibilities = new Dictionary<int, HashSet<int>>();
            for (int i = 0; i < _fields.Count; i++) {
                possibilities.Add(i, new HashSet<int>());
                for (int j = 0; j < _fields.Count; j++) {
                    possibilities[i].Add(j);
                }
            }

            foreach (int[] ticket in _nearby) {
                for (int i = 0; i < _fields.Count; i++) {
                    for (int j = 0; j < _fields.Count; j++) {
                        if (!ValidValue(ticket[i], j))
                            possibilities[i].Remove(j);
                    }
                }
            }

            Dictionary<string, int> fieldMap = new Dictionary<string, int>();
            for (int j = 0; j < _fields.Count && fieldMap.Count < _fields.Count; j++) {
                for (int i = 0; i < _fields.Count && fieldMap.Count < _fields.Count; i++) {
                    if (possibilities[i].Count == 1) {
                        fieldMap[_fields[possibilities[i].First()]] = i;
                        foreach (int iprime in possibilities.Keys) {
                            possibilities[iprime].Remove(j);
                        }
                    }
                }
            }
            

            int sum = 0;
            foreach (string field in _fields) {
                if (field.Contains("destination")) {
                    sum += _ticket[fieldMap[field]];
                }
            }
            return sum;
        }

        public long Part2v2() {
            List<HashSet<string>> candidates = new List<HashSet<string>>(_fields.Count);
            for (int i = 0; i < _fields.Count; i++)
                candidates.Add(new HashSet<string>());

            for (int k = 0; k < _fields.Count; k++) {
                for (int v = 0; v < _fields.Count; v++) {
                    IEnumerable<int> vals = _nearby.Select(x => x[v]);
                    if (vals.All(x => ValidValue(x, k))) {
                        candidates[v].Add(_fields[k]);
                    }
                }
            }

            int maxCount = -1;
            while (maxCount > 1 || maxCount < 0) {
                maxCount = 0;
                for (int k = 0; k < _fields.Count; k++) {
                    if (candidates[k].Count == 1) {
                        for (int k2 = 0; k2 < _fields.Count; k2++) {
                            if (k2 != k)
                                candidates[k2].Remove(candidates[k].First());
                        }
                    }
                    else if (candidates[k].Count > maxCount)
                        maxCount = candidates[k].Count;
                }
            }

            long prod = 1;
            for (int i = 0; i < _fields.Count; i++) {
                if (candidates[i].First().Contains("departure"))
                    prod *= _ticket[i];
            }
            return prod;
        }

        private bool ValidValue(int x, int? fieldLimit = null) {
            foreach (Tuple<int, int, int> range in _ranges) {
                if (range.Item1 <= x && x <= range.Item2
                    && (fieldLimit == null || fieldLimit == range.Item3))
                    return true;
            }
            return false;
        }

        private void ParseRanges() {
            // start, end, field index
            _fields = new List<string>();
            _ranges = new List<Tuple<int, int, int>>();
            string pattern = @"\d+-\d+";
            Regex re = new Regex(pattern);
            int field = 0;
            bool myTicket = false;
            foreach (string line in _lines) {
                MatchCollection ms = re.Matches(line);
                if (ms.Count == 0) {
                    if (line.Contains("your"))
                        myTicket = true;
                    else if (myTicket) {
                        _ticket = line
                            .Split(',')
                            .Select(x => int.Parse(x))
                            .ToArray();
                        break;
                    }
                    continue;
                }
                string fieldTitle = line.Split(':')[0];
                _fields.Add(fieldTitle);
                foreach (Match m in ms) {
                    int[] vals = m.Value
                        .Split('-')
                        .Select(x => int.Parse(x))
                        .ToArray();
                    if (vals[0] > vals[1])
                        throw new NotSupportedException($"Backwards range detected! {m.Value}");
                    _ranges.Add(new Tuple<int, int, int>(vals[0], vals[1], field));
                }
                field++;
            }
        }
    }
}
