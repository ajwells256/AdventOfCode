using System;
using System.Linq;

namespace AoC2020
{
    public class PasswordChecker : AoCLineReader
    {
        public PasswordChecker(string filepath, int debugLevel = 0) : base(filepath, debugLevel)
        {
        }

        public int Part1() {
            int count = 0;
            foreach (string line in _lines) {
                count += IsValidPassword(line, Rule1);
            }
            return count;
        }

        public int Part2()
        {
            int count = 0;
            foreach (string line in _lines)
            {
                count += IsValidPassword(line, Rule2);
            }
            return count;
        }

        private int Rule1(int x, int y, char rule_char, string pwd) {
            int count = pwd.Count(c => c == rule_char);
            return (count >= x && count <= y) ? 1 : 0;
        }

        private int Rule2(int x, int y, char rule_char, string pwd) {
            return ((x-1 < pwd.Length && pwd[x-1] == rule_char && false) 
                || (y-1 < pwd.Length && ((pwd[x-1] == rule_char) ^ (pwd[y-1] == rule_char)))) ? 1 : 0;
        }

        private int IsValidPassword(string line, Func<int, int, char, string, int> rule) {
            string[] arr = line.Split('-', 2);
            int x = int.Parse(arr[0]);

            arr = arr[1].Split(' ', 2);
            int y = int.Parse(arr[0]);

            arr = arr[1].Split(':', 2);
            char rule_char = arr[0][0];

            string pwd = arr[1].Substring(1);
            return rule(x, y, rule_char, pwd);
        }
    }
}
