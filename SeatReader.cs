using System;
using System.Collections.Generic;
using System.Linq;

namespace AoC2020
{
    public class SeatReader : AoCLineReader
    {
        public SeatReader(string filepath, int debugLevel = 0) : base(filepath, debugLevel)
        {
        }

        public int Part1()
        {
            int max = 0;
            foreach (string seat in _lines) 
                max = Math.Max(max, GetSeatId(seat));
            return max;
        }

        public int Part2()
        {
            // return FindMissing_Bitmap();
            return FindMissing_Sum();
        }

        /// <summary>
        /// Constructs a bitmap out of populated fields (not really, but memory isn't a concern).
        /// Then searches linearly for the first empty seat with populated seats on either side.
        /// </summary>
        /// <returns>The first seatId matching the criteria.</returns>
        private int FindMissing_Bitmap() {
            int[] bitmap = new int[1024];
            foreach (string seat in _lines)
                bitmap[GetSeatId(seat)] = 1;
            int seatid = 0;
            for (int i = 1; i < 1023; i++)
            {
                if (bitmap[i] == 0 && bitmap[i - 1] == 1 && bitmap[i + 1] == 1)
                {
                    seatid = i;
                    break;
                }
            }
            return seatid;
        }

        /// <summary>
        /// Finds the missing seatId by determining the amount by which the sum of seatIds
        /// falls short of the expected sum. Currently not working for unknown reasons.
        /// </summary>
        /// <returns></returns>
        private int FindMissing_Sum() {
            IEnumerable<int> seats = _lines.Select(s => GetSeatId(s));
            int min = seats.Min();
            int max = seats.Max();
            int actualSum = seats.Sum();
            int rangeSum = (max - min) * (max + min) / 2; // sum of all ints min - max
            DebugLog($"Got {seats.Count()} seats, minimum {min} maximum {max}. Expected sum {rangeSum} actual sum {actualSum}");
            return rangeSum - actualSum;
        }

        /// <summary>
        /// Parses the seat code into a binary description of the seat id.
        /// Note that row * 8 + column = row << 3 + column where column is only 3 bits
        /// so the column can just be written directly into the lower three bits of row.
        /// </summary>
        /// <param name="seatCode"></param>
        /// <returns>The seat id for the given seat code</returns>
        private int GetSeatId(string seatCode) {
            int seatId = 0;
            int x;
            int bits = seatCode.Length;
            for (x = 0; x < bits; x++) {
                if (seatCode[x] == 'B' || seatCode[x] == 'R')
                    seatId |= 1 << (bits - x - 1);
            }
            return seatId;
        }
    }
}
