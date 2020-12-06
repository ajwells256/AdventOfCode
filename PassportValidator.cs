using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace AoC2020
{
    public class PassportValidator : AoCLineReader
    {
        public PassportValidator(string filepath, int debugLevel = 0) : base(filepath, debugLevel)
        {
        }

        public int Part1() {
            return Part1Helper((x) => true);
        }

        private int Part1Helper(Func<string, bool> predicate)
        {
            int count = 0;
            HashSet<string> fields = GetFieldSet();
            foreach (string line in _lines) {
                if (line.Equals("\n") || line.Equals("")) {
                    if (fields.Count == 0) {
                        count++;
                    }
                    fields = GetFieldSet();
                    continue;
                }
                string[] pairs = line.Split(' ');
                foreach (string pair in pairs) {
                    if (predicate(pair))
                        fields.Remove(pair.Substring(0,3));
                }
            }
            return count;
        }

        private HashSet<string> GetFieldSet() {
            return new HashSet<string>(
                    new string[] {
                        "byr",
                        "iyr",
                        "eyr",
                        "hgt",
                        "hcl",
                        "ecl",
                        "pid"
                    }
                );
        }

        public int Part2()
        {
            return Part1Helper(Verifier);
        }

        /// <summary>
        /// Verifies a key:value pair based on the rule set specified.
        /// </summary>
        /// <param name="pair">A key value pair in 'key:value' format.</param>
        /// <returns>Whether the value met the criteria.</returns>
        private bool Verifier(string pair) {
            string[] keyVal = pair.Split(':');
            bool accept = false;
            switch (keyVal[0]) {
                case "byr":
                    if (Regex.IsMatch(keyVal[1], @"^\d{4}$")) {
                        int val = int.Parse(keyVal[1]);
                        if (val <= 2002 && val >= 1920) {
                            DebugLog(val);
                            accept = true;
                        }
                    }
                    break;
                case "iyr":
                    if (Regex.IsMatch(keyVal[1], @"^\d{4}$"))
                    {
                        int val = int.Parse(keyVal[1]);
                        if (val <= 2020 && val >= 2010)
                            accept = true;
                    }
                    break;
                case "eyr":
                    if (Regex.IsMatch(keyVal[1], @"^\d{4}$"))
                    {
                        int val = int.Parse(keyVal[1]);
                        if (val <= 2030 && val >= 2020)
                            accept = true;
                    }
                    break;
                case "hgt":
                    if (Regex.IsMatch(keyVal[1], @"^\d+(in|cm)$"))
                    {
                        int val = int.Parse(keyVal[1].Substring(0, keyVal[1].Length-2));
                        if (keyVal[1].IndexOf('i') == -1) { // cm
                            if (val <= 193 && val >= 150)
                                accept = true;
                        } else { // in
                            if (val <= 76 && val >= 59)
                                accept = true;
                        }
                    }
                    break;
                case "hcl":
                    if (Regex.IsMatch(keyVal[1], @"^#[0-9a-f]{6}$"))
                    {
                        accept = true;
                    }
                    break;
                case "ecl":
                    accept = new List<string>() {
                        "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
                    }.Contains(keyVal[1]);
                    break;
                case "pid":
                    if (Regex.IsMatch(keyVal[1], @"^\d{9}$"))
                    {
                        accept = true;
                    }
                    break;
            }
            if (!accept)
                DebugLog($"Rejected {pair}", 2);
            return accept;
        }
    }
}
