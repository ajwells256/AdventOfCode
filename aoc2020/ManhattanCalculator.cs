using System;
using System.Collections.Generic;
using System.Linq;

namespace AoC2020
{
    public class ManhattanCalculator : AoCLineReader
    {
        private int _heading = 0;
        private int _east = 0;
        private int _north = 0;
        public ManhattanCalculator(string filepath, int debugLevel = 0) : base(filepath, debugLevel)
        {
        }

        /// <summary>
        /// </summary>
        /// <returns>Manhattan distance from starting point 0,0 after parsing the instructions</returns>
        public int Part1() {
            _east = 0;
            _north = 0;
            foreach (string line in _lines) {
                int val = int.Parse(line.Substring(1));
                switch (line[0]) {
                    case 'N':
                        _north += val;
                        break;
                    case 'S':
                        _north -= val;
                        break;
                    case 'E':
                        _east += val;
                        break;
                    case 'W':
                        _east -= val;
                        break;
                    case 'R':
                        _heading -= val;
                        break;
                    case 'L':
                        _heading += val;
                        break;
                    case 'F':
                        _north += val * (int)Math.Sin(Math.PI * (_heading / 180.0));
                        _east += val * (int)Math.Cos(Math.PI * (_heading / 180.0));
                        break;
                }
            }
            return Math.Abs(_north) + Math.Abs(_east);
        }

        /// <summary>
        /// Similar to part 1, but with slight modifications. Rotations
        /// are hard but the trig checks out. It's much easier to think of it
        /// in terms of angles.
        /// </summary>
        /// <returns>Manhattan distance from starting point 0,0 after parsing the instructions</returns>
        public int Part2() {
            _east = 0;
            _north = 0;
            int wpe = 10;
            int wpn = 1;
            foreach (string line in _lines)
            {
                int val = int.Parse(line.Substring(1));
                double theta, norm;
                switch (line[0]) {
                    case 'N':
                        wpn += val;
                        break;
                    case 'S':
                        wpn -= val;
                        break;
                    case 'E':
                        wpe += val;
                        break;
                    case 'W':
                        wpe -= val;
                        break;
                    case 'R':
                        theta = Math.Atan2(wpn, wpe);
                        norm = Math.Sqrt((wpe * wpe) + (wpn * wpn));
                        wpn = (int)Math.Round(Math.Sin(theta - Math.PI * (val / 180.0)) * norm);
                        wpe = (int)Math.Round(Math.Cos(theta - Math.PI * (val / 180.0)) * norm);
                        break;
                    case 'L':
                        theta = Math.Atan2(wpn, wpe);
                        norm = Math.Sqrt((wpe * wpe) + (wpn * wpn));
                        wpn = (int)Math.Round(Math.Sin(theta + Math.PI * (val / 180.0)) * norm);
                        wpe = (int)Math.Round(Math.Cos(theta + Math.PI * (val / 180.0)) * norm);
                        break;
                    case 'F':
                        _north += val * wpn;
                        _east += val * wpe;
                        break;
                }
            }
            return Math.Abs(_north) + Math.Abs(_east);
        }
    }
}
