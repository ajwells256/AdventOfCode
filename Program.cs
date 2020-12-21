using System;
using System.Collections.Generic;

namespace AoC2020 {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Starting Advent of Code 2020");
            Day21();
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

        static void Day5() {
            SeatReader s = new SeatReader("inputs/d5p1.txt");
            Console.WriteLine($"Day 5 Part 1: {s.Part1()}");
            Console.WriteLine($"Day 5 Part 2: {s.Part2()}");
        }

        static void Day6() {
            CDFGroupAggregator g = new CDFGroupAggregator("inputs/d6p1.txt");
            Console.WriteLine($"Day 6 Part 1: {g.Part1()}");
            Console.WriteLine($"Day 6 Part 2: {g.Part2()}");
        }

        static void Day7() {
            BagColorTreeAnalyzer b = new BagColorTreeAnalyzer("inputs/d7p1.txt");
            Console.WriteLine($"Day 7 Part 1: {b.Part1()}");
            Console.WriteLine($"Day 7 Part 2: {b.Part2()}");
        }

        static void Day8() {
            BootCodeExecutor b = new BootCodeExecutor("inputs/d8p1.txt");
            Console.WriteLine($"Day 8 Part 1: {b.Part1()}");
            Console.WriteLine($"Day 8 Part 2: {b.Part2()}");
            Console.WriteLine($"Day 8 Part 2 v2: {b.Part2v2()}");
        }

        static void Day9() {
            XMASReader x = new XMASReader("inputs/d9p1.txt");
            Console.WriteLine($"Day 9 Part 1: {x.Part1()}");
            Console.WriteLine($"Day 9 Part 2: {x.Part2()}");
        }

        static void Day10() {
            JoltChainer j = new JoltChainer("inputs/d10p1.txt");
            Console.WriteLine($"Day 10 Part 1: {j.Part1()}");
            Console.WriteLine($"Day 10 Part 2: {j.Part2()}");
        }

        static void Day11() {
            SeatSimulator s = new SeatSimulator("inputs/d11.txt",2);
            Console.WriteLine($"Day 11 Part 1: {s.Part1()}");
            Console.WriteLine($"Day 11 Part 2: {s.Part2()}");
        }

        static void Day12() {
            ManhattanCalculator m = new ManhattanCalculator("inputs/d12.txt", 2);
            Console.WriteLine($"Day 12 Part 1: {m.Part1()}");
            Console.WriteLine($"Day 12 Part 2: {m.Part2()}");
        }
        static void Day13() {
            BusScheduler b = new BusScheduler("inputs/d13.txt");
            Console.WriteLine($"Day 13 Part 1: {b.Part1()}");
            Console.WriteLine($"Day 13 Part 2: {b.Part2()}");
        }

        static void Day14() {
            Docker d = new Docker("inputs/d14.txt");
            Console.WriteLine($"Day 14 Part 1: {d.Part1()}");
            Console.WriteLine($"Day 14 Part 2: {d.Part2()}");
        }

        static void Day15() {
            MemoryGame m = new MemoryGame();
            Console.WriteLine($@"Day 15 Part 1: {m.PlayGame(
                new List<int>(new int[] { 13, 16, 0, 12, 15, 1}),
                2020)}");
            Console.WriteLine($@"Day 15 Part 2: {m.PlayGame(
                new List<int>(new int[] { 13, 16, 0, 12, 15, 1 }),
                30000000)}");
        }

        static void Day16() {
            TicketScanner t = new TicketScanner("inputs/d16.txt");
            Console.WriteLine($@"Day 16 Part 1: {t.Part1()}");
            Console.WriteLine($@"Day 16 Part 2: {t.Part2v2()}");
        }

        static void Day17() {
            PocketDimension p = new PocketDimension("inputs/d17.txt");
            Console.WriteLine($"Day 17 Part 1: {p.Part1()}");
            Console.WriteLine($"Day 17 Part 2: {p.Part2()}");
        }

        static void Day18() {
            ExpressionEvaluator e = new ExpressionEvaluator("inputs/d18.txt", 1);
            Console.WriteLine($"Day 18 Part 1: {e.Part1()}");
            Console.WriteLine($"Day 18 Part 2: {e.Part2()}");
        }

        // static void Day19() {
        //     GrammarParser g = new GrammarParser("inputs/d19.txt", 1);
        //     Console.WriteLine($"Day 19 Part 1: {g.Part1()}");
        //     Console.WriteLine($"Day 19 Part 2: {g.Part2()}");
        // }

        static void Day20() {
            ImageTileConstructor i = new ImageTileConstructor("inputs/d20.txt", 1);
            Console.WriteLine($"Day 20 Part 1: {i.Part1()}");
            Console.WriteLine($"Day 20 Part 2: {i.Part2()}");
        }

        static void Day21() {
            IngredientParser i = new IngredientParser("inputs/d21.txt", 1);
            Console.WriteLine($"Day 21 Part 1: {i.Part1()}");
            Console.WriteLine($"Day 21 Part 2: {i.Part2()}");
        }
    }
}
