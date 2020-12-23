using System.Collections.Generic;
using System.Linq;

namespace AoC2020
{
    public class CupSimulator : AoCBase
    {
        public class LinkedList<T> {
            public T Data;
            public LinkedList<T> Next;
            public LinkedList<T> Prev;

            public LinkedList<T> RemoveNext(int n = 1) {
                LinkedList<T> cur = Next;
                LinkedList<T> head = cur;
                head.Prev = null;
                for (int i = 1; i < n; i++) {
                    cur = cur.Next;
                }

                Next = cur.Next;
                Next.Prev = this;
                cur.Next = null;

                return head;
            }

            public List<T> GetData() {
                LinkedList<T> cur = this;
                List<T> vals = new List<T>();
                while (cur != null) {
                    vals.Add(cur.Data);
                    cur = cur.Next;

                    // check for circular linked list
                    if (cur != null && cur.Equals(this))
                        break;
                }
                return vals;
            }

            public LinkedList<T> Add(T data) {
                Next = new LinkedList<T>() {
                    Data = data,
                    Prev = this
                };
                return Next;
            }

            public void Append(LinkedList<T> list) {
                LinkedList<T> temp = Next;
                Next = list;
                LinkedList<T> cur = list;
                cur.Prev = this;
                while (cur.Next != null)
                    cur = cur.Next;
                cur.Next = temp;
                temp.Prev = cur;
            }
        }

        private string _startingState;
        public CupSimulator(string startingState, int debugLevel = 0) : base(debugLevel)
        {
            _startingState = startingState;
        }

        public string Part1() {
            Dictionary<int, LinkedList<int>> dict = Init();
            LinkedList<int> head = dict[int.Parse(_startingState.Substring(0, 1))];
            Cycle(dict, head, 100);
            head = dict[1].Next;
            string output = "1";
            while (head.Data != 1) {
                output = $"{output}{head.Data}";
                head = head.Next;
            }
            return output;
        }

        public long Part2() {
            Dictionary<int, LinkedList<int>> dict = Init(true);
            LinkedList<int> head = dict[int.Parse(_startingState.Substring(0, 1))];

            for (int i = 0; i < 1000000; i++) {

            }

            Cycle(dict, head, 10000000);
            head = dict[1];
            return (long)head.Next.Data * (long)head.Next.Next.Data;
        }

        private void Cycle(Dictionary<int, LinkedList<int>> dict, LinkedList<int> head, int cycles, int remove = 3) {
            LinkedList<int> snip;
            LinkedList<int> next = head;
            int minCup = dict.Keys.Min();
            int maxCup = dict.Keys.Max();
            for (int i = 0; i < cycles; i++) {
                snip = next.RemoveNext(remove);
                List<int> snipped = snip.GetData();

                int destCup = next.Data - 1;
                while (!dict.ContainsKey(destCup) || snipped.Contains(destCup)) {
                    destCup--;
                    if (destCup < minCup) {
                        destCup = maxCup;
                    }
                }

                dict[destCup].Append(snip);
                next = next.Next;
            }
        }

        private Dictionary<int, LinkedList<int>> Init(bool million = false) {
            LinkedList<int> head = null;
            LinkedList<int> cur = head;
            Dictionary<int, LinkedList<int>> dict = new Dictionary<int, LinkedList<int>>();
            foreach(char c in _startingState) {
                if (head == null) {
                    head = new LinkedList<int>() {
                        Data = int.Parse(c.ToString())
                    };
                    cur = head;
                    dict.Add(cur.Data, cur);
                } else {
                    cur = cur.Add(int.Parse(c.ToString()));
                    dict.Add(cur.Data, cur);
                }
            }
            if (million) {
                int n = dict.Keys.Max();
                int N = 1000000 - dict.Count();
                for (int i = 0; i < N; i++) {
                    n++;
                    cur = cur.Add(n);
                    dict.Add(cur.Data, cur);
                }
            }

            cur.Next = head;
            head.Prev = cur;
            return dict;
        }

    }
}