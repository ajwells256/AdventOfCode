using System;
using System.IO;
using System.Linq;


namespace AoC2020
{
    public class MapReader : AoCBase
    {
        private string[] _map;
        private int _width;
        private int _height;

        private enum Coord {
            Tree,
            Blank
        }

        public MapReader(string filepath, int debugLevel = 0) : base(debugLevel)
        {
            _map = ReadFile(filepath);
            _width = _map[0].Length;
            _height = _map.Length;
        }

        public int Part1(int x_step = 3, int y_step = 1)
        {
            int trees = 0;
            int y, x = 0;
            for (y = 0; y < _height; y+=y_step) {
                if (GetCoord(x, y) == Coord.Tree)
                    trees++;
                x += x_step;
            }
            return trees;
        }

        public int Part2()
        {
            int[] arr = new int[] {
                Part1(1, 1),
                Part1(),
                Part1(5, 1),
                Part1(7, 1),
                Part1(1, 2)
            };
            return arr.Aggregate(1, (acc, next) => acc*next);
        }

        private Coord GetCoord(int x, int y) {
            Coord c = Coord.Tree;
            if (y >= _height)
                throw new IndexOutOfRangeException("Off the map there be dragons");
            if (_map[y][x % _width] == '.')
                c = Coord.Blank;
            return c;
        } 

        private string[] ReadFile(string filepath)
        {
            string[] lines = File.ReadAllLines(filepath);
            return lines;
        }
    }
}
