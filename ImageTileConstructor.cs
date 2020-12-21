using System.Linq;
using System.Collections.Generic;
using System;

namespace AoC2020
{
    public class ImageTileConstructor : AoCStringReader 
    {
        /// <summary>
        /// Maps borders to the tile ids of the tiles that have it
        /// </summary>
        private Dictionary<string, HashSet<int>> _borders;
        private Dictionary<int, Tile> _tiles;
        private IEnumerable<int> _corners;

        private string[] _monster = new string[] {
            "                  # ",
            "#    ##    ##    ###",
            " #  #  #  #  #  #   "
        };
        private class Tile {
            public int TID;
            public List<string> Chars;
            public Tile(int tid) {
                TID = tid;
                Chars = new List<string>();
            }

            public Tile(int tid, List<string> chars) {
                TID = tid;
                Chars = chars;
            }

            /// <summary>
            /// Returns a new Tile with a new character map after rotating the donor Tile
            /// r times clockwise.
            /// </summary>
            /// <param name="r">Number of rotations clockwise.</param>
            /// <returns></returns>
            public Tile RotateClockwise(int r) {
                List<string> oldChars = Chars;
                List<string> newChars = new List<string>(Chars.Count);
                for (int i = 0; i < r; i++) {
                    for (int j = 0; j < oldChars[0].Length; j++) {
                        newChars.Add(new string(oldChars.Select(x => x[j]).Reverse().ToArray()));
                    }
                    oldChars = newChars;
                    newChars = new List<string>(Chars.Count);
                }
                return new Tile(TID, oldChars);
            }

            public Tile FlipHorizontally() {
                List<string> newChars = new List<string>(Chars.Count);
                for (int i = 0; i < Chars.Count; i++) {
                    newChars.Add(new string(Chars[i].Reverse().ToArray()));
                }
                return new Tile(TID, newChars);
            }

            public Tile FlipVertically() {
                List<string> newChars = new List<string>(Chars.Count);
                for (int i = Chars.Count - 1; i >= 0; i--) {
                    newChars.Add(new string(Chars[i]));
                }
                return new Tile(TID, newChars);
            }

            public List<string> GetBorders() {
                List<string> output = new List<string>();
                output.Add(Chars.First()); // 0
                output.Add(new string(Chars.Select(x => x.Last()).ToArray())); // 1
                output.Add(Chars.Last()); // 2
                output.Add(new string(Chars.Select(x => x.First()).ToArray())); // 3
                for (int i = 0; i < 4; i++) {
                    output.Add(new string(output[i].Reverse().ToArray()));
                }
                return output;
            }

            /// <summary>
            /// Retrieves the specified border for the tile, safely wrapping around if the index is too large.
            /// </summary>
            /// <param name="edge"></param>
            /// <returns></returns>
            public string GetBorder(int edge) {
                string bbase = GetBorders()[edge % 4];
                return bbase;
            }

            public Tuple<int, int> GetTransformation(string border) {
                List<string> borders = GetBorders();
                int idx = borders.IndexOf(border);
                if (idx < 4) {
                    return new Tuple<int, int>(idx, 2);
                } else {
                    int rot = idx - 4;
                    int flip = idx % 2;
                    return new Tuple<int, int>(rot, flip);
                }
            }
        }

        public ImageTileConstructor(string filepath, int debugLevel = 0) : base(filepath, debugLevel)
        {
            _borders = new Dictionary<string, HashSet<int>>();
            _tiles = new Dictionary<int, Tile>();
            Init();
        }

        public long Part1() {
            IEnumerable<int> tiles = _borders.Where(kv => kv.Value.Count() == 1).Select(kv => kv.Value.First());
            IEnumerable<Tuple<int, int>> query = from t in tiles 
                        group t by t into g 
                        select new Tuple<int, int>(g.Key, g.Count());
            _corners = query.Where(x => x.Item2 == 4)
                .Select(x => x.Item1);
            long result = query.Where(x => x.Item2 == 4)
                .Select(x => x.Item1)
                .Aggregate(1L, (acc, next) => acc *= (long)next);
            return result;
        }

