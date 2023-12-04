using System.Diagnostics;
using System.Collections.Generic;
using System.Linq;
using System.IO;

namespace AoC2020
{
    public class BootCodeExecutor : AoCBase
    {
        private string[] _lines;
        private int _pc = 0;
        private int _acc = 0;

        private class State {
            public int ACC;
            public int PC;
            public HashSet<int> Seen;
        }

        public BootCodeExecutor(string filepath, int debugLevel = 0) : base(debugLevel)
        {
            _lines = ReadFile(filepath);
        }

        public int Part1()
        {
            _pc = 0;
            _acc = 0;
            HashSet<int> seen = new HashSet<int>();
            while (!seen.Contains(_pc)) {
                seen.Add(_pc);
                Execute();
            }
            return _acc;
        }

        public int Part2()
        {
            _pc = 0;
            _acc = 0;
            State oldState = null;
            HashSet<int> seen = new HashSet<int>();
            int EOF = _lines.Count();
            int debugCount = 0;
            while (_pc < EOF) {
                while (oldState == null) {
                    seen.Add(_pc);
                    oldState = DFSExecute(seen);
                }
                // create new copy of seen for branch
                seen = new HashSet<int>(seen);
                while (_pc < EOF && !seen.Contains(_pc)) {
                    seen.Add(_pc);
                    Execute();
                }
                if (seen.Contains(_pc)) {
                    // this branch failed
                    seen = oldState.Seen;
                    _pc = oldState.PC;
                    _acc = oldState.ACC;
                    // Do not error correct the instruction we branched on
                    // pc was already accounted for in seen set
                    Execute();
                    debugCount++;
                    DebugLog($"{debugCount} branch(s) failed; seen {seen.Count} pcs");
                    oldState = null;
                }
            }
            return _acc;
        }

        public int Part2v2()
        {
            _pc = 0;
            _acc = 0;
            State oldState = null;
            HashSet<int> seen = new HashSet<int>();
            int EOF = _lines.Count();
            int debugCount = 0;
            while (_pc < EOF)
            {
                while (oldState == null)
                {
                    seen.Add(_pc);
                    oldState = DFSExecute(seen);
                }
                while (_pc < EOF && !seen.Contains(_pc))
                {
                    seen.Add(_pc);
                    Execute();
                }
                if (seen.Contains(_pc))
                {
                    // this branch failed
                    _pc = oldState.PC;
                    _acc = oldState.ACC;
                    // Do not error correct the instruction we branched on
                    // pc was already counted
                    Execute();
                    debugCount++;
                    DebugLog($"{debugCount} branch(s) failed; seen {seen.Count} pcs");
                    oldState = null;
                }
            }
            return _acc;
        }


        private void Execute() {
            string op = _lines[_pc].Substring(0, 3);
            int arg = int.Parse(_lines[_pc].Substring(4));
            DebugLog($"{op} {arg}", 2);
            switch (op) {
                case "nop":
                    _pc++;
                    break;
                case "acc":
                    _pc++;
                    _acc += arg;
                    break;
                case "jmp":
                    _pc += arg;
                    break;
            }
        }

        /// <summary>
        /// Execute code, error correcting nop and jmp as it goes.
        /// </summary>
        /// <returns>A saved state if it corrected a code, null otherwise</returns>
        private State DFSExecute(HashSet<int> seen) {
            string op = _lines[_pc].Substring(0, 3);
            int arg = int.Parse(_lines[_pc].Substring(4));
            DebugLog($"{op} {arg}", 2);
            State oldState = null;
            switch (op) {
                case "nop": // jmp
                    oldState = new State {
                        Seen = seen,
                        PC = _pc,
                        ACC = _acc
                    };
                    _pc += arg;
                    break;
                case "acc":
                    _pc++;
                    _acc += arg;
                    break;
                case "jmp": // nop
                    oldState = new State
                    {
                        Seen = seen,
                        PC = _pc,
                        ACC = _acc
                    };
                    _pc++;
                    break;
            }
            return oldState;
        }

        private string[] ReadFile(string filepath)
        {
            string[] lines = File.ReadAllLines(filepath);
            return lines;
        }
    }
}
