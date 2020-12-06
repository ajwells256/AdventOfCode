using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;


namespace AoC2020
{
    public class SetSearcher : AoCBase
    {
        /// <summary>
        /// Sorted list of input values from the Day1 input file
        /// </summary>
        private List<int> _inputValues;

        public SetSearcher(string filepath, int debugLevel = 0) : base(debugLevel) {
            _inputValues = ReadFile(filepath).ToList();
            _inputValues.Sort();
        }

        public int Part1Original() {
            int i, idx = -1;
            for (i = 0; i < _inputValues.Count; i++) {
                DebugLog($"Trying index {i}", 1);
                idx = SpecializedSubsetSum(_inputValues, i, 2020);
                if (idx != -1)
                    break;
            }
            return _inputValues[i] * _inputValues[idx];
        }

        public int Part1() {
            Tuple<int, int> pair = HashSetSubsetSum(_inputValues, 2020);
            int product = -1;
            if (pair != null)
                product = pair.Item1 * pair.Item2;
            return product;
        }

        public int Part2() {
            int i;
            int product = -1;
            for (i = 0; i < _inputValues.Count; i++)
            {
                /* ORIGINAL
                for (j = i+1; j < _inputValues.Count; j++) {
                    // want arr[i] + arr[j] + x = 2020, x > arr[j]
                    // so assume x = arr[j], when that exceeds 2020 we move on
                    if (_inputValues[i] + 2*_inputValues[j] > 2020)
                        break;
                    DebugLog($"Trying indices {i},{j}", 2);
                    idx = SpecializedSubsetSum(_inputValues, j, 2020 - _inputValues[i]);
                    if (idx != -1)
                        break;
                }
                if (idx != -1)
                    break;
                */
                Tuple<int, int> pair = HashSetSubsetSum(_inputValues, 2020 - _inputValues[i], i);
                if (pair != null) {
                    product = pair.Item1 * pair.Item2 * _inputValues[i];
                    break;
                }
            }
            return product;
        }

        /// <summary>
        /// Returns the index of the second value such that the two values sum to 
        /// targetSum. Returns -1 if there was no match.
        /// This runs in logn time, so nlogn because set must be sorted first.
        /// </summary>
        /// <param name="set"> A sorted set of values, of which value is one</param>
        private int SpecializedSubsetSum(List<int> set, int valueIdx, int targetSum) {
            int value = set[valueIdx];
            int upper = set.Count;
            int lower = valueIdx;
            int cursor = valueIdx + ((upper - lower) / 2);
            int matchIdx = -1;

            while(cursor < upper && cursor > lower) {
                DebugLog($"Cursor: {cursor} High: {upper} Low: {lower}");
                int test = set[cursor] + value;
                if (test == targetSum) {
                    matchIdx = cursor;
                    break;
                }
                else if (test < targetSum) {
                    lower = cursor;
                    cursor += (upper - cursor) / 2;
                }
                else {
                    upper = cursor;
                    cursor -= (cursor - lower) / 2;
                }
            }
            return matchIdx;
        }

        /// <summary>
        /// Returns a tuple containing two integers in the specified set which
        /// sum to the target value. Runs in linear time.
        /// </summary>
        /// <param name="set">An unsorted list of integers</param>
        /// <param name="targetSum">The target sum for two items in set</param>
        /// <param name="ignoreIdx">An index to exclude from the list</param>
        /// <returns></returns>
        private Tuple<int, int> HashSetSubsetSum(List<int> set, int targetSum, int ignoreIdx = -1) {
            HashSet<int> seen = new HashSet<int>(set.Count);
            Tuple<int, int> pair = null;
            int i;
            for (i = 0; i < set.Count; i++) {
                if (i == ignoreIdx)
                    continue;
                if (seen.Contains(targetSum - set[i])) {
                    pair = new Tuple<int, int>(set[i], targetSum - set[i]);
                    break;
                }
                seen.Add(set[i]);
            }
            return pair;
        }


        private IEnumerable<int> ReadFile(string filepath) {
            string[] numFile = File.ReadAllLines(filepath);
            IEnumerable<int> intList = numFile.Select(x => int.Parse(x));
            return intList;
        }


    }
}
