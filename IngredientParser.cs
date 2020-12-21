using System.Linq;
using System.Collections.Generic;

namespace AoC2020
{
    public class IngredientParser : AoCLineReader
    {
        private Dictionary<string, HashSet<string>> _allergenCandidates;
        private Dictionary<string, int> _ingredientCount;
        public IngredientParser(string filepath, int debugLevel = 0) : base(filepath, debugLevel)
        {
            ParseAllergenCandidates();
        }

        public int Part1() {
            // Get a single set with each of the ingredients that were not cleared.
            HashSet<string> risky = new HashSet<string>();
            foreach (HashSet<string> candidate in _allergenCandidates.Values) {
                risky.UnionWith(candidate);
            }

            // Count occurances of each ingredient except the risky ones.
            int count = 0;
            foreach (string ingredient in _ingredientCount.Keys.Except(risky)) {
                count += _ingredientCount[ingredient];
            }
            return count;
        }

        public string Part2() {
            IEnumerable<string> certain;
            
            // While there exist ingredients|allergen pairs that haven't been confirmed
            while (_allergenCandidates.Where(x => x.Value.Count > 1).Count() > 0) {
                // Get a list of the ingredient names we are certain about
                certain = _allergenCandidates
                    .Where(x => x.Value.Count == 1)
                    .Select(x => x.Value.First());
                // (Try to) remove each locked in ingredient from each unconfirmed set
                foreach (string ingredient in certain) {
                    foreach (HashSet<string> s in _allergenCandidates.Values) {
                        if (s.Count > 1) {
                            s.RemoveWhere(x => x.Equals(ingredient));
                        }
                    }
                }
            }
            // Sorting by key, then fetching the values in order
            List<KeyValuePair<string, string>> toSort = _allergenCandidates
                .Select(x => new KeyValuePair<string, string>(x.Key, x.Value.First()))
                .ToList();
            toSort.Sort((p1, p2) => p1.Key.CompareTo(p2.Key));
            return toSort.Aggregate("", (acc, next) => $"{acc},{next.Value}").Substring(1);
        }

        private void ParseAllergenCandidates() {
            _allergenCandidates = new Dictionary<string, HashSet<string>>();
            _ingredientCount = new Dictionary<string, int>();
            foreach (string line in _lines) {
                int containsIdx = line.IndexOf('(');
                if (containsIdx > 0) {
                    // A set of all ingredients. Assumes that there are no duplicate ingredients
                    HashSet<string> ingredients = line
                        .Substring(0, containsIdx-1)
                        .Split(' ')
                        .ToHashSet();

                    // Keep track of the number of times ingredients appear
                    foreach (string ingredient in ingredients) {
                        if (_ingredientCount.ContainsKey(ingredient)) {
                            _ingredientCount[ingredient]++;
                        } else {
                            _ingredientCount.Add(ingredient, 1);
                        }
                    }

                    // Get the allergens for this product
                    int allergenIdx = containsIdx + "(contains ".Length;
                    string[] allergens = line
                        .Substring(allergenIdx, line.IndexOf(')')-allergenIdx)
                        .Split(", ");
                    
                    // Advent of Code assumes that only one ingredient can produce an allergen. Said another way,
                    // if 2 products have peanuts, the same ingredient in both is the source of the peanut.
                    // This translates into set intersection between ingredient lists from multiple products
                    // having the same allergens.
                    foreach (string a in allergens) {
                        if (_allergenCandidates.ContainsKey(a)) {
                            _allergenCandidates[a].IntersectWith(ingredients);
                        } else {
                            _allergenCandidates.Add(a, new HashSet<string>(ingredients));
                        }
                    }
                }
            }
        }
    }
}