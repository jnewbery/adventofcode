// TODO: implement the Bron-Kerbosch algorithm to find maximal cliques
// https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
use fxhash::{FxHashMap, FxHashSet};

fn expand_subsets(subsets: &FxHashSet<Vec<String>>, pairs: &FxHashMap<String, Vec<String>>) -> FxHashSet<Vec<String>> {
    let mut new_subsets = FxHashSet::default();
    for subset in subsets.iter() {
        for next in pairs.get(&subset[0]).unwrap() {
            if subset.contains(next) {
                continue;
            }
            if subset.into_iter().map(|s| pairs.get(s).unwrap()).all(|p| p.contains(next)) {
                let mut new_subset = subset.clone();
                new_subset.insert(0, next.clone());
                new_subset.sort();
                new_subsets.insert(new_subset);
            }
        }
    }
    new_subsets
}

pub fn solve(input: &str) -> String {
    let mut pairs: FxHashMap<String, Vec<String>> = FxHashMap::default();
    let mut best_subsets: FxHashSet<Vec<String>> = FxHashSet::default();
    for line in input.lines() {
        // println!("{:?}", line);
        let mut parts = line.split("-");
        let a = parts.next().unwrap().to_string();
        let b = parts.next().unwrap().to_string();
        pairs.entry(a.clone()).or_insert(Vec::new()).push(b.clone());
        pairs.entry(b.clone()).or_insert(Vec::new()).push(a.clone());
        for c in pairs.get(&a).unwrap() {
            if pairs.get(c).unwrap().contains(&b) {
                let mut new_trio = [a.clone(), b.clone(), c.clone()];
                new_trio.sort();
                best_subsets.insert(new_trio.to_vec());
            }
        }
    }
    while best_subsets.len() > 1 {
        // println!("{:?} best_subsets of len {}", best_subsets.len(), best_subsets.iter().next().unwrap().len());
        best_subsets = expand_subsets(&best_subsets, &pairs);
    }
    // println!("{:?} best_subsets", best_subsets.len());
    // println!("{:?} terminals", pairs.keys().len());
    // println!("{:?} pairs", pairs.values().map(Vec::len).sum::<usize>());
    // println!("{:?} best_subset", best_subsets);
    best_subsets.iter().next().unwrap().join(",")
}
