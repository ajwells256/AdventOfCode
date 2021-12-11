using System;
using System.Collections.Generic;


namespace AoC2020 {
    public class SeatSimulator : AoCStringReader {
        private char[,] _map;
        private int _width;
        private int _height;
        private bool _visible;
        private int _occupied;
        private List<Tuple<int, int>> _directions;

        public SeatSimulator(string filepath, int debugLevel = 0) : base(filepath, debugLevel) {
            _width = _lines[0].Length;
            _height = _lines.Length;
            _map = new char[_height, _width];

            _directions = new List<Tuple<int, int>>();
            for (int y = -1; y < 2; y++) {
                for (int x = -1; x < 2; x++) {
                    if (x != 0 || y != 0)
                        _directions.Add(new Tuple<int, int>(x, y));
                }
            }
        }

        public int Part1() {
            InitMap();
            _visible = false;
            _occupied = 4;
            while (RunSimulation()) {}
            return Count();
        }

        public int Part2() {
            InitMap();
            _visible = true;
            _occupied = 5;
            while (RunSimulation()) { }
            return Count();
        }

        /// <summary>
        /// Count the number of chars matching target in the vicinity of (x,y).
        /// _directions indicates the directions and magnitute in which to look.
        /// _visible indicates whether to search for first visible chair or not.
        /// </summary>
        /// <param name="x">x coord</param>
        /// <param name="y">y coord</param>
        /// <param name="target"></param>
        /// <returns>Number of surrounding chars meeting the criteria</returns>
        private int CountChar(int x, int y, char target) {
            int count = 0;
            foreach (Tuple<int, int> dir in _directions) {
                int dx = dir.Item1;
                int dy = dir.Item2;
                int mult = 1;
                while ((GetChar(x+(dx*mult), y+(dy*mult)) == '.') && _visible)
                    mult++;
                if (GetChar(x+(dx*mult), y+(dy*mult)) == target)
                    count++;
            }
            return count;
        }

        /// <summary>
        /// A safe reading of the char map
        /// </summary>
        /// <param name="x">x coord</param>
        /// <param name="y">y coord</param>
        /// <returns>the char found or bang if bounds were exceeded</returns>
        private char GetChar(int x, int y) {
            if (x < 0 || y < 0 || x >= _width || y >= _height)
                return '!';
            return _map[y, x];
        }

        /// <summary>
        /// Get the next value for a given point, given the rules of the simulation
        /// including _visible and _occupied values.
        /// </summary>
        /// <param name="x">x coord</param>
        /// <param name="y">y coord</param>
        /// <returns>Next char for this point</returns>
        private char GetNextChar(int x, int y) {
            char c = GetChar(x, y);
            int occupied = CountChar(x, y, '#');
            if (c == '.')
                return '.';
            if ((c == 'L' && occupied == 0) || (c == '#' && occupied < _occupied))
                return '#';
            return 'L';
        }

        /// <summary>
        /// Runs the simulation one iteration. 
        /// </summary>
        /// <returns>True if a seat changed state, false otherwise.</returns>
        private bool RunSimulation() {
            bool changed = false;
            char[,] newmap = new char[_height, _width];
            for (int y = 0; y < _height; y++) {
                for (int x = 0; x < _width; x++) {
                    char newchar = GetNextChar(x, y);
                    newmap[y,x] = newchar;
                    if (!changed && GetChar(x, y) != newchar)
                        changed = true;
                }
            }
            _map = newmap;
            return changed;
        }

        /// <summary>
        /// Count the number of target characters in the map.
        /// </summary>
        /// <param name="target"></param>
        /// <returns></returns>
        private int Count(char target = '#') {
            int count = 0;
            for (int y = 0; y < _height; y++) {
                for (int x = 0; x < _width; x++) {
                    if (GetChar(x, y) == target)
                        count++;
                }
            }
            return count;
        }

        private void InitMap() {
            for (int y = 0; y < _height; y++) {
                for (int x = 0; x < _width; x++) {
                    _map[y, x] = _lines[y][x];
                }
            }
        }

        private void PrintMap() {
            for (int y = 0; y < _height; y++) {
                for (int x = 0; x < _width; x++) {
                    DebugWrite(GetChar(x, y), 0);
                }
                DebugLog("", 0);
            }
        }
    }
}