        public int Part2() {
            if (_corners == null)
                Part1();
            
            Tile corner = _tiles[_corners.First()];
            while (_borders[corner.GetBorder(0)].Count != 1 && _borders[corner.GetBorder(3)].Count != 1)
                corner = corner.RotateClockwise(1);
            
            Tile[,] grid = new Tile[12,12];
            grid[0,0] = corner;
            grid = Stitch(grid, 0, 1);
            Char[,] image = new Char[grid.GetLength(0)*(corner.Chars[0].Length-2), grid.GetLength(1)*(corner.Chars.Count-2)];
            for (int y = 0; y < image.GetLength(1); y++) {
                for (int x = 0; x < image.GetLength(0); x++) {
                    Tile t = grid[x >> 3, y >> 3];
                    image[x, y] = t.Chars[(y % 8) + 1][(x % 8) + 1];
                    DebugWrite(image[x, y]);
                }
                DebugLog("");
            }
            Tile monster = new Tile(0, _monster.ToList());
            for (int j = 0; j < 4; j++) {
                if (j == 1)
                    monster = monster.FlipHorizontally();
                else if (j == 2)
                    monster = monster.FlipVertically();
                else if (j == 3)
                    monster = monster.FlipHorizontally(); // so, just a vertial flip
                for (int i = 0; i < 4; i++) {
                    int monsters = DrawMonsters(image, monster);
                    DebugLog(monsters);
                    if (monsters > 0) {
                        break;
                    }
                    monster.RotateClockwise(1);
                }
            }
            return CountChars(image);
        }

        private int CountChars(Char[,] image, Char c = '#') {
            int count = 0;
            for (int y = 0; y < image.GetLength(1); y++) {
                for (int x = 0; x < image.GetLength(0); x++) {
                    if (image[x,y] == c)
                        count++;
                    DebugWrite(image[x, y]);
                }
                DebugLog("");
            }
            return count;
        }

        private void Init() {
            Tile t = null;
            int tid = 0;
            foreach (string line in _lines) {
                if (line.Equals(""))
                    continue;
                if (line.Contains("Tile")) {
                    string id = line.Substring(
                        line.IndexOf(' ')+1,
                        line.IndexOf(':') - line.IndexOf(' ') - 1
                    );
                    DebugLog(id, 2);
                    tid = int.Parse(id);
                    t = new Tile(tid);
                    _tiles.Add(tid, t);
                    continue;
                }
                
                t.Chars.Add(line);
            }

            foreach (KeyValuePair<int, Tile> kv in _tiles) {
                List<string> tborders = kv.Value.GetBorders();
                foreach (string border in tborders)
                    AddBorder(kv.Key, border); 
            }
        }

        private int DrawMonsters(Char[,] image, Tile monsterTile) {
            int count = 0;
            List<Tuple<int, int>> body = new List<Tuple<int, int>>();
            for (int y = 0; y < monsterTile.Chars.Count; y++) {
                for (int x = 0; x < monsterTile.Chars[0].Length; x++) {
                    if (monsterTile.Chars[y][x] == '#')
                        body.Add(new Tuple<int, int>(x, y));
                }
            }
            for (int y = 0; y < image.GetLength(1) - monsterTile.Chars.Count; y++) {
                for (int x = 0; x < image.GetLength(0) - monsterTile.Chars[0].Length; x++) {
                    bool monster = true;
                    foreach (Tuple<int, int> seg in body) {
                        if (image[x + seg.Item1, y + seg.Item2] != '#') {
                            monster = false;
                            break;
                        }
                    }
                    if (monster) {
                        count++;
                        foreach (Tuple<int, int> seg in body) {
                            image[x + seg.Item1, y + seg.Item2] = '@';
                        }
                    }
                }
            }
            return count;
        }

        private void AddBorder(int tid, string border) {
            if (!_borders.ContainsKey(border))
                _borders.Add(border, new HashSet<int>());
            _borders[border].Add(tid);
        }

        private Tile[,] Stitch(Tile[,] grid, int X = 0, int Y = 0) {
            for (int x = X; x < grid.GetLength(0); x++) {
                for (int y = 0; y < grid.GetLength(1); y++) {
                    if (grid[x,y] != null)
                        continue;
                    if (y == 0) {
                        grid[x, y] = PickNextTile(grid[x - 1, y], x, y, 1);
                        continue;
                    }
                    grid[x, y] = PickNextTile(grid[x, y - 1], x, y, 2);
                }
            }
            return grid;
        }

        private Tile PickNextTile(Tile old, int x, int y, int edge) {
            string target = old.GetBorder(edge);
            Tile nextTile = _tiles[_borders[target].Except(new int[] { old.TID }).First()];
            string actual = nextTile.GetBorder(edge + 2);
            while (!(target.Equals(actual) || target.Equals(new string(actual.Reverse().ToArray())))) {
                nextTile = nextTile.RotateClockwise(1);
                actual = nextTile.GetBorder(edge + 2);
            }
            if (!target.Equals(actual))
                if (edge % 2 == 0)
                    nextTile = nextTile.FlipHorizontally();
                else
                    nextTile = nextTile.FlipVertically();
            if (!target.Equals(nextTile.GetBorder(edge + 2)))
                throw new Exception("You done messed up");
            return nextTile;
        }
    }
}