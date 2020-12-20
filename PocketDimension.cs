using System;
using System.Collections.Generic;


namespace AoC2020
{
    public class PocketDimension : AoCStringReader
    {
        private HashSet<Tuple<int, int, int>> _active;
        private HashSet<Tuple<int, int, int, int>> _active4;
        private int _register = 0;

        public PocketDimension(string filepath, int debugLevel = 0) : base(filepath, debugLevel)
        {
        }

        public int Part1()
        {
            InitGrid();
            for (int t = 0; t < 6; t++) {
                RunSimulation();
            }
            return _active.Count;
        }

        public int Part2()
        {
            InitGrid(true);
            for (int t = 0; t < 6; t++)
            {
                RunSimulation4();
            }
            return _active4.Count;
        }

        private Tuple<int, int, int> T(int x, int y, int z) {
            return new Tuple<int, int, int>(x, y, z);
        }

        private Tuple<int, int, int, int> T(int x, int y, int z, int q)
        {
            return new Tuple<int, int, int, int>(x, y, z, q);
        }

        private void RunSimulation() {
            HashSet<Tuple<int,int,int>> add = new HashSet<Tuple<int, int, int>>();
            HashSet<Tuple<int, int, int>> remove = new HashSet<Tuple<int, int, int>>();
            HashSet<Tuple<int, int, int>> queue = new HashSet<Tuple<int, int, int>>();
            foreach (Tuple<int, int, int> act in _active) {
                int actneigh = ActiveNeighbors(act);
                if (!(actneigh == 2 || actneigh == 3))
                    remove.Add(act);
                ForeachNeighbor(act, (x, y, z) => queue.Add(T(x, y, z)));
            }
            queue.ExceptWith(_active);
            
            foreach (Tuple<int, int, int> inact in queue) {
                if (3 == ActiveNeighbors(inact))
                    add.Add(inact);
            }

            _active.ExceptWith(remove);
            _active.UnionWith(add);
        }

        private void RunSimulation4()
        {
            HashSet<Tuple<int, int, int, int>> add = new HashSet<Tuple<int, int, int, int>>();
            HashSet<Tuple<int, int, int, int>> remove = new HashSet<Tuple<int, int, int, int>>();
            HashSet<Tuple<int, int, int, int>> queue = new HashSet<Tuple<int, int, int, int>>();
            foreach (Tuple<int, int, int, int> act in _active4)
            {
                _register = 0;
                ForeachNeighbor(act, (x, y, z, q) => 
                    _register += _active4.Contains(T(x, y, z, q)) ? 1 : 0);
                if (!(_register == 2 || _register == 3))
                    remove.Add(act);
                ForeachNeighbor(act, (x, y, z, q) => queue.Add(T(x, y, z, q)));
            }
            queue.ExceptWith(_active4);

            foreach (Tuple<int, int, int, int> inact in queue)
            {
                _register = 0;
                ForeachNeighbor(inact, (x, y, z, q) =>
                    _register += _active4.Contains(T(x, y, z, q)) ? 1 : 0);
                if (3 == _register)
                    add.Add(inact);
            }

            _active4.ExceptWith(remove);
            _active4.UnionWith(add);
        }

        private void ForeachNeighbor(Tuple<int, int, int> tup, Action<int, int, int> act) {
            ForeachNeighbor(tup.Item1, tup.Item2, tup.Item3, act);
        }

        private void ForeachNeighbor(int X, int Y, int Z, Action<int, int, int> act) {
            for (int x = -1; x< 2; x++) {
                for (int y = -1; y< 2; y++) {
                    for (int z = -1; z< 2; z++) {
                        if (x == 0 && y == 0 && z == 0)
                            continue;
                        act(X+x, Y+y, Z+z);
                    }
                }
            }
        }

        private void ForeachNeighbor(Tuple<int, int, int, int> tup, Action<int, int, int, int> act)
        {
            ForeachNeighbor(tup.Item1, tup.Item2, tup.Item3, tup.Item4, act);
        }

        private void ForeachNeighbor(int X, int Y, int Z, int Q, Action<int, int, int, int> act)
        {
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    for (int z = -1; z < 2; z++)
                    {
                        for (int q = -1; q < 2; q++)
                        {
                            if (x == 0 && y == 0 && z == 0 && q == 0)
                                continue;
                            act(X + x, Y + y, Z + z, Q + q);
                        }
                    }
                }
            }
        }

        private int ActiveNeighbors(Tuple<int, int, int> tup) {
            return ActiveNeighbors(tup.Item1, tup.Item2, tup.Item3);
        }
        private int ActiveNeighbors(int X, int Y, int Z) {
            int count = 0;
            for (int x = -1; x < 2; x++) {
                for (int y = -1; y < 2; y++) {
                    for (int z = -1; z < 2; z++) {
                        if (x == 0 && y == 0 && z == 0)
                            continue;
                        if (_active.Contains(T(X+x, Y+y, Z+z)))
                            count++;
                    }
                }
            }
            return count;
        }

        private void InitGrid(bool four = false)
        {
            if (four)
                _active4 = new HashSet<Tuple<int, int, int, int>>();
            else
                _active = new HashSet<Tuple<int, int, int>>();
            for (int y = 0; y < _lines.Length; y++) {
                for (int x = 0; x < _lines[0].Length; x++) {
                    if (_lines[y][x] == '#') {
                        if (four) {
                            _active4.Add(T(x, y, 0, 0));
                        } else {
                            _active.Add(T(x, y, 0));
                        }
                    }
                }
            }
        }

    }
}
