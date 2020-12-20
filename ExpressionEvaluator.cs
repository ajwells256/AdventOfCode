using System.Linq;
using System.Collections.Generic;
using System;
using System.Text.RegularExpressions;

namespace AoC2020
{
    public class ExpressionEvaluator : AoCLineReader
    {
        public ExpressionEvaluator(string filepath, int debugLevel = 0) : base(filepath, debugLevel)
        {
        }

        public long Part1()
        {
            long sum = 0;
            foreach (string line in _lines) {
                long i = EvaluateLine(line);
                sum += i;
                DebugLog(i);
            }
            return sum;
        }

        public int Part2()
        {
            return 0;
        }

        private long EvaluateLine(string line) {
            long value = 0;
            int op = 0; // 0: set, 1: +, 2: *
            for (int i = 0; i < line.Length; i++) {
                switch(line[i]) {
                    case ' ':
                        break;
                    case '+':
                        op = 1;
                        break;
                    case '*':
                        op = 2;
                        break;
                    case '(':
                        if (op == 1)
                            value += EvaluateLine(line.Substring(i+1));
                        else if (op == 2)
                            value *= EvaluateLine(line.Substring(i + 1));
                        else
                            value = EvaluateLine(line.Substring(i + 1));
                        i = FindCloseParen(line, i+1);
                        break;
                    case ')':
                        return value;
                    default:
                        if (op == 1)
                            value += int.Parse(line[i].ToString());
                        else if (op == 2)
                            value *= int.Parse(line[i].ToString());
                        else
                            value = int.Parse(line[i].ToString());
                        break;
                }
            }
            return value;
        }

        private int FindCloseParen(string line, int idx) {
            int sema = 1;
            for (int i = idx; i < line.Length; i++) {
                if (line[i] == ')')
                    sema--;
                else if (line[i] == '(')
                    sema++;
                if (sema == 0)
                    return i;
            }
            return -1;
        }
    }
}