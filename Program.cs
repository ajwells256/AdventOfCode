using System;

namespace AoC2020 {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Starting Advent of Code 2020");
            Day1();
            // Day2();
            // Day3();
            // Day4();
            // Day5();
            Day6();
        }

        static void Day1() {
            SetSearcher s = new SetSearcher("inputs/d1p1.txt");
            Console.WriteLine($"Day 1 Part 1: {s.Part1()}");
            // Console.WriteLine($"Day 1 Part 1: {s.Part1Original()}");
            Console.WriteLine($"Day 1 Part 2: {s.Part2()}");
        }

        static void Day2() {
            PasswordChecker c = new PasswordChecker("inputs/d2p1.txt");
            Console.WriteLine($"Day 2 Part 1: {c.Part1()}");
            Console.WriteLine($"Day 2 Part 2: {c.Part2()}");
        }

        static void Day3() {
            MapReader m = new MapReader("inputs/d3p1.txt");
            Console.WriteLine($"Day 3 Part 1: {m.Part1()}");
            Console.WriteLine($"Day 3 Part 2: {m.Part2()}");
        }

        static void Day4() {
            PassportValidator p = new PassportValidator("inputs/d4p1.txt");
            Console.WriteLine($"Day 4 Part 1: {p.Part1()}");
            Console.WriteLine($"Day 4 Part 2: {p.Part2()}");
        }

        static void Day5()
        {
            SeatReader s = new SeatReader("inputs/d5p1.txt");
            Console.WriteLine($"Day 5 Part 1: {s.Part1()}");
            Console.WriteLine($"Day 5 Part 2: {s.Part2()}");
        }

        static void Day6()
        {
            CDFGroupAggregator g = new CDFGroupAggregator("inputs/d6p1.txt");
            Console.WriteLine($"Day 6 Part 1: {g.Part1()}");
            Console.WriteLine($"Day 6 Part 2: {g.Part2()}");
        }
    }
}
